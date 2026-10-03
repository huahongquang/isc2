# ISC2 Certified in Cybersecurity (CC) - Study & Exam Simulator Platform 🛡️

Nền tảng học tập, tra cứu và luyện thi trắc nghiệm chứng chỉ quốc tế **(ISC)² Certified in Cybersecurity (CC)** được xây dựng và trích xuất trực tiếp từ cuốn sách giáo trình chuẩn:
> 📘 **Certified in Cybersecurity (CC) Exam Guide** *(Master core security concepts and pass the ISC2 Certified in Cybersecurity (CC) exam)*

---

## 🚀 Cách khởi động ứng dụng (Chỉ 1 Click)

### Cách 1: Chạy trực tiếp bằng file Batch (Khuyên dùng trên Windows)
- Nhấp đúp (Double-click) vào file **`run_app.bat`** trong thư mục `D:\Project\ISC2`.
- Ứng dụng sẽ tự động khởi động server cục bộ và tự động mở trình duyệt web tại địa chỉ `http://127.0.0.1:8080`.

### Cách 2: Chạy qua dòng lệnh Terminal / PowerShell
```powershell
cd D:\Project\ISC2
python app.py
```

---

## 🎯 Các tính năng trọng tâm của ứng dụng

### 1. 📊 Bảng điều khiển tiến độ (Dashboard)
- **Theo dõi tiến độ học tập**: Số câu hỏi đã làm trên tổng số 277 câu, tỷ lệ trả lời đúng (%), điểm đánh giá độ sẵn sàng thi (**Exam Readiness Score** theo chuẩn đỗ 70% của ISC2).
- **Thống kê chi tiết 5 Domain**:
  - **Domain 1**: Nguyên lý an toàn thông tin (*Security Principles* - Chiếm 26% đề thi, 49 câu hỏi)
  - **Domain 2**: Duy trì hoạt động, Khôi phục thảm họa & Phản ứng sự cố (*BC, DR & IR* - Chiếm 10% đề thi, 43 câu hỏi)
  - **Domain 3**: Khái niệm kiểm soát truy cập (*Access Control Concepts* - Chiếm 22% đề thi, 30 câu hỏi)
  - **Domain 4**: An toàn mạng (*Network Security* - Chiếm 24% đề thi, 124 câu hỏi)
  - **Domain 5**: Vận hành an ninh (*Security Operations* - Chiếm 18% đề thi, 31 câu hỏi)

### 2. 🎯 Luyện thi theo Domain (Domain-Focused Practice)
- Lọc câu hỏi theo từng Domain hoặc toàn bộ 277 câu.
- Chế độ làm bài: **Tuần tự** hoặc **Đảo ngẫu nhiên**.
- 4 phương án trắc nghiệm chuẩn chỉnh (A, B, C, D).
- **Phản hồi tức thì & Giải thích chi tiết**: Hiển thị đáp án đúng/sai ngay lập tức, kèm giải thích cặn kẽ và trích dẫn số trang cụ thể trong cuốn sách gốc.
- Đánh dấu sao (Bookmark) các câu hỏi khó để ôn tập lại sau.
- Hỗ trợ phím tắt: Bấm `1`, `2`, `3`, `4` để chọn đáp án; bấm mũi tên trái/phải để chuyển câu.

### 3. ⏱️ Thi thử mô phỏng đề thi thật (Full Mock Exam Simulator)
- **Chế độ thi chuẩn 100 câu / 120 phút**: Lấy ngẫu nhiên câu hỏi phân bổ đúng tỷ lệ trọng số của 5 Domain chuẩn kỳ thi ISC2 CC.
- Chế độ thi nhanh: 50 câu (60 phút) hoặc 25 câu (30 phút).
- Đồng hồ đếm ngược thời gian thực, bảng lưới 100 câu hỏi trực quan với các trạng thái: Đã chọn, Chưa làm, Gắn cờ xem lại (*Flag for Review*).
- **Báo cáo kết quả chi tiết**:
  - Đánh giá **ĐẠT (PASS)** hoặc **CHƯA ĐẠT (FAIL)** theo ngưỡng 70% chuẩn ISC2.
  - Pháo hoa chúc mừng nếu đạt điểm Pass!
  - Biểu đồ phân tích độ mạnh/yếu trên từng Domain giúp nhận biết chính xác phần kiến thức cần bổ sung.

### 4. 🗂️ Thẻ ghi nhớ thông minh 3D (Smart Flashcards)
- Thẻ lật 3 chiều (3D Flip Card) giúp rèn luyện trí nhớ theo phương pháp Spaced Repetition.
- Mặt trước: Câu hỏi thi / Thuật ngữ then chốt.
- Mặt sau: Đáp án chính xác, lời giải thích và số trang sách tham chiếu.
- Phân loại mức độ ghi nhớ: *Chưa thuộc (Phím 1)*, *Đang nhớ (Phím 2)*, *Đã thuộc (Phím 3)*.
- Bấm phím cách (`Space`) để lật thẻ cực nhanh.

### 5. 📖 Cẩm nang lý thuyết & 7 Bảng Cheat Sheets Kinh Điển
- Toàn bộ lý thuyết tóm tắt chắt lọc của cả 5 Domain kèm các **Mẹo thi cốt lõi (Exam Tips)**.
- **7 Bảng tra cứu Cheat Sheets quan trọng nhất**:
  1. *Mapping Attacks to the CIA Triad* (Ánh xạ các cuộc tấn công vào CIA & DAD)
  2. *Security Controls Matrix* (Ma trận kiểm soát: Vật lý / Kỹ thuật / Quản trị x Ngăn chặn / Phát hiện / Khắc phục)
  3. *Disaster Recovery Site Types* (So sánh Hot Site, Warm Site, Cold Site, Mobile Site)
  4. *Access Control Models* (So sánh DAC, MAC, RBAC, RuBAC, ABAC)
  5. *OSI 7 Layers vs TCP/IP Model & Protocols* (Mô hình mạng và giao thức)
  6. *Well-Known Ports & Services* (Bảng cổng mạng: FTP 20/21, SSH 22, Telnet 23, DNS 53, HTTP 80, HTTPS 443, RDP 3389...)
  7. *Cryptography Essentials* (So sánh Mã hóa đối xứng AES vs Bất đối xứng RSA vs Hàm băm SHA-256)
- **4 Canons Đạo đức ISC2** bắt buộc phải thuộc lòng thứ tự ưu tiên khi đi thi.

### 6. 📑 Từ điển thuật ngữ & Viết tắt (Cybersecurity Glossary & Acronyms)
- Hơn 40+ thuật ngữ và từ viết tắt quan trọng nhất trong kỳ thi (CIA, DAD, BIA, RTO, RPO, MTD, DAC, MAC, RBAC, ABAC, MFA, IDS/IPS, SIEM, DLP, AES, RSA, PKI...).
- Thanh tìm kiếm tức thì theo từ khóa tiếng Anh hoặc tiếng Việt.

### 7. ❌ Ôn tập câu sai & Đã lưu (Mistakes & Bookmarks Review)
- Hệ thống tự động ghi nhớ các câu hỏi bạn từng làm sai.
- Chế độ luyện tập riêng cho danh sách câu sai để biến điểm yếu thành điểm mạnh trước ngày thi chính thức.

### 8. 📕 Tích hợp trực tiếp Sách gốc PDF
- Nút "Mở PDF" trên thanh menu cho phép mở trực tiếp file `Certified in Cybersecurity (CC) Exam Guide.pdf` ngay trên trình duyệt để đối chiếu nội dung gốc bất kỳ lúc nào.

---

## 📁 Cấu trúc thư mục dự án

```
D:\Project\ISC2\
│
├── Certified in Cybersecurity (CC) Exam Guide.pdf   # Sách giáo trình gốc (Packt Publishing)
├── app.py                                            # Web server nhẹ (Python HTTP Server & REST API)
├── run_app.bat                                       # File khởi chạy 1-click cho Windows
├── index.html                                        # Giao diện ứng dụng Single Page App hiện đại
├── isc2_data.json                                    # Cơ sở dữ liệu 277 câu hỏi, 5 Domain, 7 Cheat Sheets, Glossary
├── extract_data.py                                   # Script trích xuất và xử lý dữ liệu từ PDF
├── enrich_content.py                                 # Script bổ sung lý thuyết & cẩm nang 5 Domain
└── README.md                                         # Tài liệu hướng dẫn sử dụng chi tiết
```

---

## 💡 Lời khuyên ôn thi từ cuốn sách (Exam Preparation Strategy)

1. **Hiểu bản chất thay vì học vẹt**: Đề thi ISC2 CC là đề thi mang tính áp dụng tình huống thực tế (Scenario-based). Hãy luôn đặt câu hỏi *"Mục tiêu an ninh ở đây là gì?"*.
2. **Quy tắc vàng**: An toàn tính mạng con người (**Human Life Safety**) luôn là ưu tiên cao nhất trong mọi tình huống BCP, DRP và an ninh vật lý.
3. **Mục tiêu đạt điểm**: Hãy luyện các bộ câu hỏi và thi thử cho đến khi đạt điểm trung bình **trên 85%** trước khi bước vào phòng thi thật (kỳ thi thật yêu cầu 70%).
