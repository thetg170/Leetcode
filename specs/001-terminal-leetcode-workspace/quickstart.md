# Quickstart — Kiểm tra MVP

## Chuẩn bị

Dùng checkout có các file dự án và một bản cài Git, tmux, Neovim và uv. Từ thư mục repo chạy:

```sh
./tools/bootstrap-lc.sh
lc doctor
```

Trên máy đã có đủ gói trong cache, thêm `--offline` vào lệnh bootstrap để kiểm tra thiết lập offline.

## Mở và đổi bài

1. Từ ngoài repo, chạy `lc` và chọn Two Sum. Xác nhận đề hiện bên trái và file `solution.py` mở trong Neovim bên phải.
2. Thêm một dòng vào editor và giữ buffer chưa lưu. Từ terminal khác chạy `lc lang vi` rồi `lc lang en`. Xác nhận nội dung đề đổi và dòng mới vẫn còn.
3. Dùng picker trong Neovim hoặc `lc open <problem>` để đổi sang bài khác rồi quay lại Two Sum. Xác nhận buffer giữ dòng đang sửa. Detach tmux rồi chạy `lc resume` để kiểm tra phiên editor được giữ.
4. Chọn một bài thiếu bản VI. Chuyển sang VI và xác nhận phần đề ghi rõ fallback. Thu hẹp terminal và thử zoom rồi đổi pane bằng phím tmux hiện tại.

## Kiểm tra lời giải

Viết và lưu lời giải Two Sum, rồi chạy:

```sh
lc run 1
lc test 1
```

Run hiển thị dữ liệu vào, kết quả mong đợi và kết quả thực tế. Test kiểm tra các ca pytest có sẵn. Thử phím tắt Test từ editor để xác nhận phiên bản đang sửa được lưu trước khi chạy.

Trong checkout thử nghiệm, lần lượt thử đáp án sai, lỗi khi thực thi và vòng lặp vượt quá `--timeout 1`. Thử `lc test` cho một bài thiếu test. Xác nhận mỗi trường hợp có thông báo và mã thoát riêng cho thành công hoặc thất bại.

## Kiểm tra dữ liệu và đồng bộ

```sh
lc mark need-review 1
lc note "Xem lại cách dùng hash map." 1
lc status 1
```

Xác nhận tiến độ và ghi chú nằm trong các file có thể kiểm tra bằng Git. Thử bootstrap từ một checkout cục bộ khác có dấu cách trong đường dẫn. Dùng repo thử nghiệm để kiểm tra `lc sync` với editor đang mở, thay đổi chưa commit, xung đột, nhánh bị lệch và một lần pull fast-forward thành công.
