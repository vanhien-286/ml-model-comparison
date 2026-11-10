# 📊 Phân Loại Email Spam Bằng Machine Learning

Dự án nghiên cứu và so sánh hiệu năng của các thuật toán Học máy (Machine Learning) trong bài toán phân loại tin nhắn/email rác (Spam).

---

## 📌 Giới Thiệu

Đồ án thực hiện so sánh 3 thuật toán phổ biến:

- **Naive Bayes** (MultinomialNB)
- **Decision Tree** (Cây quyết định)
- **Random Forest** (Rừng ngẫu nhiên)

Tập dữ liệu được tiền xử lý và trích xuất đặc trưng bằng kỹ thuật **TF-IDF**.

---

## 📂 Cấu Trúc Thư Mục

ml-model-comparison/
├── Data/
│ └── spam.csv # Tập dữ liệu tin nhắn SMS/Email
├── bd.py # File vẽ biểu đồ trực quan hóa dữ liệu
├── decision_tree.py # Code huấn luyện mô hình Decision Tree
├── naive_bayes.py # Code huấn luyện mô hình Naive Bayes
├── random_forest.py # Code huấn luyện mô hình Random Forest
├── read.py # File đọc và xem dữ liệu
└── README.md # Tài liệu hướng dẫn

```

---

## 📊 Kết Quả Thực Nghiệm

| Mô hình | Accuracy (Độ chính xác) | Precision (Spam) | Recall (Spam) | F1-Score (Spam) |
| :--- | :---: | :---: | :---: | :---: |
| **Random Forest** | **97.67%** | **100%** | **83%** | **0.90** |
| **Naive Bayes** | 96.68% | 100% | 75% | 0.86 |
| **Decision Tree** | 95.34% | 90% | 73% | 0.81 |

👉 **Kết luận:** **Random Forest** cho kết quả tối ưu nhất với độ chính xác cao và tránh hoàn toàn việc nhận diện nhầm thư thường thành thư rác (Precision 100%).

---

## 🛠️ Cài Đặt & Chạy Dự Án

### 1. Cài đặt các thư viện cần thiết

Mở Terminal/CMD và chạy lệnh:

pip install pandas scikit-learn nltk matplotlib seaborn wordcloud

### 2. Chạy thử các mô hình

Bạn có thể chạy riêng từng file tùy theo mô hình muốn kiểm thử:

- **Chạy mô hình Random Forest:**

  python random_forest.py

- **Chạy mô hình Naive Bayes:**


  python naive_bayes.py

- **Chạy mô hình Decision Tree:**

  python decision_tree.py


- **Xem biểu đồ phân tích dữ liệu:**

  python bd.py

---

```
