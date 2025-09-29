# 🎮 Tic Tac Toe với Python & Adversarial Search

## 📌 Giới thiệu
Dự án này triển khai trò chơi **Tic Tac Toe (3×3)** bằng **Python**, trong đó máy tính sử dụng các **thuật toán tìm kiếm có đối thủ** như:

- **Minimax**
- **Alpha-Beta Pruning**
- (tùy chọn) **Monte Carlo Tree Search (MCTS)**

Dự án phù hợp cho việc học:
- biểu diễn trạng thái trò chơi bằng `numpy`.
- cài đặt và tối ưu thuật toán tìm kiếm.
- viết hàm đánh giá (evaluation function).
- mở rộng sang các trò chơi khác.

---

## 🏗️ Cấu trúc project
```

tic_tac_toe/
├─ README.md
├─ requirements.txt
├─ src/
│  ├─ game.py          # logic cốt lõi: trạng thái, luật, kiểm tra thắng
│  ├─ ai_minimax.py    # Minimax + Alpha-Beta pruning
│  ├─ ai_mcts.py       # (tùy chọn) MCTS
│  ├─ ui_tk.py         # (tùy chọn) giao diện tkinter
│  └─ main.py          # chạy trò chơi (CLI hoặc GUI)
└─ tests/
├─ test_game.py
└─ test_ai.py

````

---

## ⚙️ Cài đặt
Yêu cầu:
- Python >= 3.8
- Các thư viện:
```bash
  pip install numpy
```

(có thể mở rộng thêm `pygame`, `tkinter`, hoặc `numba` nếu muốn)

---

## 🚀 Cách chạy

### Chạy trên terminal (CLI)

```bash
python src/main.py
```

Người chơi nhập tọa độ (hàng, cột) để đánh, máy tính sẽ phản hồi bằng Minimax/Alpha-Beta.

### Chạy với giao diện (nếu bật `ui_tk.py`)

```bash
python src/ui_tk.py
```

---

## 🧠 Thuật toán tìm kiếm

### Minimax

* Duyệt toàn bộ cây trạng thái.
* Giả định đối thủ chơi tối ưu.
* Với Tic Tac Toe (cây nhỏ), Minimax chơi hoàn hảo.

### Alpha-Beta Pruning

* Cắt tỉa nhánh không cần thiết trong Minimax.
* Tăng tốc độ tính toán, đặc biệt quan trọng với trò chơi lớn hơn.

### Hàm đánh giá (Heuristic)

* Nếu xét toàn bộ cây: chỉ cần `+10` cho thắng, `-10` cho thua, `0` cho hòa.
* Nếu cắt ở độ sâu giới hạn: dùng heuristic như:

  * +3 nếu có 2 quân X + 1 ô trống.
  * -3 nếu có 2 quân O + 1 ô trống.
  * +1 / -1 cho các khả năng thắng tiềm năng.

---

## 📚 Mở rộng

* Thêm **MCTS** để xử lý trò chơi phức tạp hơn.
* Dùng **numba** để tăng tốc Minimax.
* Xây dựng giao diện **pygame** hoặc web với **Flask**.
* Mở rộng luật sang **Caro 5-in-a-row**.

