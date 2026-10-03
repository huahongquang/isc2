import json

data_file = r"d:\Project\ISC2\isc2_data.json"

with open(data_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Rich Domain Study Summaries & Cheat Sheets
domain_summaries = [
    {
        "domain_id": 1,
        "title": "Domain 1: Security Principles (Nguyên lý an toàn thông tin)",
        "weight": "26%",
        "exam_tips": [
            "Ghi nhớ bộ ba CIA (Confidentiality, Integrity, Availability) và mặt đối nghịch DAD (Disclosure, Alteration, Denial).",
            "Mục tiêu quan trọng nhất trong mọi tình huống an ninh luôn là: AN TOÀN TÍNH MẠNG CON NGƯỜI (Human Life Safety).",
            "Nắm vững 4 điều lệ đạo đức ISC2 theo đúng thứ tự ưu tiên (Protect society -> Act honorably -> Diligent service -> Advance profession).",
            "Phân biệt rõ: Policy (Bắt buộc, mức cao), Standard (Bắt buộc, chi tiết kỹ thuật), Procedure (Quy trình từng bước), Guideline (Khuyến nghị, tùy ý).",
            "Công thức tính rủi ro: Risk = Threat x Vulnerability x Impact. Rủi ro định lượng: ALE = SLE x ARO."
        ],
        "sections": [
            {
                "heading": "1. Bộ ba CIA và Bộ ba DAD (CIA & DAD Triads)",
                "content": """- **Confidentiality (Tính bảo mật)**: Đảm bảo thông tin chỉ được truy cập bởi người có thẩm quyền. Bị đe dọa bởi: Sniffing/Eavesdropping, đánh cắp mật khẩu, kỹ nghệ xã hội (Social Engineering). Kiểm soát: Mã hóa (Encryption), kiểm soát truy cập (Access Control), phân loại dữ liệu.
- **Integrity (Tính toàn vẹn)**: Đảm bảo dữ liệu chính xác, đầy đủ và không bị sửa đổi trái phép. Bị đe dọa bởi: Data tampering, Man-in-the-Middle, SQL Injection. Kiểm soát: Hàm băm (Hashing - SHA-256), chữ ký số, kiểm soát phiên bản.
- **Availability (Tính sẵn sàng)**: Đảm bảo hệ thống và dữ liệu luôn có thể truy cập khi người dùng hợp pháp cần. Bị đe dọa bởi: DoS/DDoS, ransomware, mất điện, hỏa hoạn, lỗi phần cứng. Kiểm soát: Sao lưu (Backup), máy chủ dự phòng (Redundancy/Failover), cân bằng tải, RAID, UPS.
- **Mặt đối lập DAD**:
  + Confidentiality đối lập với **Disclosure** (Tiết lộ trái phép).
  + Integrity đối lập với **Alteration** (Sửa đổi trái phép).
  + Availability đối lập với **Denial** (Từ chối dịch vụ)."""
            },
            {
                "heading": "2. Khung IAAA và Tính chống chối bỏ (Non-Repudiation)",
                "content": """- **Identification (Định danh)**: Khai báo bạn là ai (Ví dụ: Nhập Username, quẹt thẻ ID).
- **Authentication (Xác thực)**: Chứng minh bạn đúng là người đó (Ví dụ: Nhập mật khẩu, quét vân tay).
- **Authorization (Cấp quyền)**: Xác định bạn được phép làm gì trên hệ thống (Ví dụ: Chỉ được đọc, hoặc được ghi).
- **Accounting / Auditing (Kiểm tra trách nhiệm)**: Ghi lại hành vi của bạn vào nhật ký hệ thống (Logs) để phục vụ giám sát và điều tra.
- **Non-Repudiation (Tính chống chối bỏ)**: Đảm bảo một bên không thể phủ nhận hành động họ đã thực hiện (như gửi email, duyệt giao dịch). Được đảm bảo thông qua **Chữ ký số (Digital Signatures)** kết hợp với **Audit Logs**."""
            },
            {
                "heading": "3. Quản lý rủi ro (Risk Management Process)",
                "content": """- **Khái niệm then chốt**:
  + **Asset (Tài sản)**: Mọi thứ có giá trị với tổ chức (Dữ liệu, máy chủ, danh tiếng).
  + **Threat (Mối đe dọa)**: Bất kỳ yếu tố nào có thể gây hại cho tài sản (Tin tặc, thiên tai, mã độc).
  + **Vulnerability (Lỗ hổng)**: Điểm yếu bảo mật trong phần mềm, cấu hình hoặc con người.
  + **Risk (Rủi ro)**: Khả năng mối đe dọa khai thác lỗ hổng gây thiệt hại (Risk = Threat x Vulnerability x Impact).
- **4 Phương án ứng phó rủi ro (Risk Treatments)**:
  + **Risk Avoidance (Tránh rủi ro)**: Loại bỏ hoàn toàn nguyên nhân rủi ro (Ví dụ: Ngừng cung cấp dịch vụ nguy hiểm, hủy bỏ dự án).
  + **Risk Transference / Sharing (Chuyển giao rủi ro)**: Đẩy gánh nặng tài chính sang bên thứ ba (Ví dụ: Mua bảo hiểm an ninh mạng, thuê đối tác ngoài).
  + **Risk Mitigation / Reduction (Giảm thiểu rủi ro)**: Triển khai các biện pháp kiểm soát an ninh để hạ thấp xác suất hoặc tác động (Ví dụ: Cài đặt tường lửa, mã hóa dữ liệu).
  + **Risk Acceptance (Chấp nhận rủi ro)**: Chấp nhận giữ lại rủi ro khi chi phí khắc phục lớn hơn giá trị tài sản (Phải do ban lãnh đạo phê duyệt)."""
            },
            {
                "heading": "4. Các loại biện pháp kiểm soát an ninh (Security Controls)",
                "content": """- **Phân loại theo bản chất (Nature)**:
  + **Physical (Vật lý)**: Hàng rào, bảo vệ, khóa cửa, cửa xoay, camera CCTV, bình chữa cháy.
  + **Technical / Logical (Kỹ thuật/Logic)**: Tường lửa, hệ thống IDS/IPS, mã hóa, mật khẩu, phân quyền ACL, MFA.
  + **Administrative / Managerial (Quản trị)**: Chính sách bảo mật, quy định đào tạo, lý lịch tư pháp, quy trình kiểm toán.
- **Phân loại theo chức năng (Function)**:
  + **Preventive (Ngăn chặn)**: Ngăn chặn sự cố trước khi nó xảy ra (Tường lửa, khóa cửa, chính sách).
  + **Detective (Phát hiện)**: Phát hiện và cảnh báo khi sự cố đang diễn ra (Camera CCTV, hệ thống IDS, rà soát nhật ký Log).
  + **Corrective (Khắc phục)**: Sửa chữa và khôi phục hệ thống sau sự cố (Bản sao lưu Backup, vá lỗ hổng Patch, diệt virus).
  + **Deterrent (Răn đe)**: Cảnh báo người vi phạm từ bỏ ý định (Biển báo camera, thông báo hình phạt).
  + **Compensating (Bù đắp)**: Biện pháp thay thế tạm thời khi biện pháp chính không thể triển khai."""
            },
            {
                "heading": "5. Bộ Quy tắc Đạo đức ISC2 (ISC2 Code of Ethics)",
                "content": """Mọi thành viên ISC2 bắt buộc phải tuân thủ 4 điều lệ đạo đức theo ĐÚNG THỨ TỰ ƯU TIÊN sau:
1. **Canon 1**: Bảo vệ xã hội, lợi ích chung, niềm tin thiết yếu của cộng đồng và hạ tầng quốc gia. (Protect society, the common good, necessary public trust and confidence, and the infrastructure).
2. **Canon 2**: Hành động danh dự, trung thực, công bằng, có trách nhiệm và tuân thủ pháp luật. (Act honorably, honestly, justly, responsibly, and legally).
3. **Canon 3**: Cung cấp dịch vụ mẫn cán, tận tụy và chuyên nghiệp cho các bên ủy thác. (Provide diligent and competent service to principals).
4. **Canon 4**: Phát triển và bảo vệ uy tín nghề nghiệp. (Advance and protect the profession)."""
            }
        ]
    },
    {
        "domain_id": 2,
        "title": "Domain 2: Business Continuity, Disaster Recovery, and Incident Response (Duy trì hoạt động, Khôi phục thảm họa & Phản ứng sự cố)",
        "weight": "10%",
        "exam_tips": [
            "Ưu tiên tối cao trong mọi kế hoạch BCP/DRP luôn là: SỰ AN TOÀN VÀ TÍNH MẠNG CON NGƯỜI.",
            "Phân biệt RTO (Thời gian phục hồi tối đa) và RPO (Lượng dữ liệu tối đa chấp nhận mất mát tính theo thời gian).",
            "So sánh 3 loại site: Hot Site (Nhanh nhất, đắt nhất), Warm Site (Vừa phải), Cold Site (Chậm nhất, rẻ nhất).",
            "Nắm vững 4 giai đoạn phản ứng sự cố: 1. Chuẩn bị -> 2. Phát hiện & Phân tích -> 3. Cô lập, Xử lý & Khôi phục -> 4. Đánh giá bài học kinh nghiệm.",
            "Chuỗi bảo quản bằng chứng số (Chain of Custody) là yếu tố bắt buộc để bằng chứng được chấp nhận tại tòa án."
        ],
        "sections": [
            {
                "heading": "1. Khái niệm BCP vs DRP vs IRP",
                "content": """- **BCP (Business Continuity Plan - Kế hoạch duy trì hoạt động kinh doanh)**: Tập trung vào cấp độ tổ chức/doanh nghiệp nhằm duy trì các chức năng kinh doanh thiết yếu trong và sau thảm họa. Mục tiêu là sự tồn tại của tổ chức.
- **DRP (Disaster Recovery Plan - Kế hoạch khôi phục sau thảm họa)**: Tập trung vào kỹ thuật và CNTT nhằm khôi phục máy chủ, mạng, ứng dụng và dữ liệu sau khi xảy ra thảm họa.
- **IRP (Incident Response Plan - Kế hoạch ứng phó sự cố)**: Tập trung vào các quy trình hành động tức thì để phát hiện, ngăn chặn và xử lý một vụ tấn công mạng cụ thể."""
            },
            {
                "heading": "2. Phân tích tác động kinh doanh (BIA) và Các chỉ số RTO, RPO",
                "content": """- **BIA (Business Impact Analysis)**: Quy trình xác định các quy trình kinh doanh trọng yếu, mức độ phụ thuộc và ước tính thiệt hại tài chính/danh tiếng khi gián đoạn.
- **MTD (Maximum Tolerable Downtime)**: Khoảng thời gian tối đa doanh nghiệp có thể chịu đựng gián đoạn trước khi phá sản hoặc không thể phục hồi.
- **RTO (Recovery Time Objective)**: Thời gian mục tiêu để khôi phục xong hệ thống sau thảm họa (RTO luôn phải nhỏ hơn MTD).
- **RPO (Recovery Point Objective)**: Điểm khôi phục mục tiêu tính theo thời gian sao lưu dữ liệu (Ví dụ: RPO = 2 giờ nghĩa là chấp nhận mất tối đa dữ liệu của 2 giờ gần nhất; nếu muốn RPO = 0 thì phải sao lưu đồng bộ theo thời gian thực)."""
            },
            {
                "heading": "3. Các loại trung tâm dự phòng (DR Site Types)",
                "content": """- **Hot Site (Site Nóng)**: Trang bị đầy đủ phần cứng, mạng và dữ liệu được đồng bộ hóa thời gian thực. Sẵn sàng hoạt động trong vài phút đến vài giờ. Chi phí đắt đỏ nhất.
- **Warm Site (Site Ấm)**: Đã lắp đặt sẵn máy chủ và kết nối mạng nhưng chưa có dữ liệu mới nhất. Cần thời gian để khôi phục dữ liệu từ bản sao lưu (mất vài giờ đến vài ngày). Chi phí vừa phải.
- **Cold Site (Site Nguội)**: Chỉ là mặt bằng vật lý có sẵn điện và điều hòa, hoàn toàn không có máy chủ hay dữ liệu. Mất từ vài tuần đến vài tháng để mua sắm lắp đặt. Chi phí thấp nhất.
- **Mobile Site (Site Di động)**: Trung tâm dữ liệu thu nhỏ đặt trên xe container cơ động, phục vụ ứng cứu khẩn cấp tại hiện trường."""
            },
            {
                "heading": "4. 4 Giai đoạn Phản ứng sự cố (Incident Response Phases)",
                "content": """Theo hướng dẫn NIST SP 800-61 / ISC2:
1. **Preparation (Chuẩn bị)**: Xây dựng chính sách, thành lập đội CSIRT/CERT, mua sắm công cụ giám sát, tổ chức diễn tập định kỳ.
2. **Detection & Analysis (Phát hiện & Phân tích)**: Giám sát cảnh báo từ SIEM/IDS, xác minh xem sự cố có thật hay là báo động giả (False Positive), đánh giá phạm vi ảnh hưởng.
3. **Containment, Eradication & Recovery (Cô lập, Triệt tiêu & Khôi phục)**:
   + *Containment*: Cách ly máy bị nhiễm khỏi mạng nội bộ để ngăn lây lan.
   + *Eradication*: Loại bỏ mã độc, xóa tài khoản backdoor, vá lỗ hổng bị khai thác.
   + *Recovery*: Khôi phục hệ thống từ bản sao lưu sạch, kiểm thử trước khi đưa vào sản xuất.
4. **Post-Incident Activity / Lessons Learned (Đánh giá sau sự cố)**: Tổ chức cuộc họp rút kinh nghiệm, lập báo cáo chi tiết, cập nhật lại quy trình ứng phó để không lặp lại sai lầm."""
            }
        ]
    },
    {
        "domain_id": 3,
        "title": "Domain 3: Access Control Concepts (Các khái niệm kiểm soát truy cập)",
        "weight": "22%",
        "exam_tips": [
            "Phân biệt rõ 4 mô hình: DAC (Chủ tài nguyên tự quyết), MAC (Hệ thống gán nhãn an ninh), RBAC (Theo vai trò chức danh), ABAC (Theo thuộc tính ngữ cảnh).",
            "MFA yêu cầu tối thiểu 2 yếu tố KHÁC NHAU từ 3 nhóm chính: Something you know, Something you have, Something you are. (2 mật khẩu KHÔNG phải là MFA).",
            "Nguyên tắc Đặc quyền tối thiểu (Least Privilege) và Phân tách nhiệm vụ (Separation of Duties) xuất hiện trong hầu hết các kịch bản thi.",
            "Cửa Mantrap là biện pháp kiểm soát vật lý hiệu quả nhất chống đi bám đuôi (Tailgating / Piggybacking)."
        ],
        "sections": [
            {
                "heading": "1. Các biện pháp kiểm soát truy cập vật lý (Physical Access Controls)",
                "content": """- **Hàng rào (Fencing)**: Rào cản đầu tiên ngăn chặn và định hướng luồng di chuyển.
- **Mantrap / Airlock (Cửa kiểm soát liên động 2 lớp)**: Khoang đệm có 2 cửa, cửa thứ nhất đóng kín thì cửa thứ hai mới mở được. Chỉ cho phép 1 người đi qua tại một thời điểm, loại bỏ triệt để hành vi đi bám đuôi (**Tailgating / Piggybacking**).
- **Cửa xoay (Turnstiles)**: Kiểm soát từng cá nhân quẹt thẻ trước khi vào sảnh tòa nhà.
- **Bảo vệ và Chó nghiệp vụ (Guards & Guard Dogs)**: Kiểm soát vật lý linh hoạt có tính răn đe rất cao.
- **CCTV & Cảm biến chuyển động**: Ghi hình và phát hiện kẻ đột nhập (Detective control)."""
            },
            {
                "heading": "2. Các mô hình kiểm soát truy cập logic (Access Control Models)",
                "content": """- **DAC (Discretionary Access Control)**: Do người tạo hoặc chủ sở hữu tài nguyên (Data Owner) toàn quyền quyết định ai được truy cập và phân quyền. Ví dụ: Phân quyền NTFS trên Windows, chmod trên Linux.
- **MAC (Mandatory Access Control)**: Mô hình nghiêm ngặt nhất, do hệ thống bắt buộc thực thi. Người dùng có mức cấp phép an ninh (Clearance), dữ liệu được gắn nhãn độ mật (Classification: Top Secret, Secret, Confidential). Người dùng chỉ được truy cập nếu mức Clearance >= nhãn của dữ liệu.
- **RBAC (Role-Based Access Control)**: Quyền hạn được gán cho các Vai trò (Roles) trong tổ chức, sau đó người dùng được gán vào vai trò tương ứng (Ví dụ: Bác sĩ, Y tá, Kế toán). Rất dễ quản lý khi nhân viên thay đổi vị trí.
- **RuBAC (Rule-Based Access Control)**: Quyền truy cập được xác định bởi các quy tắc logic cứng (Ví dụ: Quy tắc tường lửa - Chặn mọi truy cập ngoài giờ hành chính).
- **ABAC (Attribute-Based Access Control)**: Mô hình thế hệ mới linh hoạt nhất. Đánh giá tập hợp các thuộc tính: Người dùng (Phòng ban), Tài nguyên (Độ mật), Môi trường (Thời gian, vị trí IP, thiết bị), Hành động (Đọc/Ghi)."""
            },
            {
                "heading": "3. Xác thực đa yếu tố (Multi-Factor Authentication - MFA)",
                "content": """MFA yêu cầu từ 2 yếu tố thuộc các danh mục KHÁC NHAU:
1. **Something you know (Điều bạn biết)**: Mật khẩu (Password), mã PIN, câu hỏi bảo mật.
2. **Something you have (Thứ bạn có)**: Thẻ thông minh (Smartcard), mã OTP từ Authenticator app, Token phần cứng (YubiKey), tin nhắn SMS.
3. **Something you are (Đặc điểm cơ thể bạn)**: Dấu vân tay, quét mống mắt (Iris), quét võng mạc (Retina), nhận diện khuôn mặt.
- *Yếu tố bổ sung*:
  + **Somewhere you are (Nơi bạn đang ở)**: Tọa độ GPS, dải địa chỉ IP công ty.
  + **Something you do (Cách bạn hành động)**: Tốc độ gõ phím (Keystroke dynamics), dáng điệu ký tên."""
            },
            {
                "heading": "4. Các nguyên tắc quản trị tài khoản và nhân sự",
                "content": """- **Least Privilege (Đặc quyền tối thiểu)**: Người dùng chỉ được cấp các quyền hạn tối thiểu vừa đủ để hoàn thành nhiệm vụ được giao.
- **Need to Know (Nhu cầu cần biết)**: Chỉ cho phép tiếp cận thông tin khi có lý do chính đáng phục vụ công việc, dù người đó có cấp bậc cao.
- **Separation of Duties - SoD (Phân tách trách nhiệm)**: Chia tách quy trình nhạy cảm cho nhiều người (Ví dụ: Người lập lệnh chuyển tiền không được là người duyệt lệnh chuyển tiền).
- **Dual Control / Two-Person Rule**: Yêu cầu 2 người cùng có mặt thực hiện đồng thời một hành động tối mật (Ví dụ: 2 người cùng tra chìa khóa để mở két tiền).
- **Mandatory Vacation (Nghỉ phép bắt buộc) & Job Rotation (Luân chuyển công việc)**: Giúp phát hiện các hành vi gian lận hoặc sai phạm kéo dài của nhân viên."""
            }
        ]
    },
    {
        "domain_id": 4,
        "title": "Domain 4: Network Security (An toàn mạng)",
        "weight": "24%",
        "exam_tips": [
            "Thuộc lòng 7 tầng mô hình OSI (1-Physical, 2-Data Link, 3-Network, 4-Transport, 5-Session, 6-Presentation, 7-Application).",
            "Nhớ các cổng mạng quan trọng: SSH (22), DNS (53), HTTP (80), HTTPS (443), RDP (3389).",
            "Phân biệt TCP (Bắt tay 3 bước SYN-SYN/ACK-ACK, tin cậy) và UDP (Không kết nối, nhanh, VoIP/Streaming/DNS query).",
            "Dải IP riêng tư RFC 1918 không thể định tuyến ra Internet: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.",
            "Phân biệt IDS (Phát hiện và cảnh báo thụ động) và IPS (Đặt trên đường truyền - inline, chủ động chặn gói tin tấn công).",
            "Mô hình đám mây: SaaS (Nhà cung cấp quản lý nhiều nhất), IaaS (Khách hàng quản lý nhiều nhất)."
        ],
        "sections": [
            {
                "heading": "1. Mô hình OSI 7 tầng vs Mô hình TCP/IP",
                "content": """- **Layer 7 - Application (Ứng dụng)**: Giao diện trực tiếp với người dùng và ứng dụng. Giao thức: HTTP, HTTPS, DNS, DHCP, FTP, SSH, SMTP.
- **Layer 6 - Presentation (Trình diễn)**: Định dạng, nén và mã hóa/giải mã dữ liệu. Giao thức: SSL/TLS, ASCII, JPEG, MP3.
- **Layer 5 - Session (Phiên)**: Thiết lập, duy trì và giải phóng phiên liên lạc. Giao thức: RPC, NetBIOS, PPTP.
- **Layer 4 - Transport (Giao vận)**: Truyền dữ liệu đầu cuối (End-to-End). Đơn vị: Segment. Giao thức: TCP (Bắt tay 3 bước), UDP.
- **Layer 3 - Network (Mạng)**: Định tuyến gói tin qua các mạng khác nhau. Đơn vị: Packet. Thiết bị: Router. Giao thức: IPv4, IPv6, ICMP (Ping), IPsec.
- **Layer 2 - Data Link (Liên kết dữ liệu)**: Truyền dữ liệu giữa 2 thiết bị trong cùng mạng cục bộ. Đơn vị: Frame. Thiết bị: Switch. Địa chỉ: MAC Address (48 bit). Giao thức: Ethernet, Wi-Fi (802.11), ARP.
- **Layer 1 - Physical (Vật lý)**: Truyền các bit tín hiệu thô qua phương tiện vật lý. Đơn vị: Bit (0 và 1). Thiết bị: Cáp quang, cáp mạng Cat6, Hub, Repeater."""
            },
            {
                "heading": "2. Các hình thức tấn công mạng phổ biến",
                "content": """- **DoS / DDoS (Từ chối dịch vụ phân tán)**: Làm ngập băng thông hoặc cạn kiệt tài nguyên máy chủ bằng lượng truy cập khổng lồ từ mạng botnet (Ví dụ: SYN Flood, UDP Flood, Smurf Attack).
- **Man-in-the-Middle - MITM / On-Path Attack**: Kẻ tấn công đứng giữa chặn bắt và có thể sửa đổi dữ liệu truyền giữa 2 bên mà họ không hề hay biết (Phòng chống bằng mã hóa TLS/HTTPS).
- **Spoofing (Giả mạo)**: Giả mạo địa chỉ IP, địa chỉ MAC, hoặc tên miền (DNS Spoofing) để lừa hệ thống tin tưởng.
- **ARP Poisoning (Đầu độc bộ nhớ ARP)**: Kẻ tấn công gửi gói tin ARP giả mạo trong mạng LAN để liên kết địa chỉ MAC của mình với IP của Default Gateway, từ đó nghe lén toàn bộ mạng LAN."""
            },
            {
                "heading": "3. Hạ tầng phòng thủ an toàn mạng",
                "content": """- **Firewall (Tường lửa)**: Lọc lưu lượng truy cập mạng dựa trên địa chỉ IP nguồn/đích, cổng mạng và trạng thái kết nối (Stateful Inspection).
- **DMZ (Demilitarized Zone - Vùng phi quân sự)**: Vùng mạng trung gian cách ly các máy chủ công khai (Web server, Mail server) khỏi mạng nội bộ nhạy cảm.
- **VLAN (Virtual Local Area Network)**: Phân chia một mạng vật lý thành nhiều mạng logic riêng biệt để tăng cường bảo mật và giảm lưu lượng quảng bá broadcast.
- **VPN (Virtual Private Network)**: Tạo đường hầm mã hóa dữ liệu an toàn khi truyền qua Internet công cộng (Sử dụng IPsec hoặc OpenVPN).
- **Bảo mật Wi-Fi**: Chuẩn WEP và WPA đã lỗi thời và không an toàn. Tiêu chuẩn hiện đại là **WPA2 (sử dụng mã hóa AES-CCMP)** và **WPA3 (sử dụng cơ chế SAE - Simultaneous Authentication of Equals)** chống tấn công dò mật khẩu offline."""
            },
            {
                "heading": "4. Mô hình Điện toán đám mây (Cloud Computing)",
                "content": """- **3 Mô hình dịch vụ (Service Models)**:
  + **IaaS (Infrastructure as a Service)**: Khách hàng thuê hạ tầng phần cứng ảo hóa (VM, lưu trữ, mạng). Khách hàng chịu trách nhiệm quản lý HĐH, ứng dụng và dữ liệu (Ví dụ: AWS EC2, Azure VM).
  + **PaaS (Platform as a Service)**: Cung cấp nền tảng phát triển ứng dụng (Runtime, CSDL). Khách hàng chỉ quản lý code và dữ liệu (Ví dụ: Google App Engine, AWS Elastic Beanstalk).
  + **SaaS (Software as a Service)**: Cung cấp phần mềm hoàn chỉnh qua trình duyệt. Nhà cung cấp quản lý toàn bộ hệ thống (Ví dụ: Microsoft 365, Google Workspace, Salesforce).
- **Mô hình trách nhiệm chung (Shared Responsibility Model)**: Khách hàng luôn luôn chịu trách nhiệm về: BẢO MẬT DỮ LIỆU CỦA MÌNH trong mọi mô hình đám mây."""
            }
        ]
    },
    {
        "domain_id": 5,
        "title": "Domain 5: Security Operations (Vận hành an ninh)",
        "weight": "18%",
        "exam_tips": [
            "Nhớ 6 giai đoạn vòng đời dữ liệu: Tạo (Create) -> Lưu trữ (Store) -> Sử dụng (Use) -> Chia sẻ (Share) -> Lưu trữ lưu trữ (Archive) -> Hủy bỏ (Destroy).",
            "Phân biệt mã hóa đối xứng (1 khóa bí mật, rất nhanh - AES) và bất đối xứng (Cặp khóa Public/Private - RSA).",
            "Chữ ký số (Digital Signature) sử dụng khóa riêng (Private Key) của người gửi để ký và khóa công khai (Public Key) để kiểm tra, đảm bảo: Integrity, Authentication, Non-repudiation.",
            "Quy tắc sao lưu 3-2-1: 3 bản sao dữ liệu, trên 2 loại phương tiện lưu trữ khác nhau, với 1 bản đặt tại vị trí ngoại vi (off-site).",
            "Khử từ (Degaussing) chỉ có tác dụng với các phương tiện lưu trữ từ tính (băng từ, ổ đĩa HDD), KHÔNG hiệu quả với ổ SSD."
        ],
        "sections": [
            {
                "heading": "1. Quản lý Nhật ký (Log Management) & Hệ thống SIEM",
                "content": """- **Log (Nhật ký hệ thống)**: Bản ghi lại mọi hoạt động và sự kiện xảy ra trên thiết bị hoặc hệ điều hành.
- **Nguyên tắc an toàn cho Log**:
  + Nhật ký log phải được lưu trữ trên một máy chủ riêng biệt tách rời khỏi máy chủ ghi nhận sự kiện (để tránh tin tặc xóa dấu vết khi xâm nhập thành công).
  + Áp dụng cơ chế WORM (Write Once, Read Many) để chống sửa đổi nhật ký.
  + Đồng bộ thời gian chính xác trên toàn hệ thống bằng giao thức **NTP (Network Time Protocol)** để đối chiếu dòng thời gian sự kiện.
- **SIEM (Security Information and Event Management)**: Hệ thống thu thập, chuẩn hóa, tương quan hóa và phân tích tập trung hàng triệu log từ tường lửa, máy chủ, phần mềm diệt virus nhằm phát hiện mối đe dọa theo thời gian thực."""
            },
            {
                "heading": "2. Vòng đời dữ liệu và Chống thất thoát dữ liệu (DLP)",
                "content": """- **Vòng đời dữ liệu (Data Life Cycle)**:
  1. *Create (Tạo mới)*: Dữ liệu được sinh ra hoặc chỉnh sửa lần đầu.
  2. *Store (Lưu trữ)*: Ghi dữ liệu vào ổ đĩa, cơ sở dữ liệu. Cần mã hóa dữ liệu ở trạng thái nghỉ (**Data-at-Rest**).
  3. *Use (Sử dụng)*: Dữ liệu được nạp vào RAM máy tính để xử lý (**Data-in-Use**).
  4. *Share (Chia sẻ)*: Truyền dữ liệu giữa các bên qua mạng (**Data-in-Transit / Data-in-Motion**). Cần mã hóa bằng TLS/IPsec.
  5. *Archive (Lưu trữ lâu dài)*: Chuyển dữ liệu cũ sang kho lưu trữ dài hạn theo chính sách tuân thủ.
  6. *Destroy (Tiêu hủy)*: Hủy bỏ vĩnh viễn khi hết thời hạn lưu trữ.
- **DLP (Data Loss Prevention)**: Giải pháp theo dõi và ngăn chặn rò rỉ dữ liệu nhạy cảm (số thẻ tín dụng, CCCD, bí mật kinh doanh) ra bên ngoài qua email, USB hoặc tải lên mạng."""
            },
            {
                "heading": "3. Phân loại dữ liệu và Phương pháp tiêu hủy an toàn",
                "content": """- **Cấp độ phân loại trong doanh nghiệp thương mại**:
  + *Public (Công khai)*: Thông tin tiếp thị, thông cáo báo chí, không gây hại nếu lộ.
  + *Internal (Nội bộ)*: Sổ tay nhân viên, sơ đồ tổ chức, chỉ dùng trong công ty.
  + *Confidential (Bảo mật)*: Báo cáo tài chính, mã nguồn, kế hoạch kinh doanh.
  + *Restricted / Secret (Tuyệt mật)*: Dữ liệu PII khách hàng, thông tin thẻ tín dụng, sở hữu trí tuệ trọng yếu.
- **Phương pháp tiêu hủy dữ liệu (Data Sanitization)**:
  + *Clearing / Overwriting*: Ghi đè dữ liệu bằng chuỗi bit 0 và 1 (có thể tái sử dụng thiết bị).
  + *Purging / Degaussing (Khử từ)*: Dùng từ trường cực mạnh làm mất hoàn toàn từ tính của đĩa HDD và băng từ.
  + *Destruction (Phá hủy vật lý)*: Nghiền vụn (Shredding), đốt lò (Incineration), khoan đục đĩa cứng. Phương pháp an toàn tuyệt đối nhất."""
            },
            {
                "heading": "4. Mật mã học (Cryptography) & Chữ ký số",
                "content": """- **Hàm băm (Hashing)**: Thuật toán một chiều biến đổi dữ liệu có độ dài bất kỳ thành một chuỗi có độ dài cố định. Đảm bảo **Tính toàn vẹn (Integrity)**. Ví dụ: SHA-256, SHA-3. MD5 và SHA-1 đã bị phá vỡ vì lỗi va chạm (collision).
- **Mã hóa đối xứng (Symmetric Encryption)**: Dùng chung MỘT khóa bí mật duy nhất để cả mã hóa và giải mã. Tốc độ rất nhanh, bảo vệ **Tính bảo mật (Confidentiality)**. Thuật toán tiêu chuẩn: **AES (128, 192, 256-bit)**.
- **Mã hóa bất đối xứng (Asymmetric Encryption)**: Dùng một CẶP khóa gồm Khóa công khai (Public Key - chia sẻ cho mọi người) và Khóa bí mật (Private Key - chỉ chủ nhân giữ). Ví dụ: **RSA, ECC, Diffie-Hellman**.
- **Chữ ký số (Digital Signature)**:
  1. Người gửi tạo mã băm của bức thư.
  2. Người gửi mã hóa mã băm đó bằng **Khóa bí mật (Private Key) của chính mình**.
  3. Người nhận dùng **Khóa công khai (Public Key) của người gửi** để giải mã và kiểm tra mã băm.
  -> Đảm bảo đồng thời: **Tính toàn vẹn (Integrity)** + **Xác thực danh tính (Authentication)** + **Chống chối bỏ (Non-Repudiation)**."""
            },
            {
                "heading": "5. Quản lý Vận hành An toàn (Operational Management)",
                "content": """- **Change Management (Quản lý thay đổi)**: Quy trình kiểm soát mọi chỉnh sửa đối với phần mềm, phần cứng hoặc mạng nhằm giảm thiểu rủi ro gián đoạn. Bao gồm: Đề xuất thay đổi, đánh giá rủi ro của hội đồng CAB (Change Advisory Board), thử nghiệm, phê duyệt và lập kế hoạch quay lui (Rollback plan).
- **Configuration Management (Quản lý cấu hình)**: Thiết lập và duy trì các đường cơ sở bảo mật chuẩn (**Security Baselines**) cho máy trạm và máy chủ.
- **Patch Management (Quản lý vá lỗi)**: Quy trình rà soát, kiểm thử bản vá trong môi trường thử nghiệm (Test lab) trước khi cập nhật đồng loạt lên hệ thống sản xuất.
- **Security Awareness Training (Đào tạo nhận thức an ninh)**: Biện pháp phòng vệ thiết yếu nhất chống lại kỹ nghệ xã hội (Social Engineering) và thư lừa đảo (Phishing)."""
            }
        ]
    }
]

data["domain_summaries"] = domain_summaries

with open(data_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Enriched isc2_data.json with full 5-Domain Study Summaries & Exam Tips!")
