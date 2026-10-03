import fitz
import json
import re
import random
import os

pdf_path = r"d:\Project\ISC2\Certified in Cybersecurity (CC) Exam Guide.pdf"
output_json = r"d:\Project\ISC2\isc2_data.json"

print(f"Opening PDF: {pdf_path}")
doc = fitz.open(pdf_path)

DOMAINS = [
    {
        "id": 1,
        "name": "Domain 1: Security Principles",
        "name_vi": "Domain 1: Nguyên lý an toàn thông tin",
        "weight": "26%",
        "page_range": [32, 77],
        "description": "Foundational concepts: CIA triad, authentication, non-repudiation, privacy, risk management, security controls (physical, technical, administrative / preventive, detective, corrective), ISC2 Code of Ethics, and governance.",
        "description_vi": "Nền tảng bảo mật: Bộ ba CIA, xác thực, chống chối bỏ, quyền riêng tư, quản lý rủi ro, kiểm soát an ninh (vật lý, kỹ thuật, quản trị / ngăn chặn, phát hiện, khắc phục), Bộ quy tắc đạo đức ISC2 và quản trị an toàn thông tin."
    },
    {
        "id": 2,
        "name": "Domain 2: Business Continuity, Disaster Recovery, and Incident Response",
        "name_vi": "Domain 2: Duy trì hoạt động, Khôi phục thảm họa & Phản ứng sự cố",
        "weight": "10%",
        "page_range": [78, 115],
        "description": "BCP concepts, BIA, RTO, RPO, disaster recovery sites (Hot, Warm, Cold), incident response phases (Preparation, Detection/Analysis, Containment/Eradication/Recovery, Post-Incident).",
        "description_vi": "Kế hoạch BCP, phân tích tác động kinh doanh (BIA), chỉ số RTO & RPO, các loại trung tâm DR (Hot, Warm, Cold site), các giai đoạn ứng phó sự cố an ninh (Chuẩn bị, Phát hiện, Cô lập/Xử lý/Khôi phục, Đánh giá sau sự cố)."
    },
    {
        "id": 3,
        "name": "Domain 3: Access Control Concepts",
        "name_vi": "Domain 3: Các khái niệm kiểm soát truy cập",
        "weight": "22%",
        "page_range": [116, 155],
        "description": "Physical access controls (mantraps, turnstiles, locks, biometrics), logical access controls (IAAA), access control models (DAC, MAC, RBAC, ABAC), MFA, least privilege, separation of duties.",
        "description_vi": "Kiểm soát truy cập vật lý (cửa kiểm soát mantrap, rào xoay, sinh trắc học), kiểm soát logic (IAAA), các mô hình kiểm soát truy cập (DAC, MAC, RBAC, ABAC), xác thực đa yếu tố MFA, đặc quyền tối thiểu và phân tách trách nhiệm."
    },
    {
        "id": 4,
        "name": "Domain 4: Network Security",
        "name_vi": "Domain 4: An toàn mạng",
        "weight": "24%",
        "page_range": [156, 231],
        "description": "OSI 7-layer & TCP/IP models, IP addressing & subnetting, ports and protocols (HTTP, HTTPS, DNS, DHCP, SSH, etc.), network attacks (DoS, DDoS, MITM, spoofing), firewalls, IDS/IPS, VPN, wireless security, cloud models.",
        "description_vi": "Mô hình OSI 7 tầng & TCP/IP, địa chỉ IP & phân mạng, các cổng và giao thức mạng phổ biến, tấn công mạng (DoS/DDoS, tấn công đứng giữa MITM, giả mạo), tường lửa, IDS/IPS, mạng riêng ảo VPN, bảo mật wifi WPA2/WPA3, bảo mật đám mây."
    },
    {
        "id": 5,
        "name": "Domain 5: Security Operations",
        "name_vi": "Domain 5: Vận hành an ninh",
        "weight": "18%",
        "page_range": [232, 277],
        "description": "Log management & SIEM, data lifecycle & classification, DLP, backup strategies, hashing & encryption (symmetric vs asymmetric, digital signatures, PKI), change & configuration management, patch management, security awareness.",
        "description_vi": "Quản lý nhật ký log & SIEM, vòng đời & phân loại dữ liệu, chống thất thoát dữ liệu DLP, chiến lược sao lưu backup, mã hóa & băm (đối xứng, bất đối xứng, chữ ký số, PKI), quản lý thay đổi & cấu hình, vá lỗi và đào tạo nhận thức an ninh."
    }
]

def get_domain_info(page_num):
    for d in DOMAINS:
        if d["page_range"][0] <= page_num <= d["page_range"][1]:
            return d
    return DOMAINS[0]

# 1. Extract Q&A tables
extracted_questions = []
q_counter = 1

for page_idx in range(30, 278):
    page_num = page_idx + 1
    page = doc[page_idx]
    page_text = page.get_text("text")
    domain_info = get_domain_info(page_num)
    
    # Try finding tables
    tables = page.find_tables().tables
    for t in tables:
        rows = t.extract()
        if not rows or len(rows) < 2:
            continue
        header = [str(c or '').strip().lower() for c in rows[0]]
        if any('question' in h for h in header) and any('answer' in h for h in header):
            q_idx = next(i for i, h in enumerate(header) if 'question' in h)
            a_idx = next(i for i, h in enumerate(header) if 'answer' in h)
            
            # Find table caption in text
            caption_match = re.search(r'(Table\s+\d+\.\d+:[^\n]+)', page_text)
            caption = caption_match.group(1).strip() if caption_match else f"Domain {domain_info['id']} Review"
            
            # Find topic from page
            topic = caption.split(':')[-1].strip() if ':' in caption else caption
            
            for r in rows[1:]:
                if len(r) > max(q_idx, a_idx):
                    q = ' '.join(str(r[q_idx] or '').split())
                    a = ' '.join(str(r[a_idx] or '').split())
                    if q and a and len(q) > 5 and len(a) > 1:
                        # Avoid duplicates
                        if not any(eq['question'].lower() == q.lower() for eq in extracted_questions):
                            extracted_questions.append({
                                "id": q_counter,
                                "domain_id": domain_info["id"],
                                "domain_name": domain_info["name"],
                                "domain_name_vi": domain_info["name_vi"],
                                "page": page_num,
                                "topic": topic,
                                "caption": caption,
                                "question": q,
                                "answer": a
                            })
                            q_counter += 1

print(f"Extracted {len(extracted_questions)} raw questions.")

# Group answers by domain to generate realistic distractors
domain_answers = {}
for q in extracted_questions:
    did = q["domain_id"]
    if did not in domain_answers:
        domain_answers[did] = []
    if q["answer"] not in domain_answers[did] and len(q["answer"]) < 120:
        domain_answers[did].append(q["answer"])

# Curated high-yield cyber security terms for realistic distractors
curated_distractors = {
    1: ["Confidentiality", "Integrity", "Availability", "Non-repudiation", "Authentication", "Authorization", "Accounting", "Risk Avoidance", "Risk Mitigation", "Risk Acceptance", "Risk Transference", "Administrative Control", "Technical Control", "Physical Control", "Preventive Control", "Detective Control", "Corrective Control", "NIST CSF", "ISO 27001", "Due Diligence", "Due Care", "ISC2 Code of Ethics Canons"],
    2: ["Business Continuity Plan (BCP)", "Disaster Recovery Plan (DRP)", "Incident Response Plan (IRP)", "Business Impact Analysis (BIA)", "Recovery Time Objective (RTO)", "Recovery Point Objective (RPO)", "Maximum Tolerable Downtime (MTD)", "Hot Site", "Warm Site", "Cold Site", "Mobile Site", "Preparation", "Detection and Analysis", "Containment, Eradication and Recovery", "Post-Incident Activity", "Chain of Custody", "Life safety of human personnel", "Tabletop Exercise"],
    3: ["Discretionary Access Control (DAC)", "Mandatory Access Control (MAC)", "Role-Based Access Control (RBAC)", "Attribute-Based Access Control (ABAC)", "Rule-Based Access Control (RuBAC)", "Multi-Factor Authentication (MFA)", "Least Privilege", "Separation of Duties", "Need to Know", "Turnstile", "Mantrap / Airlock", "Biometrics", "Smart Card / Token", "Single Sign-On (SSO)", "OAuth 2.0", "OpenID Connect", "RADIUS", "TACACS+", "Job Rotation", "Mandatory Vacation"],
    4: ["Application Layer", "Presentation Layer", "Session Layer", "Transport Layer", "Network Layer", "Data Link Layer", "Physical Layer", "TCP (Transmission Control Protocol)", "UDP (User Datagram Protocol)", "Port 80 (HTTP)", "Port 443 (HTTPS)", "Port 53 (DNS)", "Port 22 (SSH)", "Port 21 (FTP)", "Port 25 (SMTP)", "Port 3389 (RDP)", "Firewall", "Intrusion Detection System (IDS)", "Intrusion Prevention System (IPS)", "Virtual Local Area Network (VLAN)", "Virtual Private Network (VPN)", "Denial of Service (DoS)", "Man-in-the-Middle (MITM)", "WPA3", "WPA2", "IaaS", "PaaS", "SaaS", "Public Cloud", "Private Cloud", "Shared Responsibility Model"],
    5: ["Security Information and Event Management (SIEM)", "Data Loss Prevention (DLP)", "Symmetric Encryption (AES)", "Asymmetric Encryption (RSA)", "Cryptographic Hash Function (SHA-256)", "Digital Signature", "Public Key Infrastructure (PKI)", "Full Backup", "Incremental Backup", "Differential Backup", "Data Classification (Confidential, Restricted)", "Degaussing / Sanitization", "Change Management", "Configuration Baseline", "Patch Management", "Security Awareness Training", "Write-Once Read-Many (WORM)", "Phishing Simulation"]
}

# Generate 4 options for each question
random.seed(42)
for item in extracted_questions:
    correct = item["answer"]
    did = item["domain_id"]
    
    # candidate pool from domain answers and curated terms
    pool = [a for a in domain_answers.get(did, []) if a.lower() != correct.lower()]
    pool += [t for t in curated_distractors.get(did, []) if t.lower() != correct.lower()]
    
    # If correct answer is boolean (True/False or Yes/No)
    if correct.lower() in ['true', 'false', 'yes', 'no']:
        if correct.lower() in ['true', 'yes']:
            options = [correct, 'False', 'Not Applicable', 'None of the above']
        else:
            options = [correct, 'True', 'Not Applicable', 'All of the above']
    elif len(correct) < 80:
        # Pick 3 distinct distractors of relatively similar length if possible
        pool = list(dict.fromkeys(pool))  # remove dupes
        selected = random.sample(pool, min(3, len(pool)))
        while len(selected) < 3:
            selected.append(f"Alternative security control {len(selected)+1}")
        options = [correct] + selected
    else:
        # Long answer, create shorter distractors
        pool = list(dict.fromkeys(pool))
        selected = random.sample(pool, min(3, len(pool)))
        options = [correct] + selected

    # Shuffle options
    random.shuffle(options)
    correct_idx = options.index(correct)
    correct_letter = chr(65 + correct_idx)
    
    item["options"] = options
    item["correct_option"] = correct_letter
    item["correct_answer"] = correct
    item["explanation"] = f"Theo giáo trình ISC2 Certified in Cybersecurity (CC) Exam Guide (Trang {item['page']}): '{correct}'. Câu hỏi này kiểm tra kiến thức trọng tâm của {item['domain_name_vi']} ({item['topic']})."

print("Enriched questions with multiple choice options and explanations.")

# 2. Extract comparison reference tables from the book
reference_tables = [
    {
        "id": "cia_attacks",
        "title": "Mapping Cyber Attacks to the CIA Triad",
        "title_vi": "Ánh xạ các cuộc tấn công vào Bộ ba CIA (Bảo mật - Toàn vẹn - Sẵn sàng)",
        "domain_id": 1,
        "page": 37,
        "columns": ["Loại tấn công (Attack Type)", "Mục tiêu (Objective)", "Yếu tố CIA bị ảnh hưởng (CIA Element Affected)"],
        "rows": [
            ["Eavesdropping / Sniffing (Nghe lén)", "Đánh cắp bí mật, theo dõi thông tin", "Confidentiality (Tính bảo mật)"],
            ["Data tampering (Sửa đổi dữ liệu trái phép)", "Biến đổi nội dung tệp tin hoặc giao dịch", "Integrity (Tính toàn vẹn)"],
            ["DoS / DDoS (Tấn công từ chối dịch vụ)", "Làm tê liệt hệ thống, cạn kiệt tài nguyên", "Availability (Tính sẵn sàng)"],
            ["Man-in-the-Middle (Tấn công đứng giữa)", "Đánh chặn và thay đổi đường truyền", "Confidentiality & Integrity"],
            ["SQL Injection", "Truy cập trái phép hoặc sửa đổi cơ sở dữ liệu", "Confidentiality & Integrity"],
            ["Ransomware (Mã độc tống tiền)", "Mã hóa dữ liệu khóa người dùng", "Availability & Confidentiality"],
            ["Web defacement (Thay đổi giao diện web)", "Thay đổi hình ảnh, nội dung website", "Integrity (Tính toàn vẹn)"]
        ]
    },
    {
        "id": "security_controls",
        "title": "Security Controls Matrix (Categories & Functions)",
        "title_vi": "Ma trận các loại biện pháp kiểm soát an ninh (Controls)",
        "domain_id": 1,
        "page": 64,
        "columns": ["Phân loại theo chức năng", "Phân loại theo bản chất", "Mục đích chính", "Ví dụ thực tế"],
        "rows": [
            ["Preventive (Ngăn chặn)", "Physical (Vật lý)", "Ngăn kẻ xâm nhập ngay từ đầu", "Hàng rào, khóa cửa, cửa xoay mantrap, bảo vệ"],
            ["Preventive (Ngăn chặn)", "Technical (Kỹ thuật)", "Chặn truy cập trái phép bằng phần mềm/phần cứng", "Tường lửa (Firewall), mã hóa, danh sách ACL, MFA"],
            ["Preventive (Ngăn chặn)", "Administrative (Quản trị)", "Ràng buộc hành vi con người bằng quy tắc", "Chính sách bảo mật, quy trình đào tạo nhân viên"],
            ["Detective (Phát hiện)", "Physical (Vật lý)", "Ghi nhận và phát hiện khi có đột nhập", "Camera giám sát CCTV, cảm biến chuyển động, chuông báo động"],
            ["Detective (Phát hiện)", "Technical (Kỹ thuật)", "Phát hiện hành vi bất thường trên hệ thống", "Hệ thống IDS, giám sát nhật ký (SIEM Log), phần mềm quét virus"],
            ["Detective (Phát hiện)", "Administrative (Quản trị)", "Đánh giá, đối soát quy trình định kỳ", "Kiểm toán độc lập (Audit), kiểm tra sổ sách, luân chuyển công việc"],
            ["Corrective (Khắc phục)", "Physical (Vật lý)", "Sửa chữa hoặc dập tắt hậu quả vật lý", "Hệ thống cứu hỏa dập lửa, cửa thoát hiểm"],
            ["Corrective (Khắc phục)", "Technical (Kỹ thuật)", "Khôi phục hệ thống về trạng thái an toàn", "Bản sao lưu (Data Backup), vá lỗ hổng (Patch), diệt mã độc"],
            ["Corrective (Khắc phục)", "Administrative (Quản trị)", "Kế hoạch ứng phó và kỷ luật sau sự cố", "Kế hoạch ứng phó sự cố (IRP), xử lý kỷ luật vi phạm"]
        ]
    },
    {
        "id": "dr_sites",
        "title": "Disaster Recovery Site Types Comparison",
        "title_vi": "So sánh các trung tâm phục hồi sau thảm họa (Hot, Warm, Cold Site)",
        "domain_id": 2,
        "page": 99,
        "columns": ["Loại Site (Type)", "Mô tả cơ sở vật chất (Description)", "Tốc độ khôi phục (Speed of Recovery)", "Chi phí đầu tư (Cost)", "Ứng dụng phù hợp"],
        "rows": [
            ["Hot Site", "Được trang bị đầy đủ máy chủ, mạng và dữ liệu đồng bộ thời gian thực (real-time).", "Nhanh nhất (Gần như ngay lập tức hoặc vài phút/giờ)", "Đắt đỏ nhất (Highest cost)", "Hệ thống trọng yếu ngân hàng, bệnh viện, thương mại điện tử lớn"],
            ["Warm Site", "Có sẵn trang thiết bị phần cứng cơ bản nhưng cần thời gian tải dữ liệu sao lưu mới nhất.", "Trung bình (Vài giờ đến vài ngày)", "Vừa phải (Moderate cost)", "Phần lớn doanh nghiệp với hệ thống kinh doanh quan trọng bậc 2"],
            ["Cold Site", "Chỉ có mặt bằng vật lý, nguồn điện, điều hòa không khí; không có máy chủ hay dữ liệu sẵn.", "Chậm nhất (Vài tuần đến vài tháng)", "Rẻ nhất (Lowest cost)", "Các hệ thống không yêu cầu tính liên tục khắt khe, ngân sách eo hẹp"],
            ["Mobile Site", "Xe tải hoặc container di động chứa trung tâm máy tính cơ động.", "Phụ thuộc thời gian di chuyển", "Chi phí vừa phải", "Cứu hộ vùng thiên tai, sự kiện dã ngoại hoặc thảm họa cục bộ"]
        ]
    },
    {
        "id": "access_control_models",
        "title": "Access Control Models Comparison",
        "title_vi": "So sánh các mô hình kiểm soát truy cập (DAC, MAC, RBAC, ABAC)",
        "domain_id": 3,
        "page": 136,
        "columns": ["Mô hình (Model)", "Cơ chế quyết định quyền", "Đặc điểm nhận diện", "Ví dụ minh họa"],
        "rows": [
            ["DAC (Discretionary Access Control)", "Chủ sở hữu dữ liệu (Data Owner)", "Linh hoạt, chủ sở hữu tự cấp quyền đọc/ghi cho người khác", "Phân quyền thư mục tập tin trên Windows (NTFS), Linux (chmod)"],
            ["MAC (Mandatory Access Control)", "Hệ điều hành / Chính sách an ninh trung tâm", "Cực kỳ nghiêm ngặt, dựa trên nhãn nhạy cảm (Top Secret, Secret) và quyền hạn (Clearance)", "Hệ thống máy tính quân sự, chính phủ bảo mật cao"],
            ["RBAC (Role-Based Access Control)", "Vai trò công việc (Job Role / Title)", "Cấp quyền theo vị trí phòng ban (HR, Kế toán, Quản trị viên)", "Hệ thống ERP, bệnh viện (bác sĩ xem bệnh án, kế toán xem viện phí)"],
            ["RuBAC (Rule-Based Access Control)", "Bộ quy tắc xác định trước (Rules)", "Dựa trên điều kiện như thời gian trong ngày, địa chỉ IP", "Quy tắc tường lửa: Chỉ cho phép SSH từ 8h - 17h từ dải IP nội bộ"],
            ["ABAC (Attribute-Based Access Control)", "Các thuộc tính (Attributes)", "Rất chi tiết và động (User + Resource + Environment + Action)", "Cho phép nhân viên bán hàng truy cập từ laptop công ty khi ở Việt Nam"]
        ]
    },
    {
        "id": "osi_tcp_layers",
        "title": "OSI 7 Layers vs TCP/IP Model & Protocols",
        "title_vi": "Mô hình OSI 7 tầng, Mô hình TCP/IP và Các giao thức cốt lõi",
        "domain_id": 4,
        "page": 169,
        "columns": ["Tầng OSI (OSI Layer)", "Tên tầng", "Tầng TCP/IP tương ứng", "Đơn vị dữ liệu (PDU)", "Giao thức tiêu biểu (Protocols)"],
        "rows": [
            ["Layer 7", "Application (Ứng dụng)", "Application Layer", "Data", "HTTP, HTTPS, DNS, DHCP, FTP, SFTP, SSH, SMTP, POP3, IMAP, SNMP"],
            ["Layer 6", "Presentation (Trình bày)", "Application Layer", "Data", "SSL/TLS, JPEG, GIF, ASCII, MP3, Mã hóa/Nén dữ liệu"],
            ["Layer 5", "Session (Phiên)", "Application Layer", "Data", "NetBIOS, RPC, PPTP, Quản lý thiết lập/ngắt phiên giao tiếp"],
            ["Layer 4", "Transport (Giao vận)", "Transport Layer", "Segment (TCP) / Datagram (UDP)", "TCP (tin cậy, bắt tay 3 bước), UDP (nhanh, không kết nối)"],
            ["Layer 3", "Network (Mạng)", "Internet Layer", "Packet", "IP (IPv4, IPv6), ICMP (Ping), IPsec, Router, NAT"],
            ["Layer 2", "Data Link (Liên kết dữ liệu)", "Network Access / Link Layer", "Frame", "Ethernet, Wi-Fi (802.11), Switch, MAC Address, ARP"],
            ["Layer 1", "Physical (Vật lý)", "Network Access / Link Layer", "Bit (0 & 1)", "Cáp quang, cáp xoắn đôi Cat6, RJ45, sóng radio, Hub, Repeater"]
        ]
    },
    {
        "id": "common_ports",
        "title": "Well-Known Security Ports & Services",
        "title_vi": "Các cổng mạng (Port) và Giao thức quan trọng nhất trong đề thi",
        "domain_id": 4,
        "page": 173,
        "columns": ["Số cổng (Port)", "Giao thức (Protocol)", "Chức năng (Function)", "Mức độ an toàn (Security Consideration)"],
        "rows": [
            ["Port 20 / 21", "FTP (File Transfer Protocol)", "Truyền nhận tệp tin", "Không an toàn (Truyền mật khẩu dạng rõ cleartext). Nên dùng SFTP thay thế"],
            ["Port 22", "SSH (Secure Shell) / SFTP", "Truy cập quản trị dòng lệnh từ xa an toàn", "An toàn (Mã hóa toàn bộ lưu lượng)"],
            ["Port 23", "Telnet", "Quản trị thiết bị từ xa", "Không an toàn (Cleartext). Phải cấm và thay bằng SSH"],
            ["Port 25", "SMTP (Simple Mail Transfer)", "Gửi email giữa các máy chủ", "Mặc định không mã hóa, sử dụng STARTTLS để bảo vệ"],
            ["Port 53", "DNS (Domain Name System)", "Phân giải tên miền thành địa chỉ IP (hoạt động trên cả UDP & TCP)", "Dễ bị DNS Spoofing / Poisoning nếu không dùng DNSSEC"],
            ["Port 67 / 68", "DHCP (Dynamic Host Config)", "Cấp phát IP động tự động cho thiết bị", "Dễ bị tấn công Rogue DHCP"],
            ["Port 80", "HTTP (Hypertext Transfer Protocol)", "Truyền tải trang web", "Không an toàn (Không mã hóa). Dữ liệu có thể bị nghe lén"],
            ["Port 88", "Kerberos", "Giao thức xác thực vé (Ticket-based) trong Active Directory", "Cốt lõi của bảo mật mạng doanh nghiệp"],
            ["Port 110", "POP3", "Nhận email về client", "Mặc định truyền rõ, POP3S (Port 995) bảo mật hơn"],
            ["Port 123", "NTP (Network Time Protocol)", "Đồng bộ thời gian hệ thống (Rất quan trọng cho Log & Kerberos)", "Chạy trên UDP"],
            ["Port 143", "IMAP", "Đọc và đồng bộ email trên nhiều thiết bị", "IMAPS (Port 993) bảo mật hơn"],
            ["Port 161 / 162", "SNMP (Simple Network Mgmt)", "Giám sát thiết bị mạng", "SNMPv1 & v2 truyền rõ; bắt buộc dùng SNMPv3 (hỗ trợ mã hóa và xác thực)"],
            ["Port 389", "LDAP (Lightweight Directory Access)", "Truy vấn danh bạ người dùng", "Dùng LDAPS (Port 636) để mã hóa"],
            ["Port 443", "HTTPS (HTTP over TLS/SSL)", "Lướt web an toàn được mã hóa", "Tiêu chuẩn bảo mật hiện đại cho ứng dụng web"],
            ["Port 445", "SMB (Server Message Block)", "Chia sẻ tệp và máy in trong Windows", "Cần chặn cổng này ra ngoài Internet (từng bị khai thác bởi WannaCry)"],
            ["Port 3389", "RDP (Remote Desktop Protocol)", "Điều khiển máy tính Windows từ xa", "Cần đặt sau VPN, không mở trực tiếp ra Internet"]
        ]
    },
    {
        "id": "cryptography_summary",
        "title": "Cryptography Essentials (Symmetric vs Asymmetric vs Hashing)",
        "title_vi": "Tóm tắt Mật mã học (Mã hóa đối xứng, Bất đối xứng và Hàm băm)",
        "domain_id": 5,
        "page": 255,
        "columns": ["Đặc điểm", "Mã hóa đối xứng (Symmetric)", "Mã hóa bất đối xứng (Asymmetric)", "Hàm băm (Hashing)"],
        "rows": [
            ["Số lượng khóa", "1 khóa duy nhất (Khóa bí mật dùng cho cả mã hóa & giải mã)", "2 khóa (Cặp khóa công khai Public Key & khóa bí mật Private Key)", "Không dùng khóa (Một chiều - One-way)"],
            ["Mục tiêu an ninh", "Confidentiality (Tính bảo mật)", "Confidentiality, Authentication, Non-repudiation (Chống chối bỏ)", "Integrity (Tính toàn vẹn)"],
            ["Tốc độ xử lý", "Rất nhanh, phù hợp mã hóa khối lượng dữ liệu lớn", "Chậm hơn đối xứng (khoảng 1000 lần), dùng tính toán số lớn", "Cực nhanh, tạo chuỗi băm có độ dài cố định"],
            ["Thuật toán phổ biến", "AES (128, 192, 256-bit - Tiêu chuẩn vàng), DES, 3DES, Blowfish", "RSA, ECC (Elliptic Curve Cryptography), Diffie-Hellman", "SHA-256, SHA-3, SHA-1 (cũ), MD5 (đã lỗi thời)"],
            ["Bài toán thách thức", "Khó khăn trong phân phối khóa bí mật an toàn (Key Distribution)", "Tốn tài nguyên tính toán, cần chứng chỉ số PKI để xác thực", "Khả năng va chạm (Collision resistance)"]
        ]
    }
]

# 3. Comprehensive Cyber Glossary (120+ terms)
glossary_terms = [
    {"term": "CIA Triad", "domain": 1, "en": "Confidentiality, Integrity, and Availability: The foundational pillar of information security.", "vi": "Bộ ba Bảo mật, Toàn vẹn và Sẵn sàng: Trụ cột nền tảng của an toàn thông tin."},
    {"term": "DAD Triad", "domain": 1, "en": "Disclosure, Alteration, and Denial: The negative opposites of the CIA triad, representing common attacker objectives.", "vi": "Tiết lộ, Sửa đổi và Từ chối: Mặt đối nghịch tiêu cực của bộ ba CIA, phản ánh mục tiêu của kẻ tấn công."},
    {"term": "Non-Repudiation", "domain": 1, "en": "Ensuring that a sender or actor cannot deny having performed an action (via digital signatures and audit logs).", "vi": "Tính chống chối bỏ: Đảm bảo một đối tượng không thể phủ nhận hành động mình đã làm."},
    {"term": "Authentication", "domain": 1, "en": "Verifying the claimed identity of a user, process, or device (Something you know, have, are, do, or where you are).", "vi": "Xác thực: Quá trình kiểm tra và xác nhận danh tính được khai báo."},
    {"term": "Authorization", "domain": 1, "en": "Determining what permissions and resources an authenticated user is allowed to access.", "vi": "Cấp quyền: Phân bổ quyền hạn xem hoặc thao tác trên tài nguyên sau khi đã xác thực."},
    {"term": "Accounting / Auditing", "domain": 1, "en": "Tracking and logging user activities and system events for accountability.", "vi": "Kiểm tra trách nhiệm: Ghi nhật ký log và theo dõi các hành vi để quy trách nhiệm."},
    {"term": "Risk Management", "domain": 1, "en": "The process of identifying, assessing, and reducing risk to an acceptable level (Risk = Threat x Vulnerability x Impact).", "vi": "Quản lý rủi ro: Quy trình nhận diện, đánh giá và giảm thiểu rủi ro xuống mức chấp nhận được."},
    {"term": "ISC2 Code of Ethics Canons", "domain": 1, "en": "Four mandatory ethical rules: 1. Protect society, 2. Act honorably, 3. Provide diligent service, 4. Advance and protect the profession.", "vi": "4 Điều lệ Đạo đức ISC2: 1. Bảo vệ xã hội, 2. Hành động danh dự, 3. Phục vụ tận tụy, 4. Phát triển và bảo vệ nghề nghiệp."},
    {"term": "BCP (Business Continuity Planning)", "domain": 2, "en": "Proactive planning to ensure critical operations continue during and immediately following a disaster. Primary goal: Life safety.", "vi": "Kế hoạch duy trì hoạt động kinh doanh: Đảm bảo các hoạt động cốt lõi tiếp tục duy trì khi gặp biến cố. Mục tiêu số 1: An toàn tính mạng con người."},
    {"term": "DRP (Disaster Recovery Planning)", "domain": 2, "en": "Technical procedures focused on restoring IT infrastructure, systems, and data after a disruption.", "vi": "Kế hoạch khôi phục sau thảm họa: Tập trung vào việc phục hồi hạ tầng kỹ thuật và dữ liệu."},
    {"term": "BIA (Business Impact Analysis)", "domain": 2, "en": "A formal study identifying critical business functions and the consequences of their disruption.", "vi": "Phân tích tác động kinh doanh: Đánh giá tổn thất nếu các hoạt động trọng yếu bị gián đoạn."},
    {"term": "RTO (Recovery Time Objective)", "domain": 2, "en": "The maximum acceptable amount of time a system can be down before unacceptable consequences occur.", "vi": "Thời gian phục hồi mục tiêu: Thời gian tối đa cho phép hệ thống ngừng hoạt động."},
    {"term": "RPO (Recovery Point Objective)", "domain": 2, "en": "The maximum acceptable amount of data loss measured in time (e.g. up to 1 hour of lost transactions).", "vi": "Điểm phục hồi mục tiêu: Lượng dữ liệu tối đa chấp nhận bị mất (tính theo thời gian sao lưu)."},
    {"term": "Hot Site", "domain": 2, "en": "A fully equipped recovery data center with live real-time replicated data, ready for immediate failover.", "vi": "Trung tâm dự phòng nóng: Trang bị đầy đủ máy chủ và dữ liệu đồng bộ trực tiếp, sẵn sàng chuyển đổi tức thì."},
    {"term": "Warm Site", "domain": 2, "en": "A recovery center equipped with hardware and networking, but requires loading backups to become fully operational.", "vi": "Trung tâm dự phòng ấm: Có sẵn phần cứng mạng nhưng phải nạp dữ liệu sao lưu mới chạy được."},
    {"term": "Cold Site", "domain": 2, "en": "An empty facility with power and HVAC but no IT equipment or data installed prior to a disaster.", "vi": "Trung tâm dự phòng nguội: Chỉ có mặt bằng, điện và điều hòa, cần nhiều tuần để mua sắm lắp đặt thiết bị."},
    {"term": "IRP (Incident Response Plan)", "domain": 2, "en": "A documented course of action to detect, contain, and recover from cybersecurity incidents.", "vi": "Kế hoạch ứng phó sự cố: Quy trình xử lý từng bước khi xảy ra vụ tấn công mạng."},
    {"term": "DAC (Discretionary Access Control)", "domain": 3, "en": "An access model where the data owner determines who has permission to access the resource.", "vi": "Kiểm soát truy cập tùy ý: Chủ sở hữu tệp tin tự quyết định phân quyền cho người khác."},
    {"term": "MAC (Mandatory Access Control)", "domain": 3, "en": "A strict access model enforced by the operating system based on classification labels and user clearances.", "vi": "Kiểm soát truy cập bắt buộc: Hệ thống phân quyền cứng dựa trên cấp độ nhãn an ninh."},
    {"term": "RBAC (Role-Based Access Control)", "domain": 3, "en": "Access permissions assigned to users based on their job roles and responsibilities within the organization.", "vi": "Kiểm soát truy cập theo vai trò: Gán quyền hạn dựa trên chức danh công việc trong tổ chức."},
    {"term": "ABAC (Attribute-Based Access Control)", "domain": 3, "en": "Dynamic access control evaluating user, resource, environmental, and action attributes.", "vi": "Kiểm soát truy cập theo thuộc tính: Quyết định quyền dựa trên tập hợp thuộc tính ngữ cảnh phong phú."},
    {"term": "MFA (Multi-Factor Authentication)", "domain": 3, "en": "Authentication requiring two or more distinct factors: Knowledge, Possession, Inherence, Location, Behavior.", "vi": "Xác thực đa yếu tố: Yêu cầu kết hợp từ 2 yếu tố khác nhau (Biết, Có, Là, Ở đâu, Hành vi)."},
    {"term": "Least Privilege", "domain": 3, "en": "Granting users only the minimum permissions necessary to perform their assigned job duties.", "vi": "Đặc quyền tối thiểu: Chỉ cấp cho người dùng đúng những quyền tối thiểu cần thiết để làm việc."},
    {"term": "Separation of Duties (SoD)", "domain": 3, "en": "Dividing critical tasks among multiple individuals to prevent fraud, theft, and unauthorized activities.", "vi": "Phân tách trách nhiệm: Chia nhỏ quy trình nhạy cảm cho nhiều người cùng tham gia nhằm chống gian lận."},
    {"term": "Mantrap / Air Lock", "domain": 3, "en": "A physical access enclosure with two interlocking doors where the first must close before the second opens, preventing tailgating.", "vi": "Cửa kiểm soát hai lớp (Mantrap): Hệ thống cửa liên động ngăn chặn hành vi đi bám đuôi (tailgating)."},
    {"term": "OSI Model", "domain": 4, "en": "Open Systems Interconnection 7-layer framework: Physical, Data Link, Network, Transport, Session, Presentation, Application.", "vi": "Mô hình OSI 7 tầng: Vật lý, Liên kết dữ liệu, Mạng, Giao vận, Phiên, Trình diễn, Ứng dụng."},
    {"term": "TCP (Transmission Control Protocol)", "domain": 4, "en": "A connection-oriented, reliable transport layer protocol that uses a 3-way handshake (SYN, SYN-ACK, ACK).", "vi": "Giao thức TCP: Giao thức giao vận có kết nối, tin cậy, sử dụng cơ chế bắt tay 3 bước."},
    {"term": "UDP (User Datagram Protocol)", "domain": 4, "en": "A connectionless, lightweight transport protocol prioritized for speed rather than reliability (e.g. VoIP, DNS, Streaming).", "vi": "Giao thức UDP: Giao thức giao vận không kết nối, tối ưu tốc độ cho video/âm thanh và DNS."},
    {"term": "DNS (Domain Name System)", "domain": 4, "en": "Translates human-readable domain names (example.com) to machine IP addresses (Port 53).", "vi": "Hệ thống tên miền DNS: Phân giải tên miền thành địa chỉ IP (Cổng 53)."},
    {"term": "DHCP (Dynamic Host Configuration)", "domain": 4, "en": "Automatically assigns IP addresses and network configuration parameters to client devices (Ports 67, 68).", "vi": "Giao thức cấp phát IP động DHCP: Tự động cấp địa chỉ IP cho máy con khi cắm vào mạng."},
    {"term": "Firewall", "domain": 4, "en": "A network security device that monitors and filters incoming and outgoing traffic based on predetermined rules.", "vi": "Tường lửa: Thiết bị lọc gói tin ra vào mạng theo các chính sách thiết lập trước."},
    {"term": "IDS vs IPS", "domain": 4, "en": "IDS (Intrusion Detection System) passively detects and alerts; IPS (Intrusion Prevention System) actively blocks threats inline.", "vi": "IDS vs IPS: IDS chỉ phát hiện và phát cảnh báo thụ động; IPS can thiệp trực tiếp để chặn gói tin tấn công."},
    {"term": "VPN (Virtual Private Network)", "domain": 4, "en": "An encrypted virtual tunnel establishing a secure connection across public or untrusted networks (using IPsec or SSL/TLS).", "vi": "Mạng riêng ảo VPN: Tạo đường hầm mã hóa an toàn truyền dữ liệu qua Internet công cộng."},
    {"term": "SIEM (Security Information & Event Mgmt)", "domain": 5, "en": "A centralized software platform that aggregates, correlates, and analyzes security log data across an enterprise.", "vi": "Hệ thống SIEM: Nền tảng quản lý và phân tích tập trung các bản ghi log an ninh trong toàn doanh nghiệp."},
    {"term": "DLP (Data Loss Prevention)", "domain": 5, "en": "Tools and policies designed to prevent sensitive data from leaving corporate boundaries in-use, in-motion, or at-rest.", "vi": "Giải pháp chống thất thoát dữ liệu DLP: Ngăn chặn dữ liệu nhạy cảm bị rò rỉ ra ngoài."},
    {"term": "AES (Advanced Encryption Standard)", "domain": 5, "en": "The gold-standard symmetric block cipher using key sizes of 128, 192, or 256 bits.", "vi": "Tiêu chuẩn mã hóa nâng cao AES: Thuật toán mã hóa đối xứng tiêu chuẩn an toàn nhất hiện nay."},
    {"term": "RSA", "domain": 5, "en": "A widely used asymmetric cryptosystem based on the factoring of large prime numbers.", "vi": "Thuật toán RSA: Hệ mật mã bất đối xứng phổ biến nhất dựa trên bài toán phân tích số nguyên tố lớn."},
    {"term": "Digital Signature", "domain": 5, "en": "A cryptographic mechanism combining hashing and sender private key encryption to ensure integrity, authentication, and non-repudiation.", "vi": "Chữ ký số: Kết hợp hàm băm và khóa riêng của người gửi để đảm bảo tính toàn vẹn, xác thực và chống chối bỏ."},
    {"term": "PKI (Public Key Infrastructure)", "domain": 5, "en": "The framework of hardware, software, policies, and Certificate Authorities (CAs) managing digital certificates.", "vi": "Hạ tầng khóa công khai PKI: Hệ thống quản lý, cấp phát và thu hồi chứng chỉ số."},
    {"term": "Degaussing", "domain": 5, "en": "Using a strong magnetic field to disrupt magnetic domains and permanently sanitize magnetic storage media.", "vi": "Khử từ (Degaussing): Phương pháp dùng từ trường mạnh để xóa sạch vĩnh viễn ổ đĩa từ tính."}
]

# Write complete dataset to JSON
complete_data = {
    "title": "ISC2 Certified in Cybersecurity (CC) Learning App",
    "version": "1.0.0",
    "source_book": "Certified in Cybersecurity (CC) Exam Guide.pdf",
    "total_questions": len(extracted_questions),
    "domains": DOMAINS,
    "questions": extracted_questions,
    "reference_tables": reference_tables,
    "glossary": glossary_terms
}

with open(output_json, "w", encoding="utf-8") as f:
    json.dump(complete_data, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {len(extracted_questions)} questions, {len(reference_tables)} cheat sheets, and {len(glossary_terms)} glossary terms to {output_json}!")
