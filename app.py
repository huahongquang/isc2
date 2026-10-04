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
USERS_FILE = os.path.join(BASE_DIR, "users.json")
PDF_FILE = os.path.join(BASE_DIR, "Certified_in_Cybersecurity_CC_Exam_Guide.pdf")
if not os.path.exists(PDF_FILE):
    PDF_FILE = os.path.join(BASE_DIR, "Certified in Cybersecurity (CC) Exam Guide.pdf")

# Preload question & domain data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        APP_DATA = json.load(f)
else:
    APP_DATA = {"questions": [], "domains": [], "reference_tables": [], "glossary": []}

# Preload users data
DEFAULT_USERS = [
    {"id": "usr_superadmin", "username": "superadmin", "password": "123", "fullName": "Nguyễn Quản Trị Tối Cao", "role": "superadmin", "levelName": "Super Admin (Tối cao)", "roleBadge": "👑 Super Admin", "avatar": "SA", "email": "superadmin@isc2cc.vn", "status": "active", "created": "2026-10-01", "lastLogin": "Vừa xong"},
    {"id": "usr_admin", "username": "admin", "password": "123", "fullName": "Trần Chuyên Viên Bảo Mật", "role": "admin", "levelName": "Admin (Chuyên môn)", "roleBadge": "🛡️ Admin", "avatar": "AD", "email": "admin@isc2cc.vn", "status": "active", "created": "2026-10-02", "lastLogin": "Hôm nay"},
    {"id": "usr_manager", "username": "manager", "password": "123", "fullName": "Lê Quản Lý Đào Tạo", "role": "manager", "levelName": "Manager (Quản lý)", "roleBadge": "💼 Manager", "avatar": "MG", "email": "manager@isc2cc.vn", "status": "active", "created": "2026-10-02", "lastLogin": "Hôm qua"},
    {"id": "usr_staff", "username": "staff", "password": "123", "fullName": "Phạm Trợ Giảng Chuyên Đề", "role": "staff", "levelName": "Staff (Nhân viên/Trợ giảng)", "roleBadge": "📋 Staff", "avatar": "ST", "email": "staff@isc2cc.vn", "status": "active", "created": "2026-10-03", "lastLogin": "Hôm qua"},
    {"id": "usr_student", "username": "student", "password": "123", "fullName": "Đỗ Học Viên Chứng Chỉ CC", "role": "student", "levelName": "Student (Học viên)", "roleBadge": "🎓 Student", "avatar": "HV", "email": "student@isc2cc.vn", "status": "active", "created": "2026-10-03", "lastLogin": "Hôm nay"}
]

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return DEFAULT_USERS

def save_users(users):
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving users: {e}")

class ISC2RequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps(APP_DATA, ensure_ascii=False).encode("utf-8"))
            return

        if path == "/api/users" or path == "/api/auth/users":
            users = load_users()
            safe_users = [{k: v for k, v in u.items() if k != "password"} for u in users]
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps(safe_users, ensure_ascii=False).encode("utf-8"))
            return

        if path == "/api/pdf":
            if os.path.exists(PDF_FILE):
                self.send_response(200)
                self.send_header("Content-Type", "application/pdf")
                self.send_header("Content-Disposition", "inline; filename=\"Certified_in_Cybersecurity_CC_Exam_Guide.pdf\"")
                fs = os.path.getsize(PDF_FILE)
                self.send_header("Content-Length", str(fs))
                self.send_cors_headers()
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

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(length) if length > 0 else b"{}"
        
        try:
            body = json.loads(post_data.decode("utf-8"))
        except Exception:
            body = {}

        # 1. Login Authentication Endpoint
        if path == "/api/auth/login":
            username = body.get("username", "").strip().lower()
            password = body.get("password", "").strip()
            users = load_users()
            user = next((u for u in users if u.get("username", "").lower() == username and u.get("password") == password), None)

            if user:
                user["lastLogin"] = time.strftime("%Y-%m-%d %H:%M")
                save_users(users)
                safe_user = {k: v for k, v in user.items() if k != "password"}
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "user": safe_user}, ensure_ascii=False).encode("utf-8"))
            else:
                self.send_response(401)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "message": "Sai tên đăng nhập hoặc mật khẩu"}, ensure_ascii=False).encode("utf-8"))
            return

        # 2. User Management Endpoint
        if path == "/api/auth/users":
            users = load_users()
            new_user = {
                "id": body.get("id", f"usr_{int(time.time())}"),
                "username": body.get("username", "").strip(),
                "password": body.get("password", "123").strip(),
                "fullName": body.get("fullName", "").strip(),
                "role": body.get("role", "staff"),
                "levelName": body.get("levelName", "Staff"),
                "roleBadge": body.get("roleBadge", "📋 Staff"),
                "avatar": body.get("username", "US")[:2].upper(),
                "email": body.get("email", ""),
                "status": body.get("status", "active"),
                "created": time.strftime("%Y-%m-%d"),
                "lastLogin": "Chưa đăng nhập"
            }
            users.append(new_user)
            save_users(users)
            safe_user = {k: v for k, v in new_user.items() if k != "password"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "user": safe_user}, ensure_ascii=False).encode("utf-8"))
            return

        # 3. Add Custom Question Endpoint
        if path == "/api/questions":
            global APP_DATA
            new_q = {
                "id": body.get("id", len(APP_DATA.get("questions", [])) + 1),
                "domain_id": int(body.get("domain_id", 1)),
                "domain_name": body.get("domain_name", "Domain 1: Security Principles"),
                "question": body.get("question", ""),
                "options": body.get("options", {}),
                "correct_option": body.get("correct_option", "A"),
                "explanation": body.get("explanation", ""),
                "page": body.get("page", 1)
            }
            APP_DATA.setdefault("questions", []).append(new_q)
            try:
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump(APP_DATA, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"Error updating questions: {e}")
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "question": new_q}, ensure_ascii=False).encode("utf-8"))
            return

        self.send_error(404, "Endpoint not found")

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
        print("   Study Guide, Simulator & RBAC Admin Dashboard")
        print("=" * 64)
        print(f"[*] Web Server URL: {url}")
        print(f"[*] Roles: Super Admin | Admin | Manager | Staff | Student")
        print(f"[*] Total Practice Questions: {len(APP_DATA.get('questions', []))} (5 Domains)")
        print(f"[*] Official Textbook: {os.path.basename(PDF_FILE)}")
        print(f"[*] Press Ctrl+C to stop.")
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
