Cài đặt `LRUCache(capacity)`. `get(key)` trả về giá trị hoặc -1 nếu không có khóa. `put(key, value)` thêm hoặc cập nhật khóa. Một lần đọc thành công hay ghi đều làm khóa trở thành khóa dùng gần nhất. Nếu thêm vượt dung lượng, loại khóa lâu nhất chưa được dùng. Mỗi thao tác cần trung bình O(1).

## Ví dụ

```text
Sức chứa 2: put(1, 10), put(2, 20), get(1) → 10, put(3, 30), get(2) → -1.
```
