# 🌀 Mô phỏng chuyển động tròn biến đổi đều bằng Python

Đây là một chương trình Python sử dụng thư viện **NumPy** và **Matplotlib** để mô phỏng **chuyển động tròn biến đổi đều** – một dạng chuyển động trong đó tốc độ góc thay đổi đều theo thời gian.

---

## 📋 Mô tả

Chương trình vẽ và hiển thị hoạt ảnh một chất điểm chuyển động trên một đường tròn với các thông số như bán kính, tốc độ góc ban đầu và gia tốc góc. Quỹ đạo được vẽ sẵn, và chất điểm di chuyển trên đó theo thời gian. Đồng thời, chương trình cũng hiển thị **tốc độ tức thời** của chất điểm tại mỗi thời điểm.

---

## 🧠 Kiến thức vật lý liên quan

- **Phương trình góc quay**:  
  \[
  \theta(t) = \omega_0 t + \frac{1}{2} \beta t^2
  \]

- **Vị trí chất điểm**:  
  \[
  x(t) = R \cos(\theta(t)), \quad y(t) = R \sin(\theta(t))
  \]

- **Tốc độ tức thời**:  
  \[
  v(t) = R (\omega_0 + \beta t)
  \]

---

## 🛠 Cách chạy chương trình

### 1. Cài đặt thư viện cần thiết

```bash
pip install matplotlib numpy
