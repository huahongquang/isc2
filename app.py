import http.server
import socketserver
import webbrowser
import os
import json
import urllib.parse
import threading
import time
import sys

# Configure UTF-8 for console output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "isc2_data.json")
PDF_FILE = os.path.join(BASE_DIR, "Certified_in_Cybersecurity_CC_Exam_Guide.pdf")
if not os.path.exists(PDF_FILE):
    PDF_FILE = os.path.join(BASE_DIR, "Certified in Cybersecurity (CC) Exam Guide.pdf")

# Preload data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        APP_DATA = json.load(f)
else:
    APP_DATA = {"questions": [], "domains": [], "reference_tables": [], "glossary": []}

class ISC2RequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(APP_DATA, ensure_ascii=False).encode("utf-8"))
            return

        if path == "/api/pdf":
            if os.path.exists(PDF_FILE):
                self.send_response(200)
                self.send_header("Content-Type", "application/pdf")
                self.send_header("Content-Disposition", "inline; filename=\"Certified_in_Cybersecurity_CC_Exam_Guide.pdf\"")
                fs = os.path.getsize(PDF_FILE)
                self.send_header("Content-Length", str(fs))
                self.end_headers()
                with open(PDF_FILE, "rb") as f:
                    while chunk := f.read(65536):
                        self.wfile.write(chunk)
            else:
                self.send_error(404, "PDF File not found")
            return

        if path == "/" or path == "/index.html":
            self.path = "/index.html"

        return super().do_GET()

    def log_message(self, format, *args):
        pass

def find_open_port(start_port=8080):
    import socket
    port = start_port
    while port < start_port + 20:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
            port += 1
    return start_port

def run_server():
    port = find_open_port(8080)
    handler = ISC2RequestHandler
    
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        url = f"http://127.0.0.1:{port}"
        print("=" * 64)
        print("   ISC2 CERTIFIED IN CYBERSECURITY (CC) LEARNING PLATFORM")
        print("   Study Guide & Exam Practice Simulator")
        print("=" * 64)
        print(f"[*] Web Server URL: {url}")
        print(f"[*] Total Practice Questions: {len(APP_DATA.get('questions', []))} (5 Domains)")
        print(f"[*] Official Textbook: {os.path.basename(PDF_FILE)}")
        print(f"[*] Opening browser automatically... Press Ctrl+C to stop.")
        print("=" * 64)

        def open_browser():
            time.sleep(1)
            try:
                webbrowser.open(url)
            except Exception:
                pass

        threading.Thread(target=open_browser, daemon=True).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.shutdown()

if __name__ == "__main__":
    run_server()
