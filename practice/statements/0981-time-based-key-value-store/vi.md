Lưu nhiều giá trị theo thời điểm cho cùng một khóa. Thời điểm của mỗi lần set lớn hơn thời điểm của lần set trước. Hàm get lấy giá trị của khóa tại thời điểm muộn nhất không vượt quá thời điểm truy vấn. Nếu không tìm thấy, trả về chuỗi rỗng.

## Ví dụ

```text
set('k', 'old', 2), set('k', 'new', 5), get('k', 4) → 'old'
```
