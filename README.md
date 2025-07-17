# GEC-Vietnamese: Vietnamese Grammatical Error Correction

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

---

### Overview
GEC-Vietnamese is an open-source toolkit for Vietnamese Grammatical Error Correction (GEC). It provides pre-trained models, data generation scripts, and a user-friendly web interface for correcting Vietnamese sentences.

### Features
- Pre-trained models for Vietnamese GEC
- Synthetic error data generation
- Gradio-based web interface
- Example notebooks for training and evaluation

### Directory Structure
```
GEC-Vietnamese/
│
├── notebooks/              # Example, training, and testing notebooks
├── data/                   # Sample and synthetic data
├── models/                 # Trained models/checkpoints
├── requirements.txt        # Required libraries
├── main.py                 # Gradio web demo
├── generate.py             # Synthetic data generation script
├── CHANGELOG.md            # Project changelog
├── README.md               # Usage guide
├── .gitignore              # Git ignore rules
└── LICENSE                 # License
```

### Installation
```bash
pip install -r requirements.txt
```

### Usage

#### 1. Grammatical Error Correction (Web UI)
```bash
python main.py
```
- A Gradio web interface will open in your browser.
- Enter Vietnamese sentences and click "Correct".

**Example:**
- Input: `Toi di hoc ve nha.`
- Output: `Tôi đi học về nhà.`

#### 2. Synthetic Data Generation
```bash
python generate.py --input_file data/sample.xlsx --output_file data/synthetic_output.xlsx
```
- Adjust `generate.py` if your data format differs.

### Contribution
Contributions are welcome! Please open an issue or pull request. See `CONTRIBUTING.md` for guidelines.

### Changelog
See [CHANGELOG.md](CHANGELOG.md) for project history.

### Contact
- Name: Lam Nguyen (CognmaL)
- Email: 21280096@student.hcmus.edu.vn

---

### Giới thiệu
GEC-Vietnamese là bộ công cụ mã nguồn mở cho nhiệm vụ sửa lỗi ngữ pháp tiếng Việt. Dự án cung cấp mô hình huấn luyện sẵn, script sinh dữ liệu lỗi, và giao diện web thân thiện cho người dùng.

### Tính năng
- Mô hình sửa lỗi ngữ pháp tiếng Việt
- Sinh dữ liệu lỗi tổng hợp
- Giao diện web Gradio dễ sử dụng
- Notebook ví dụ huấn luyện và kiểm thử

### Cấu trúc thư mục
```
GEC-Vietnamese/
│
├── notebooks/              # Notebook ví dụ, huấn luyện, kiểm thử
├── data/                   # Dữ liệu mẫu và dữ liệu tổng hợp
├── models/                 # Mô hình/checkpoint đã huấn luyện
├── requirements.txt        # Thư viện cần thiết
├── main.py                 # Demo web Gradio
├── generate.py             # Script sinh dữ liệu lỗi
├── CHANGELOG.md            # Lịch sử thay đổi
├── README.md               # Hướng dẫn sử dụng
├── .gitignore              # Quy tắc bỏ qua file khi commit
└── LICENSE                 # Giấy phép sử dụng
```

### Cài đặt
```bash
pip install -r requirements.txt
```

### Sử dụng

#### 1. Sửa lỗi ngữ pháp (Giao diện web)
```bash
python main.py
```
- Giao diện Gradio sẽ mở trên trình duyệt.
- Nhập câu tiếng Việt và nhấn "Correct".

**Ví dụ:**
- Đầu vào: `Toi di hoc ve nha.`
- Đầu ra: `Tôi đi học về nhà.`

#### 2. Sinh dữ liệu lỗi tổng hợp
```bash
python generate.py --input_file data/sample.xlsx --output_file data/synthetic_output.xlsx
```
- Có thể cần chỉnh sửa `generate.py` nếu định dạng dữ liệu khác.

### Đóng góp
Mọi đóng góp đều được hoan nghênh! Vui lòng tạo issue hoặc pull request. Xem thêm hướng dẫn ở `CONTRIBUTING.md`.

### Lịch sử thay đổi
Xem [CHANGELOG.md](CHANGELOG.md) để biết lịch sử dự án.

### Liên hệ
- Tên: Lam Nguyen (CognmaL)
- Email: 21280096@student.hcmus.edu.vn

---

