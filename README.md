# Leetcode

Kho lời giải LeetCode và workflow luyện thuật toán + Vim motion trong 30 phút mỗi ngày.
Các file lời giải do LeetHub tạo vẫn được giữ nguyên; phần luyện tập chỉ bổ sung metadata,
test và scratch file bị Git bỏ qua.

## Workspace trong terminal

`lc` mở trình chọn bài. tmux hiển thị đề ở bên trái và Neovim mở lời giải
ở bên phải. Terminal hẹp có thể dùng bố cục trên/dưới. Kho lời giải LeetHub
và workflow `kata.py` bên dưới vẫn dùng được. Workspace tạo `solution.py` hoặc
`solution.sql` riêng khi bạn mở một bài lần đầu.

### Cài đặt và mở bài

Cần Git, uv, tmux và Neovim. Bootstrap chuẩn bị môi trường Python theo `uv.lock`
và tạo liên kết `~/.local/bin/lc`. Shell trong dotfiles hiện tại đã có thư mục này
trong PATH. Nếu có fzf, trình chọn hỗ trợ fuzzy search, nếu thiếu thì chọn bằng số.

```sh
./tools/bootstrap-lc.sh
lc doctor
lc                      # Tìm và chọn Two Sum
```

Bạn cũng có thể dùng `lc list`, `lc search two-sum` hoặc `lc open 1`.
Nếu một ID trùng, truyền tên thư mục đầy đủ. Dùng `lc resume` để vào lại
phiên đã detach. Khi bạn đổi bài, Neovim giữ các buffer chưa lưu trong phiên.
Dùng `:wall` để ghi mọi buffer trước khi thoát hoặc chuyển máy.

Trong editor bên phải, bấm `Space l h` để tra cách lưu, chạy test và thoát.
Bấm `Space l s` để xem lời giải tham khảo local của bài đang mở. Phần xem
mở riêng và giữ nguyên bản nháp. Dùng `q` hoặc `Esc` để quay lại.
[Bảng phím tắt workspace](practice/workspace-shortcuts.md)

Cả 150 bài trong deck NeetCode 150 có lời giải tham khảo local. Với 107 bài
được bổ sung, `reference.py` chứa lời giải để xem, còn `starter.py` tạo bản
nháp mới. Các lời giải mới dựa trên mã Python của NeetCode, điều chỉnh để dùng
với workspace. [Bản nguồn đã dùng](https://github.com/neetcode-gh/leetcode/tree/8fed5f7daa6a517e375a0562d876e4a72dfdafb8/python)
· [Giấy phép MIT](practice/neetcode-reference-LICENSE.txt)

### Đề bài và kiểm thử offline

`lc lang vi` và `lc lang en` đổi đề từ terminal. Trong Neovim của workspace,
bấm `Space l l` để đổi qua lại. Cả 150 bài NeetCode có đề tiếng Anh và bản
tóm tắt tiếng Việt dùng offline. Khi bài ngoài bộ này thiếu một ngôn ngữ,
workspace hiển thị bản thay thế và ghi rõ ngôn ngữ. Thêm bản diễn giải của bạn
tại `practice/statements/<tên-thư-mục>/vi.md`
hoặc `en.md`. Chỉ chia sẻ nội dung bạn có quyền đưa lên GitHub.

```sh
lc run 1                  # Input, Expected, Actual từ ví dụ Two Sum
lc test 1 --timeout 10    # Chạy bộ test Python hiện có cho bài 1
lc mark solved 1
lc note "Ôn lại cách dùng hash map" 1
lc status
```

`run` cần một ví dụ JSON trong `practice/examples/`. Two Sum có ví dụ sẵn.
`test` dùng pytest ở thư mục bài và báo khi thiếu test. SQL hỗ trợ đọc đề và sửa
lời giải. Các kết quả chạy local tách biệt với trạng thái học và Accepted trên
LeetCode. Dùng `lc mark --help` để xem bốn trạng thái học.

### Ôn bài theo thẻ Anki

Tạo thẻ cho bài muốn ôn. Đặt tên bài, một câu hỏi gợi nhớ và lệnh mở bài ở mặt
trước. Đặt ý tưởng giải, lỗi dễ mắc hoặc độ phức tạp ở mặt sau. Ví dụ thẻ Two Sum
có câu hỏi “Bạn cần lưu gì khi duyệt mảng?” và lệnh:

```sh
lc review 0001-two-sum
```

Khi thẻ đến hạn, chạy lệnh ở bất kỳ thư mục nào. Workspace mở đề và một
`solution.py` nháp với chữ ký hàm nếu có. Viết lại lời giải, dùng
`Space l r` để chạy ví dụ hoặc `Space l t` để chạy test, rồi quay về Anki lật thẻ
và tự chấm. Ở terminal khác, `lc test` chạy file đang mở, còn `lc test 0001-two-sum`
chạy lời giải chính của bài.

Mỗi lần gọi `lc review` tạo một nháp Python mới. Bản nháp cũ nằm trong
`practice/.lc/reviews/` và chỉ lưu trên máy đã làm. Dùng `lc resume` để quay
lại workspace đang giữ bài làm dở. `lc open 0001-two-sum` mở lời giải chính.
Trên Mac thứ hai, lệnh trong thẻ vẫn dùng được sau khi thiết lập workspace.
Anki quản lý ngày đến hạn và điểm ôn.

Deck **LeetCode** trên Anki có lệnh `lc review` cho đủ 150 bài NeetCode 150.
107 bài bổ sung có một ví dụ và khung hàm Python. Cả 150 bài có đề song ngữ
offline và bộ test local. Trong
Neovim, bấm `Space l t` để lưu và kiểm tra bản nháp đang mở. Kết quả dựa
trên các ca kiểm thử trong repo. Dùng liên kết LeetCode khi muốn nộp bài
trên hệ thống chấm trực tuyến.

### Đồng bộ hai máy

1. Lưu các buffer cần chia sẻ bằng `:wall`, rồi xem `git status` và `git diff`.
   Chỉ stage các đường dẫn đã xem. Lời giải luyện nằm ở `solution.py` hoặc
   `solution.sql`, ghi chú ở `notes.md`, tiến độ ở `practice/progress/`.
   Lần đồng bộ đầu cần xem và đưa cả mã workspace, bộ test và metadata mong muốn
   vào Git. Thư mục `practice/.lc/`, môi trường ảo và scratch kata là dữ liệu cục bộ.
2. Commit các thay đổi đã chọn, rồi chạy `git push` thủ công. Nếu Git từ chối
   do nhánh từ xa đi trước, fetch và xử lý phần chênh lệch trước khi push lại.
3. Trên Mac thứ hai, clone repo từ remote GitHub của bạn vào đường dẫn bất kỳ,
   vào thư mục repo rồi chạy `./tools/bootstrap-lc.sh` và `lc doctor`.
   Nếu `lc` đã trỏ sang một checkout khác, bootstrap báo rõ và giữ liên kết đó.
   Dùng `./bin/lc` để chạy trực tiếp từ checkout mới.
4. Để lấy thay đổi sau này, lưu và thoát editor workspace bằng `:qa` rồi chạy
   `lc sync` khi cây làm việc sạch. Lệnh chỉ pull fast-forward. Với conflict
   hoặc lịch sử đã phân kỳ, xem `git status` và xử lý trong Git trước khi chạy lại.

Nếu không thấy `lc`, kiểm tra `~/.local/bin` trong PATH hoặc chạy `./bin/lc`.
Bootstrap lần đầu cần tải các gói chưa có trong cache. Nếu đã có cache, dùng
`./tools/bootstrap-lc.sh --offline`. Các thao tác luyện bài sau bootstrap chạy local.

## Bắt đầu nhanh

```sh
uv sync --dev
uv run python tools/kata.py next
uv run python tools/kata.py start 0001-two-sum
uv run python tools/kata.py test --path 0001-two-sum/kata.py
uv run python tools/kata.py finish --grade good --motion gsa --motion dap --note "ôn lại hash map"
uv run python tools/kata.py report
```

- `next`: lấy bài core đang đến hạn theo ladder 1, 3, 7, 14, 30, 60 ngày.
- `start`: tạo `kata.py` trống từ signature của lời giải; thêm `--mode repair` để tạo
  `buggy.py` có một lỗi so sánh cần tìm và sửa.
- `resume`: mở lại scratch và giữ nguyên bộ đếm của session đang làm dở.
- `test`: chạy test của bài hiện tại và ghi số lần chạy/sai vào session.
- `finish`: chấm `again`, `hard`, `good` hoặc `easy`, cập nhật metadata và lịch ôn.
- `report --write`: tạo dashboard `practice/dashboard.md` từ lịch sử session.

Trong Neovim, dùng nhóm `<leader>k`: `kn` bắt đầu bài kế tiếp, `kp` chọn bài,
`kr` chạy test, `kf` kết thúc/chấm bài và `kd` xem tiến độ. Xem
[`practice/schema.md`](practice/schema.md) để biết schema metadata và quy tắc ôn.

Nếu scratch đã tồn tại, Neovim cho phép tiếp tục file cũ, ghi đè bằng một stub trống,
hoặc hủy thao tác. Restart không lưu archive của scratch.

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/MarkPhamm/Leetcode/tree/master/0001-two-sum) |
| [0004-median-of-two-sorted-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/0004-median-of-two-sorted-arrays) |
| [0011-container-with-most-water](https://github.com/MarkPhamm/Leetcode/tree/master/0011-container-with-most-water) |
| [0014-longest-common-prefix](https://github.com/MarkPhamm/Leetcode/tree/master/0014-longest-common-prefix) |
| [0015-3sum](https://github.com/MarkPhamm/Leetcode/tree/master/0015-3sum) |
| [0018-4sum](https://github.com/MarkPhamm/Leetcode/tree/master/0018-4sum) |
| [0026-remove-duplicates-from-sorted-array](https://github.com/MarkPhamm/Leetcode/tree/master/0026-remove-duplicates-from-sorted-array) |
| [0027-remove-element](https://github.com/MarkPhamm/Leetcode/tree/master/0027-remove-element) |
| [0035-search-insert-position](https://github.com/MarkPhamm/Leetcode/tree/master/0035-search-insert-position) |
| [0039-combination-sum](https://github.com/MarkPhamm/Leetcode/tree/master/0039-combination-sum) |
| [0042-trapping-rain-water](https://github.com/MarkPhamm/Leetcode/tree/master/0042-trapping-rain-water) |
| [0049-group-anagrams](https://github.com/MarkPhamm/Leetcode/tree/master/0049-group-anagrams) |
| [0053-maximum-subarray](https://github.com/MarkPhamm/Leetcode/tree/master/0053-maximum-subarray) |
| [0056-merge-intervals](https://github.com/MarkPhamm/Leetcode/tree/master/0056-merge-intervals) |
| [0066-plus-one](https://github.com/MarkPhamm/Leetcode/tree/master/0066-plus-one) |
| [0074-search-a-2d-matrix](https://github.com/MarkPhamm/Leetcode/tree/master/0074-search-a-2d-matrix) |
| [0078-subsets](https://github.com/MarkPhamm/Leetcode/tree/master/0078-subsets) |
| [0080-remove-duplicates-from-sorted-array-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0080-remove-duplicates-from-sorted-array-ii) |
| [0088-merge-sorted-array](https://github.com/MarkPhamm/Leetcode/tree/master/0088-merge-sorted-array) |
| [0090-subsets-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0090-subsets-ii) |
| [0118-pascals-triangle](https://github.com/MarkPhamm/Leetcode/tree/master/0118-pascals-triangle) |
| [0119-pascals-triangle-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0119-pascals-triangle-ii) |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/MarkPhamm/Leetcode/tree/master/0121-best-time-to-buy-and-sell-stock) |
| [0128-longest-consecutive-sequence](https://github.com/MarkPhamm/Leetcode/tree/master/0128-longest-consecutive-sequence) |
| [0136-single-number](https://github.com/MarkPhamm/Leetcode/tree/master/0136-single-number) |
| [0162-find-peak-element](https://github.com/MarkPhamm/Leetcode/tree/master/0162-find-peak-element) |
| [0167-two-sum-ii-input-array-is-sorted](https://github.com/MarkPhamm/Leetcode/tree/master/0167-two-sum-ii-input-array-is-sorted) |
| [0169-majority-element](https://github.com/MarkPhamm/Leetcode/tree/master/0169-majority-element) |
| [0170-two-sum-iii-data-structure-design](https://github.com/MarkPhamm/Leetcode/tree/master/0170-two-sum-iii-data-structure-design) |
| [0209-minimum-size-subarray-sum](https://github.com/MarkPhamm/Leetcode/tree/master/0209-minimum-size-subarray-sum) |
| [0216-combination-sum-iii](https://github.com/MarkPhamm/Leetcode/tree/master/0216-combination-sum-iii) |
| [0217-contains-duplicate](https://github.com/MarkPhamm/Leetcode/tree/master/0217-contains-duplicate) |
| [0219-contains-duplicate-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0219-contains-duplicate-ii) |
| [0228-summary-ranges](https://github.com/MarkPhamm/Leetcode/tree/master/0228-summary-ranges) |
| [0238-product-of-array-except-self](https://github.com/MarkPhamm/Leetcode/tree/master/0238-product-of-array-except-self) |
| [0252-meeting-rooms](https://github.com/MarkPhamm/Leetcode/tree/master/0252-meeting-rooms) |
| [0259-3sum-smaller](https://github.com/MarkPhamm/Leetcode/tree/master/0259-3sum-smaller) |
| [0283-move-zeroes](https://github.com/MarkPhamm/Leetcode/tree/master/0283-move-zeroes) |
| [0303-range-sum-query-immutable](https://github.com/MarkPhamm/Leetcode/tree/master/0303-range-sum-query-immutable) |
| [0325-maximum-size-subarray-sum-equals-k](https://github.com/MarkPhamm/Leetcode/tree/master/0325-maximum-size-subarray-sum-equals-k) |
| [0346-moving-average-from-data-stream](https://github.com/MarkPhamm/Leetcode/tree/master/0346-moving-average-from-data-stream) |
| [0347-top-k-frequent-elements](https://github.com/MarkPhamm/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [0349-intersection-of-two-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/0349-intersection-of-two-arrays) |
| [0350-intersection-of-two-arrays-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0350-intersection-of-two-arrays-ii) |
| [0414-third-maximum-number](https://github.com/MarkPhamm/Leetcode/tree/master/0414-third-maximum-number) |
| [0485-max-consecutive-ones](https://github.com/MarkPhamm/Leetcode/tree/master/0485-max-consecutive-ones) |
| [0496-next-greater-element-i](https://github.com/MarkPhamm/Leetcode/tree/master/0496-next-greater-element-i) |
| [0560-subarray-sum-equals-k](https://github.com/MarkPhamm/Leetcode/tree/master/0560-subarray-sum-equals-k) |
| [0605-can-place-flowers](https://github.com/MarkPhamm/Leetcode/tree/master/0605-can-place-flowers) |
| [0628-maximum-product-of-three-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0628-maximum-product-of-three-numbers) |
| [0645-set-mismatch](https://github.com/MarkPhamm/Leetcode/tree/master/0645-set-mismatch) |
| [0682-baseball-game](https://github.com/MarkPhamm/Leetcode/tree/master/0682-baseball-game) |
| [0724-find-pivot-index](https://github.com/MarkPhamm/Leetcode/tree/master/0724-find-pivot-index) |
| [0735-asteroid-collision](https://github.com/MarkPhamm/Leetcode/tree/master/0735-asteroid-collision) |
| [0746-min-cost-climbing-stairs](https://github.com/MarkPhamm/Leetcode/tree/master/0746-min-cost-climbing-stairs) |
| [0748-largest-number-at-least-twice-of-others](https://github.com/MarkPhamm/Leetcode/tree/master/0748-largest-number-at-least-twice-of-others) |
| [0792-binary-search](https://github.com/MarkPhamm/Leetcode/tree/master/0792-binary-search) |
| [0888-fair-candy-swap](https://github.com/MarkPhamm/Leetcode/tree/master/0888-fair-candy-swap) |
| [0907-koko-eating-bananas](https://github.com/MarkPhamm/Leetcode/tree/master/0907-koko-eating-bananas) |
| [0987-reveal-cards-in-increasing-order](https://github.com/MarkPhamm/Leetcode/tree/master/0987-reveal-cards-in-increasing-order) |
| [1019-squares-of-a-sorted-array](https://github.com/MarkPhamm/Leetcode/tree/master/1019-squares-of-a-sorted-array) |
| [1044-find-common-characters](https://github.com/MarkPhamm/Leetcode/tree/master/1044-find-common-characters) |
| [1066-fixed-point](https://github.com/MarkPhamm/Leetcode/tree/master/1066-fixed-point) |
| [1083-two-sum-less-than-k](https://github.com/MarkPhamm/Leetcode/tree/master/1083-two-sum-less-than-k) |
| [1098-largest-unique-number](https://github.com/MarkPhamm/Leetcode/tree/master/1098-largest-unique-number) |
| [1102-check-if-a-number-is-majority-element-in-a-sorted-array](https://github.com/MarkPhamm/Leetcode/tree/master/1102-check-if-a-number-is-majority-element-in-a-sorted-array) |
| [1149-intersection-of-three-sorted-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/1149-intersection-of-three-sorted-arrays) |
| [1241-decompress-run-length-encoded-list](https://github.com/MarkPhamm/Leetcode/tree/master/1241-decompress-run-length-encoded-list) |
| [1256-rank-transform-of-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/1256-rank-transform-of-an-array) |
| [1304-find-n-unique-integers-sum-up-to-zero](https://github.com/MarkPhamm/Leetcode/tree/master/1304-find-n-unique-integers-sum-up-to-zero) |
| [1306-minimum-absolute-difference](https://github.com/MarkPhamm/Leetcode/tree/master/1306-minimum-absolute-difference) |
| [1345-perform-string-shifts](https://github.com/MarkPhamm/Leetcode/tree/master/1345-perform-string-shifts) |
| [1391-counting-elements](https://github.com/MarkPhamm/Leetcode/tree/master/1391-counting-elements) |
| [1392-find-the-difference-of-two-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/1392-find-the-difference-of-two-arrays) |
| [1407-group-the-people-given-the-group-size-they-belong-to](https://github.com/MarkPhamm/Leetcode/tree/master/1407-group-the-people-given-the-group-size-they-belong-to) |
| [1468-check-if-n-and-its-double-exist](https://github.com/MarkPhamm/Leetcode/tree/master/1468-check-if-n-and-its-double-exist) |
| [1476-count-negative-numbers-in-a-sorted-matrix](https://github.com/MarkPhamm/Leetcode/tree/master/1476-count-negative-numbers-in-a-sorted-matrix) |
| [1477-product-of-the-last-k-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/1477-product-of-the-last-k-numbers) |
| [1505-create-target-array-in-the-given-order](https://github.com/MarkPhamm/Leetcode/tree/master/1505-create-target-array-in-the-given-order) |
| [1514-minimum-value-to-get-positive-step-by-step-sum](https://github.com/MarkPhamm/Leetcode/tree/master/1514-minimum-value-to-get-positive-step-by-step-sum) |
| [1524-string-matching-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/1524-string-matching-in-an-array) |
| [1570-final-prices-with-a-special-discount-in-a-shop](https://github.com/MarkPhamm/Leetcode/tree/master/1570-final-prices-with-a-special-discount-in-a-shop) |
| [1603-running-sum-of-1d-array](https://github.com/MarkPhamm/Leetcode/tree/master/1603-running-sum-of-1d-array) |
| [1635-number-of-good-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/1635-number-of-good-pairs) |
| [1646-kth-missing-positive-number](https://github.com/MarkPhamm/Leetcode/tree/master/1646-kth-missing-positive-number) |
| [1656-count-good-triplets](https://github.com/MarkPhamm/Leetcode/tree/master/1656-count-good-triplets) |
| [1720-crawler-log-folder](https://github.com/MarkPhamm/Leetcode/tree/master/1720-crawler-log-folder) |
| [1741-sort-array-by-increasing-frequency](https://github.com/MarkPhamm/Leetcode/tree/master/1741-sort-array-by-increasing-frequency) |
| [1833-find-the-highest-altitude](https://github.com/MarkPhamm/Leetcode/tree/master/1833-find-the-highest-altitude) |
| [1848-sum-of-unique-elements](https://github.com/MarkPhamm/Leetcode/tree/master/1848-sum-of-unique-elements) |
| [1878-check-if-array-is-sorted-and-rotated](https://github.com/MarkPhamm/Leetcode/tree/master/1878-check-if-array-is-sorted-and-rotated) |
| [1886-minimum-limit-of-balls-in-a-bag](https://github.com/MarkPhamm/Leetcode/tree/master/1886-minimum-limit-of-balls-in-a-bag) |
| [1903-design-most-recently-used-queue](https://github.com/MarkPhamm/Leetcode/tree/master/1903-design-most-recently-used-queue) |
| [1917-maximum-average-pass-ratio](https://github.com/MarkPhamm/Leetcode/tree/master/1917-maximum-average-pass-ratio) |
| [1927-maximum-ascending-subarray-sum](https://github.com/MarkPhamm/Leetcode/tree/master/1927-maximum-ascending-subarray-sum) |
| [1944-truncate-sentence](https://github.com/MarkPhamm/Leetcode/tree/master/1944-truncate-sentence) |
| [2102-find-the-middle-index-in-array](https://github.com/MarkPhamm/Leetcode/tree/master/2102-find-the-middle-index-in-array) |
| [2107-find-unique-binary-string](https://github.com/MarkPhamm/Leetcode/tree/master/2107-find-unique-binary-string) |
| [2132-convert-1d-array-into-2d-array](https://github.com/MarkPhamm/Leetcode/tree/master/2132-convert-1d-array-into-2d-array) |
| [2137-final-value-of-variable-after-performing-operations](https://github.com/MarkPhamm/Leetcode/tree/master/2137-final-value-of-variable-after-performing-operations) |
| [2160-minimum-operations-to-make-a-uni-value-grid](https://github.com/MarkPhamm/Leetcode/tree/master/2160-minimum-operations-to-make-a-uni-value-grid) |
| [2163-kth-distinct-string-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/2163-kth-distinct-string-in-an-array) |
| [2164-two-best-non-overlapping-events](https://github.com/MarkPhamm/Leetcode/tree/master/2164-two-best-non-overlapping-events) |
| [2190-count-common-words-with-one-occurrence](https://github.com/MarkPhamm/Leetcode/tree/master/2190-count-common-words-with-one-occurrence) |
| [2195-time-needed-to-buy-tickets](https://github.com/MarkPhamm/Leetcode/tree/master/2195-time-needed-to-buy-tickets) |
| [2210-find-target-indices-after-sorting-array](https://github.com/MarkPhamm/Leetcode/tree/master/2210-find-target-indices-after-sorting-array) |
| [2211-k-radius-subarray-averages](https://github.com/MarkPhamm/Leetcode/tree/master/2211-k-radius-subarray-averages) |
| [2219-maximum-number-of-words-found-in-sentences](https://github.com/MarkPhamm/Leetcode/tree/master/2219-maximum-number-of-words-found-in-sentences) |
| [2220-find-all-possible-recipes-from-given-supplies](https://github.com/MarkPhamm/Leetcode/tree/master/2220-find-all-possible-recipes-from-given-supplies) |
| [2232-adding-spaces-to-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/2232-adding-spaces-to-a-string) |
| [2277-count-equal-and-divisible-pairs-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/2277-count-equal-and-divisible-pairs-in-an-array) |
| [2292-counting-words-with-a-given-prefix](https://github.com/MarkPhamm/Leetcode/tree/master/2292-counting-words-with-a-given-prefix) |
| [2308-divide-array-into-equal-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/2308-divide-array-into-equal-pairs) |
| [2350-find-closest-number-to-zero](https://github.com/MarkPhamm/Leetcode/tree/master/2350-find-closest-number-to-zero) |
| [2358-number-of-ways-to-split-array](https://github.com/MarkPhamm/Leetcode/tree/master/2358-number-of-ways-to-split-array) |
| [2392-successful-pairs-of-spells-and-potions](https://github.com/MarkPhamm/Leetcode/tree/master/2392-successful-pairs-of-spells-and-potions) |
| [2525-count-number-of-distinct-integers-after-reverse-operations](https://github.com/MarkPhamm/Leetcode/tree/master/2525-count-number-of-distinct-integers-after-reverse-operations) |
| [2614-maximum-count-of-positive-integer-and-negative-integer](https://github.com/MarkPhamm/Leetcode/tree/master/2614-maximum-count-of-positive-integer-and-negative-integer) |
| [2634-minimum-common-value](https://github.com/MarkPhamm/Leetcode/tree/master/2634-minimum-common-value) |
| [2640-maximum-number-of-integers-to-choose-from-a-range-i](https://github.com/MarkPhamm/Leetcode/tree/master/2640-maximum-number-of-integers-to-choose-from-a-range-i) |
| [2691-count-vowel-strings-in-ranges](https://github.com/MarkPhamm/Leetcode/tree/master/2691-count-vowel-strings-in-ranges) |
| [2692-take-gifts-from-the-richest-pile](https://github.com/MarkPhamm/Leetcode/tree/master/2692-take-gifts-from-the-richest-pile) |
| [2695-find-score-of-an-array-after-marking-all-elements](https://github.com/MarkPhamm/Leetcode/tree/master/2695-find-score-of-an-array-after-marking-all-elements) |
| [2699-count-the-number-of-fair-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/2699-count-the-number-of-fair-pairs) |
| [2707-merge-two-2d-arrays-by-summing-values](https://github.com/MarkPhamm/Leetcode/tree/master/2707-merge-two-2d-arrays-by-summing-values) |
| [2868-continuous-subarrays](https://github.com/MarkPhamm/Leetcode/tree/master/2868-continuous-subarrays) |
| [2888-minimum-index-of-a-valid-split](https://github.com/MarkPhamm/Leetcode/tree/master/2888-minimum-index-of-a-valid-split) |
| [2891-maximum-beauty-of-an-array-after-applying-operation](https://github.com/MarkPhamm/Leetcode/tree/master/2891-maximum-beauty-of-an-array-after-applying-operation) |
| [2917-count-pairs-whose-sum-is-less-than-target](https://github.com/MarkPhamm/Leetcode/tree/master/2917-count-pairs-whose-sum-is-less-than-target) |
| [2977-check-if-a-string-is-an-acronym-of-words](https://github.com/MarkPhamm/Leetcode/tree/master/2977-check-if-a-string-is-an-acronym-of-words) |
| [3152-maximum-value-of-an-ordered-triplet-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3152-maximum-value-of-an-ordered-triplet-ii) |
| [3318-find-x-sum-of-all-k-long-subarrays-i](https://github.com/MarkPhamm/Leetcode/tree/master/3318-find-x-sum-of-all-k-long-subarrays-i) |
| [3331-minimum-operations-to-exceed-threshold-value-i](https://github.com/MarkPhamm/Leetcode/tree/master/3331-minimum-operations-to-exceed-threshold-value-i) |
| [3334-apple-redistribution-into-boxes](https://github.com/MarkPhamm/Leetcode/tree/master/3334-apple-redistribution-into-boxes) |
| [3349-adjacent-increasing-subarrays-detection-i](https://github.com/MarkPhamm/Leetcode/tree/master/3349-adjacent-increasing-subarrays-detection-i) |
| [3372-longest-strictly-increasing-or-strictly-decreasing-subarray](https://github.com/MarkPhamm/Leetcode/tree/master/3372-longest-strictly-increasing-or-strictly-decreasing-subarray) |
| [3427-special-array-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3427-special-array-ii) |
| [3429-special-array-i](https://github.com/MarkPhamm/Leetcode/tree/master/3429-special-array-i) |
| [3446-find-the-number-of-good-pairs-i](https://github.com/MarkPhamm/Leetcode/tree/master/3446-find-the-number-of-good-pairs-i) |
| [3463-alternating-groups-i](https://github.com/MarkPhamm/Leetcode/tree/master/3463-alternating-groups-i) |
| [3483-alternating-groups-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3483-alternating-groups-ii) |
| [3577-convert-doubly-linked-list-to-array-i](https://github.com/MarkPhamm/Leetcode/tree/master/3577-convert-doubly-linked-list-to-array-i) |
| [3581-the-two-sneaky-numbers-of-digitville](https://github.com/MarkPhamm/Leetcode/tree/master/3581-the-two-sneaky-numbers-of-digitville) |
| [3582-find-indices-of-stable-mountains](https://github.com/MarkPhamm/Leetcode/tree/master/3582-find-indices-of-stable-mountains) |
| [3594-identify-the-largest-outlier-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/3594-identify-the-largest-outlier-in-an-array) |
| [3610-find-x-sum-of-all-k-long-subarrays-i](https://github.com/MarkPhamm/Leetcode/tree/master/3610-find-x-sum-of-all-k-long-subarrays-i) |
| [3615-convert-doubly-linked-list-to-array-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3615-convert-doubly-linked-list-to-array-ii) |
| [3621-minimum-operations-to-make-array-values-equal-to-k](https://github.com/MarkPhamm/Leetcode/tree/master/3621-minimum-operations-to-make-array-values-equal-to-k) |
| [3644-minimum-positive-sum-subarray](https://github.com/MarkPhamm/Leetcode/tree/master/3644-minimum-positive-sum-subarray) |
| [3656-minimum-number-of-operations-to-make-elements-in-array-distinct](https://github.com/MarkPhamm/Leetcode/tree/master/3656-minimum-number-of-operations-to-make-elements-in-array-distinct) |
| [3685-count-subarrays-of-length-three-with-a-condition](https://github.com/MarkPhamm/Leetcode/tree/master/3685-count-subarrays-of-length-three-with-a-condition) |
## Prefix Sum
|  |
| ------- |
| [0209-minimum-size-subarray-sum](https://github.com/MarkPhamm/Leetcode/tree/master/0209-minimum-size-subarray-sum) |
| [0238-product-of-array-except-self](https://github.com/MarkPhamm/Leetcode/tree/master/0238-product-of-array-except-self) |
| [0303-range-sum-query-immutable](https://github.com/MarkPhamm/Leetcode/tree/master/0303-range-sum-query-immutable) |
| [0325-maximum-size-subarray-sum-equals-k](https://github.com/MarkPhamm/Leetcode/tree/master/0325-maximum-size-subarray-sum-equals-k) |
| [0560-subarray-sum-equals-k](https://github.com/MarkPhamm/Leetcode/tree/master/0560-subarray-sum-equals-k) |
| [0724-find-pivot-index](https://github.com/MarkPhamm/Leetcode/tree/master/0724-find-pivot-index) |
| [1477-product-of-the-last-k-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/1477-product-of-the-last-k-numbers) |
| [1514-minimum-value-to-get-positive-step-by-step-sum](https://github.com/MarkPhamm/Leetcode/tree/master/1514-minimum-value-to-get-positive-step-by-step-sum) |
| [1537-maximum-score-after-splitting-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/1537-maximum-score-after-splitting-a-string) |
| [1603-running-sum-of-1d-array](https://github.com/MarkPhamm/Leetcode/tree/master/1603-running-sum-of-1d-array) |
| [1833-find-the-highest-altitude](https://github.com/MarkPhamm/Leetcode/tree/master/1833-find-the-highest-altitude) |
| [2102-find-the-middle-index-in-array](https://github.com/MarkPhamm/Leetcode/tree/master/2102-find-the-middle-index-in-array) |
| [2358-number-of-ways-to-split-array](https://github.com/MarkPhamm/Leetcode/tree/master/2358-number-of-ways-to-split-array) |
| [2571-find-the-pivot-integer](https://github.com/MarkPhamm/Leetcode/tree/master/2571-find-the-pivot-integer) |
| [2691-count-vowel-strings-in-ranges](https://github.com/MarkPhamm/Leetcode/tree/master/2691-count-vowel-strings-in-ranges) |
| [3427-special-array-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3427-special-array-ii) |
| [3644-minimum-positive-sum-subarray](https://github.com/MarkPhamm/Leetcode/tree/master/3644-minimum-positive-sum-subarray) |
## Database
|  |
| ------- |
| [0175-combine-two-tables](https://github.com/MarkPhamm/Leetcode/tree/master/0175-combine-two-tables) |
| [0176-second-highest-salary](https://github.com/MarkPhamm/Leetcode/tree/master/0176-second-highest-salary) |
| [0177-nth-highest-salary](https://github.com/MarkPhamm/Leetcode/tree/master/0177-nth-highest-salary) |
| [0178-rank-scores](https://github.com/MarkPhamm/Leetcode/tree/master/0178-rank-scores) |
| [0180-consecutive-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0180-consecutive-numbers) |
| [0181-employees-earning-more-than-their-managers](https://github.com/MarkPhamm/Leetcode/tree/master/0181-employees-earning-more-than-their-managers) |
| [0182-duplicate-emails](https://github.com/MarkPhamm/Leetcode/tree/master/0182-duplicate-emails) |
| [0183-customers-who-never-order](https://github.com/MarkPhamm/Leetcode/tree/master/0183-customers-who-never-order) |
| [0184-department-highest-salary](https://github.com/MarkPhamm/Leetcode/tree/master/0184-department-highest-salary) |
| [0185-department-top-three-salaries](https://github.com/MarkPhamm/Leetcode/tree/master/0185-department-top-three-salaries) |
| [0196-delete-duplicate-emails](https://github.com/MarkPhamm/Leetcode/tree/master/0196-delete-duplicate-emails) |
| [0197-rising-temperature](https://github.com/MarkPhamm/Leetcode/tree/master/0197-rising-temperature) |
| [0262-trips-and-users](https://github.com/MarkPhamm/Leetcode/tree/master/0262-trips-and-users) |
| [0512-game-play-analysis-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0512-game-play-analysis-ii) |
| [0569-median-employee-salary](https://github.com/MarkPhamm/Leetcode/tree/master/0569-median-employee-salary) |
| [0571-find-median-given-frequency-of-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0571-find-median-given-frequency-of-numbers) |
| [0574-winning-candidate](https://github.com/MarkPhamm/Leetcode/tree/master/0574-winning-candidate) |
| [0577-employee-bonus](https://github.com/MarkPhamm/Leetcode/tree/master/0577-employee-bonus) |
| [0578-get-highest-answer-rate-question](https://github.com/MarkPhamm/Leetcode/tree/master/0578-get-highest-answer-rate-question) |
| [0579-find-cumulative-salary-of-an-employee](https://github.com/MarkPhamm/Leetcode/tree/master/0579-find-cumulative-salary-of-an-employee) |
| [0580-count-student-number-in-departments](https://github.com/MarkPhamm/Leetcode/tree/master/0580-count-student-number-in-departments) |
| [0585-investments-in-2016](https://github.com/MarkPhamm/Leetcode/tree/master/0585-investments-in-2016) |
| [0586-customer-placing-the-largest-number-of-orders](https://github.com/MarkPhamm/Leetcode/tree/master/0586-customer-placing-the-largest-number-of-orders) |
| [0596-classes-more-than-5-students](https://github.com/MarkPhamm/Leetcode/tree/master/0596-classes-more-than-5-students) |
| [0597-friend-requests-i-overall-acceptance-rate](https://github.com/MarkPhamm/Leetcode/tree/master/0597-friend-requests-i-overall-acceptance-rate) |
| [0601-human-traffic-of-stadium](https://github.com/MarkPhamm/Leetcode/tree/master/0601-human-traffic-of-stadium) |
| [0602-friend-requests-ii-who-has-the-most-friends](https://github.com/MarkPhamm/Leetcode/tree/master/0602-friend-requests-ii-who-has-the-most-friends) |
| [0603-consecutive-available-seats](https://github.com/MarkPhamm/Leetcode/tree/master/0603-consecutive-available-seats) |
| [0607-sales-person](https://github.com/MarkPhamm/Leetcode/tree/master/0607-sales-person) |
| [0610-triangle-judgement](https://github.com/MarkPhamm/Leetcode/tree/master/0610-triangle-judgement) |
| [0612-shortest-distance-in-a-plane](https://github.com/MarkPhamm/Leetcode/tree/master/0612-shortest-distance-in-a-plane) |
| [0613-shortest-distance-in-a-line](https://github.com/MarkPhamm/Leetcode/tree/master/0613-shortest-distance-in-a-line) |
| [0614-second-degree-follower](https://github.com/MarkPhamm/Leetcode/tree/master/0614-second-degree-follower) |
| [0615-average-salary-departments-vs-company](https://github.com/MarkPhamm/Leetcode/tree/master/0615-average-salary-departments-vs-company) |
| [0618-students-report-by-geography](https://github.com/MarkPhamm/Leetcode/tree/master/0618-students-report-by-geography) |
| [0619-biggest-single-number](https://github.com/MarkPhamm/Leetcode/tree/master/0619-biggest-single-number) |
| [0626-exchange-seats](https://github.com/MarkPhamm/Leetcode/tree/master/0626-exchange-seats) |
| [0627-swap-salary](https://github.com/MarkPhamm/Leetcode/tree/master/0627-swap-salary) |
| [1135-customers-who-bought-all-products](https://github.com/MarkPhamm/Leetcode/tree/master/1135-customers-who-bought-all-products) |
| [1136-actors-and-directors-who-cooperated-at-least-three-times](https://github.com/MarkPhamm/Leetcode/tree/master/1136-actors-and-directors-who-cooperated-at-least-three-times) |
| [1153-product-sales-analysis-i](https://github.com/MarkPhamm/Leetcode/tree/master/1153-product-sales-analysis-i) |
| [1154-product-sales-analysis-ii](https://github.com/MarkPhamm/Leetcode/tree/master/1154-product-sales-analysis-ii) |
| [1162-project-employees-ii](https://github.com/MarkPhamm/Leetcode/tree/master/1162-project-employees-ii) |
| [1163-project-employees-iii](https://github.com/MarkPhamm/Leetcode/tree/master/1163-project-employees-iii) |
| [1172-sales-analysis-i](https://github.com/MarkPhamm/Leetcode/tree/master/1172-sales-analysis-i) |
| [1173-sales-analysis-ii](https://github.com/MarkPhamm/Leetcode/tree/master/1173-sales-analysis-ii) |
| [1179-game-play-analysis-i](https://github.com/MarkPhamm/Leetcode/tree/master/1179-game-play-analysis-i) |
| [1180-game-play-analysis-ii](https://github.com/MarkPhamm/Leetcode/tree/master/1180-game-play-analysis-ii) |
| [1181-game-play-analysis-iii](https://github.com/MarkPhamm/Leetcode/tree/master/1181-game-play-analysis-iii) |
| [1182-game-play-analysis-iv](https://github.com/MarkPhamm/Leetcode/tree/master/1182-game-play-analysis-iv) |
| [1193-game-play-analysis-v](https://github.com/MarkPhamm/Leetcode/tree/master/1193-game-play-analysis-v) |
| [1198-unpopular-books](https://github.com/MarkPhamm/Leetcode/tree/master/1198-unpopular-books) |
| [1204-new-users-daily-count](https://github.com/MarkPhamm/Leetcode/tree/master/1204-new-users-daily-count) |
| [1214-highest-grade-for-each-student](https://github.com/MarkPhamm/Leetcode/tree/master/1214-highest-grade-for-each-student) |
| [1215-reported-posts](https://github.com/MarkPhamm/Leetcode/tree/master/1215-reported-posts) |
| [1237-reported-posts-ii](https://github.com/MarkPhamm/Leetcode/tree/master/1237-reported-posts-ii) |
| [1246-user-activity-for-the-past-30-days-ii](https://github.com/MarkPhamm/Leetcode/tree/master/1246-user-activity-for-the-past-30-days-ii) |
| [1259-article-views-ii](https://github.com/MarkPhamm/Leetcode/tree/master/1259-article-views-ii) |
| [1269-market-analysis-ii](https://github.com/MarkPhamm/Leetcode/tree/master/1269-market-analysis-ii) |
| [1291-immediate-food-delivery-i](https://github.com/MarkPhamm/Leetcode/tree/master/1291-immediate-food-delivery-i) |
| [1318-tournament-winners](https://github.com/MarkPhamm/Leetcode/tree/master/1318-tournament-winners) |
| [1327-last-person-to-fit-in-the-bus](https://github.com/MarkPhamm/Leetcode/tree/master/1327-last-person-to-fit-in-the-bus) |
| [1328-monthly-transactions-ii](https://github.com/MarkPhamm/Leetcode/tree/master/1328-monthly-transactions-ii) |
| [1339-team-scores-in-football-tournament](https://github.com/MarkPhamm/Leetcode/tree/master/1339-team-scores-in-football-tournament) |
| [1357-report-contiguous-dates](https://github.com/MarkPhamm/Leetcode/tree/master/1357-report-contiguous-dates) |
| [1377-number-of-comments-per-post](https://github.com/MarkPhamm/Leetcode/tree/master/1377-number-of-comments-per-post) |
| [1384-total-sales-amount-by-year](https://github.com/MarkPhamm/Leetcode/tree/master/1384-total-sales-amount-by-year) |
| [1399-page-recommendations](https://github.com/MarkPhamm/Leetcode/tree/master/1399-page-recommendations) |
| [1405-all-people-report-to-the-given-manager](https://github.com/MarkPhamm/Leetcode/tree/master/1405-all-people-report-to-the-given-manager) |
| [1420-find-the-start-and-end-number-of-continuous-ranges](https://github.com/MarkPhamm/Leetcode/tree/master/1420-find-the-start-and-end-number-of-continuous-ranges) |
| [1425-weather-type-in-each-country](https://github.com/MarkPhamm/Leetcode/tree/master/1425-weather-type-in-each-country) |
| [1438-find-the-team-size](https://github.com/MarkPhamm/Leetcode/tree/master/1438-find-the-team-size) |
| [1439-running-total-for-different-genders](https://github.com/MarkPhamm/Leetcode/tree/master/1439-running-total-for-different-genders) |
| [1453-ads-performance](https://github.com/MarkPhamm/Leetcode/tree/master/1453-ads-performance) |
| [1481-students-with-invalid-departments](https://github.com/MarkPhamm/Leetcode/tree/master/1481-students-with-invalid-departments) |
| [1494-activity-participants](https://github.com/MarkPhamm/Leetcode/tree/master/1494-activity-participants) |
| [1495-number-of-trusted-contacts-of-a-customer](https://github.com/MarkPhamm/Leetcode/tree/master/1495-number-of-trusted-contacts-of-a-customer) |
| [1504-get-the-second-most-recent-activity](https://github.com/MarkPhamm/Leetcode/tree/master/1504-get-the-second-most-recent-activity) |
| [1536-customers-who-bought-products-a-and-b-but-not-c](https://github.com/MarkPhamm/Leetcode/tree/master/1536-customers-who-bought-products-a-and-b-but-not-c) |
| [1546-find-the-quiet-students-in-all-exams](https://github.com/MarkPhamm/Leetcode/tree/master/1546-find-the-quiet-students-in-all-exams) |
| [1551-npv-queries](https://github.com/MarkPhamm/Leetcode/tree/master/1551-npv-queries) |
| [1564-create-a-session-bar-chart](https://github.com/MarkPhamm/Leetcode/tree/master/1564-create-a-session-bar-chart) |
| [1565-evaluate-boolean-expression](https://github.com/MarkPhamm/Leetcode/tree/master/1565-evaluate-boolean-expression) |
| [1578-apples-oranges](https://github.com/MarkPhamm/Leetcode/tree/master/1578-apples-oranges) |
| [1579-active-users](https://github.com/MarkPhamm/Leetcode/tree/master/1579-active-users) |
| [1623-sales-by-day-of-the-week](https://github.com/MarkPhamm/Leetcode/tree/master/1623-sales-by-day-of-the-week) |
| [1625-group-sold-products-by-the-date](https://github.com/MarkPhamm/Leetcode/tree/master/1625-group-sold-products-by-the-date) |
| [1639-friendly-movies-streamed-last-month](https://github.com/MarkPhamm/Leetcode/tree/master/1639-friendly-movies-streamed-last-month) |
| [1641-countries-you-can-safely-invest-in](https://github.com/MarkPhamm/Leetcode/tree/master/1641-countries-you-can-safely-invest-in) |
| [1645-hopper-company-queries-ii](https://github.com/MarkPhamm/Leetcode/tree/master/1645-hopper-company-queries-ii) |
| [1654-customer-order-frequency](https://github.com/MarkPhamm/Leetcode/tree/master/1654-customer-order-frequency) |
| [1664-find-users-with-valid-e-mails](https://github.com/MarkPhamm/Leetcode/tree/master/1664-find-users-with-valid-e-mails) |
| [1686-fix-product-name-format](https://github.com/MarkPhamm/Leetcode/tree/master/1686-fix-product-name-format) |
| [1712-unique-orders-and-customers-per-month](https://github.com/MarkPhamm/Leetcode/tree/master/1712-unique-orders-and-customers-per-month) |
| [1718-warehouse-manager](https://github.com/MarkPhamm/Leetcode/tree/master/1718-warehouse-manager) |
| [1735-the-most-frequently-ordered-products-for-each-customer](https://github.com/MarkPhamm/Leetcode/tree/master/1735-the-most-frequently-ordered-products-for-each-customer) |
| [1749-sellers-with-no-sales](https://github.com/MarkPhamm/Leetcode/tree/master/1749-sellers-with-no-sales) |
| [1759-find-the-missing-ids](https://github.com/MarkPhamm/Leetcode/tree/master/1759-find-the-missing-ids) |
| [1795-hopper-company-queries-iii](https://github.com/MarkPhamm/Leetcode/tree/master/1795-hopper-company-queries-iii) |
| [1821-products-worth-over-invoices](https://github.com/MarkPhamm/Leetcode/tree/master/1821-products-worth-over-invoices) |
| [1852-biggest-window-between-visits](https://github.com/MarkPhamm/Leetcode/tree/master/1852-biggest-window-between-visits) |
| [1898-leetflex-banned-accounts](https://github.com/MarkPhamm/Leetcode/tree/master/1898-leetflex-banned-accounts) |
| [1914-find-the-subtasks-that-did-not-execute](https://github.com/MarkPhamm/Leetcode/tree/master/1914-find-the-subtasks-that-did-not-execute) |
| [1917-leetcodify-friends-recommendations](https://github.com/MarkPhamm/Leetcode/tree/master/1917-leetcodify-friends-recommendations) |
| [1919-leetcodify-similar-friends](https://github.com/MarkPhamm/Leetcode/tree/master/1919-leetcodify-similar-friends) |
| [1964-find-interview-candidates](https://github.com/MarkPhamm/Leetcode/tree/master/1964-find-interview-candidates) |
| [1991-league-statistics](https://github.com/MarkPhamm/Leetcode/tree/master/1991-league-statistics) |
| [1998-suspicious-bank-accounts](https://github.com/MarkPhamm/Leetcode/tree/master/1998-suspicious-bank-accounts) |
| [2014-orders-with-maximum-quantity-above-average](https://github.com/MarkPhamm/Leetcode/tree/master/2014-orders-with-maximum-quantity-above-average) |
| [2030-group-employees-of-the-same-salary](https://github.com/MarkPhamm/Leetcode/tree/master/2030-group-employees-of-the-same-salary) |
| [2092-users-that-actively-request-confirmation-messages](https://github.com/MarkPhamm/Leetcode/tree/master/2092-users-that-actively-request-confirmation-messages) |
| [2097-strong-friendship](https://github.com/MarkPhamm/Leetcode/tree/master/2097-strong-friendship) |
| [2136-find-cutoff-score-for-each-school](https://github.com/MarkPhamm/Leetcode/tree/master/2136-find-cutoff-score-for-each-school) |
| [2143-count-the-number-of-experiments](https://github.com/MarkPhamm/Leetcode/tree/master/2143-count-the-number-of-experiments) |
| [2167-number-of-accounts-that-did-not-stream](https://github.com/MarkPhamm/Leetcode/tree/master/2167-number-of-accounts-that-did-not-stream) |
| [2172-low-quality-problems](https://github.com/MarkPhamm/Leetcode/tree/master/2172-low-quality-problems) |
| [2185-accepted-candidates-from-the-interviews](https://github.com/MarkPhamm/Leetcode/tree/master/2185-accepted-candidates-from-the-interviews) |
| [2194-the-category-of-each-member-in-the-store](https://github.com/MarkPhamm/Leetcode/tree/master/2194-the-category-of-each-member-in-the-store) |
| [2199-finding-the-topic-of-each-post](https://github.com/MarkPhamm/Leetcode/tree/master/2199-finding-the-topic-of-each-post) |
| [2208-account-balance](https://github.com/MarkPhamm/Leetcode/tree/master/2208-account-balance) |
| [2214-the-winner-university](https://github.com/MarkPhamm/Leetcode/tree/master/2214-the-winner-university) |
| [2252-the-airport-with-the-most-traffic](https://github.com/MarkPhamm/Leetcode/tree/master/2252-the-airport-with-the-most-traffic) |
| [2281-the-number-of-passengers-in-each-bus-i](https://github.com/MarkPhamm/Leetcode/tree/master/2281-the-number-of-passengers-in-each-bus-i) |
| [2313-longest-winning-streak](https://github.com/MarkPhamm/Leetcode/tree/master/2313-longest-winning-streak) |
| [2315-the-change-in-global-rankings](https://github.com/MarkPhamm/Leetcode/tree/master/2315-the-change-in-global-rankings) |
| [2336-the-number-of-users-that-are-eligible-for-discount](https://github.com/MarkPhamm/Leetcode/tree/master/2336-the-number-of-users-that-are-eligible-for-discount) |
| [2370-users-with-two-purchases-within-seven-days](https://github.com/MarkPhamm/Leetcode/tree/master/2370-users-with-two-purchases-within-seven-days) |
| [2371-the-users-that-are-eligible-for-discount](https://github.com/MarkPhamm/Leetcode/tree/master/2371-the-users-that-are-eligible-for-discount) |
| [2431-products-with-three-or-more-orders-in-two-consecutive-years](https://github.com/MarkPhamm/Leetcode/tree/master/2431-products-with-three-or-more-orders-in-two-consecutive-years) |
| [2440-tasks-count-in-the-weekend](https://github.com/MarkPhamm/Leetcode/tree/master/2440-tasks-count-in-the-weekend) |
| [2441-arrange-table-by-gender](https://github.com/MarkPhamm/Leetcode/tree/master/2441-arrange-table-by-gender) |
| [2446-the-first-day-of-the-maximum-recorded-degree-in-each-city](https://github.com/MarkPhamm/Leetcode/tree/master/2446-the-first-day-of-the-maximum-recorded-degree-in-each-city) |
| [2451-product-sales-analysis-iv](https://github.com/MarkPhamm/Leetcode/tree/master/2451-product-sales-analysis-iv) |
| [2452-product-sales-analysis-v](https://github.com/MarkPhamm/Leetcode/tree/master/2452-product-sales-analysis-v) |
| [2474-customers-with-strictly-increasing-purchases](https://github.com/MarkPhamm/Leetcode/tree/master/2474-customers-with-strictly-increasing-purchases) |
| [2484-compute-the-rank-as-a-percentage](https://github.com/MarkPhamm/Leetcode/tree/master/2484-compute-the-rank-as-a-percentage) |
| [2494-merge-overlapping-events-in-the-same-hall](https://github.com/MarkPhamm/Leetcode/tree/master/2494-merge-overlapping-events-in-the-same-hall) |
| [2515-calculate-the-influence-of-each-salesperson](https://github.com/MarkPhamm/Leetcode/tree/master/2515-calculate-the-influence-of-each-salesperson) |
| [2516-sort-the-olympic-table](https://github.com/MarkPhamm/Leetcode/tree/master/2516-sort-the-olympic-table) |
| [2523-change-null-values-in-a-table-to-the-previous-value](https://github.com/MarkPhamm/Leetcode/tree/master/2523-change-null-values-in-a-table-to-the-previous-value) |
| [2534-employees-with-deductions](https://github.com/MarkPhamm/Leetcode/tree/master/2534-employees-with-deductions) |
| [2622-form-a-chemical-bond](https://github.com/MarkPhamm/Leetcode/tree/master/2622-form-a-chemical-bond) |
| [2643-concatenate-the-name-and-the-profession](https://github.com/MarkPhamm/Leetcode/tree/master/2643-concatenate-the-name-and-the-profession) |
| [2720-popularity-percentage](https://github.com/MarkPhamm/Leetcode/tree/master/2720-popularity-percentage) |
| [2829-find-latest-salaries](https://github.com/MarkPhamm/Leetcode/tree/master/2829-find-latest-salaries) |
| [2830-count-artist-occurrences-on-spotify-ranking-list](https://github.com/MarkPhamm/Leetcode/tree/master/2830-count-artist-occurrences-on-spotify-ranking-list) |
| [2840-immediate-food-delivery-iii](https://github.com/MarkPhamm/Leetcode/tree/master/2840-immediate-food-delivery-iii) |
| [2841-bikes-last-time-used](https://github.com/MarkPhamm/Leetcode/tree/master/2841-bikes-last-time-used) |
| [2842-find-active-users](https://github.com/MarkPhamm/Leetcode/tree/master/2842-find-active-users) |
| [2853-consecutive-transactions-with-increasing-amounts](https://github.com/MarkPhamm/Leetcode/tree/master/2853-consecutive-transactions-with-increasing-amounts) |
| [3002-flight-occupancy-and-waitlist-analysis](https://github.com/MarkPhamm/Leetcode/tree/master/3002-flight-occupancy-and-waitlist-analysis) |
| [3061-calculate-trapping-rain-water](https://github.com/MarkPhamm/Leetcode/tree/master/3061-calculate-trapping-rain-water) |
| [3103-find-trending-hashtags-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3103-find-trending-hashtags-ii) |
| [3155-highest-salaries-difference](https://github.com/MarkPhamm/Leetcode/tree/master/3155-highest-salaries-difference) |
| [3156-rolling-average-steps](https://github.com/MarkPhamm/Leetcode/tree/master/3156-rolling-average-steps) |
| [3156-employee-task-duration-and-concurrent-tasks](https://github.com/MarkPhamm/Leetcode/tree/master/3156-employee-task-duration-and-concurrent-tasks) |
| [3160-calculate-orders-within-each-interval](https://github.com/MarkPhamm/Leetcode/tree/master/3160-calculate-orders-within-each-interval) |
| [3188-find-top-scoring-students-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3188-find-top-scoring-students-ii) |
| [3205-market-analysis-iii](https://github.com/MarkPhamm/Leetcode/tree/master/3205-market-analysis-iii) |
| [3253-symmetric-coordinates](https://github.com/MarkPhamm/Leetcode/tree/master/3253-symmetric-coordinates) |
| [3255-pizza-toppings-cost-analysis](https://github.com/MarkPhamm/Leetcode/tree/master/3255-pizza-toppings-cost-analysis) |
| [3256-find-candidates-for-data-scientist-position](https://github.com/MarkPhamm/Leetcode/tree/master/3256-find-candidates-for-data-scientist-position) |
| [3257-maximize-items](https://github.com/MarkPhamm/Leetcode/tree/master/3257-maximize-items) |
| [3258-classifying-triangles-by-lengths](https://github.com/MarkPhamm/Leetcode/tree/master/3258-classifying-triangles-by-lengths) |
| [3259-binary-tree-nodes](https://github.com/MarkPhamm/Leetcode/tree/master/3259-binary-tree-nodes) |
| [3281-find-peak-calling-hours-for-each-city](https://github.com/MarkPhamm/Leetcode/tree/master/3281-find-peak-calling-hours-for-each-city) |
| [3283-find-third-transaction](https://github.com/MarkPhamm/Leetcode/tree/master/3283-find-third-transaction) |
| [3284-find-expensive-cities](https://github.com/MarkPhamm/Leetcode/tree/master/3284-find-expensive-cities) |
| [3285-manager-of-the-largest-department](https://github.com/MarkPhamm/Leetcode/tree/master/3285-manager-of-the-largest-department) |
| [3286-class-performance](https://github.com/MarkPhamm/Leetcode/tree/master/3286-class-performance) |
| [3287-loan-types](https://github.com/MarkPhamm/Leetcode/tree/master/3287-loan-types) |
| [3288-top-three-wineries](https://github.com/MarkPhamm/Leetcode/tree/master/3288-top-three-wineries) |
| [3300-friday-purchases-i](https://github.com/MarkPhamm/Leetcode/tree/master/3300-friday-purchases-i) |
| [3302-viewers-turned-streamers](https://github.com/MarkPhamm/Leetcode/tree/master/3302-viewers-turned-streamers) |
| [3339-top-percentile-fraud](https://github.com/MarkPhamm/Leetcode/tree/master/3339-top-percentile-fraud) |
| [3340-snaps-analysis](https://github.com/MarkPhamm/Leetcode/tree/master/3340-snaps-analysis) |
| [3357-employees-project-allocation](https://github.com/MarkPhamm/Leetcode/tree/master/3357-employees-project-allocation) |
| [3365-find-all-unique-email-domains](https://github.com/MarkPhamm/Leetcode/tree/master/3365-find-all-unique-email-domains) |
| [3368-first-letter-capitalization](https://github.com/MarkPhamm/Leetcode/tree/master/3368-first-letter-capitalization) |
| [3369-calculate-trapping-rain-water](https://github.com/MarkPhamm/Leetcode/tree/master/3369-calculate-trapping-rain-water) |
| [3374-first-letter-capitalization-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3374-first-letter-capitalization-ii) |
| [3432-find-longest-calls](https://github.com/MarkPhamm/Leetcode/tree/master/3432-find-longest-calls) |
| [3440-server-utilization-time](https://github.com/MarkPhamm/Leetcode/tree/master/3440-server-utilization-time) |
| [3457-invalid-tweets-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3457-invalid-tweets-ii) |
| [3473-calculate-parking-fees-and-duration](https://github.com/MarkPhamm/Leetcode/tree/master/3473-calculate-parking-fees-and-duration) |
| [3481-second-day-verification](https://github.com/MarkPhamm/Leetcode/tree/master/3481-second-day-verification) |
| [3482-analyze-organization-hierarchy](https://github.com/MarkPhamm/Leetcode/tree/master/3482-analyze-organization-hierarchy) |
| [3488-find-top-scoring-students](https://github.com/MarkPhamm/Leetcode/tree/master/3488-find-top-scoring-students) |
| [3505-find-cities-in-each-state](https://github.com/MarkPhamm/Leetcode/tree/master/3505-find-cities-in-each-state) |
| [3512-bitwise-user-permissions-analysis](https://github.com/MarkPhamm/Leetcode/tree/master/3512-bitwise-user-permissions-analysis) |
| [3520-year-on-year-growth-rate](https://github.com/MarkPhamm/Leetcode/tree/master/3520-year-on-year-growth-rate) |
| [3539-customer-purchasing-behavior-analysis](https://github.com/MarkPhamm/Leetcode/tree/master/3539-customer-purchasing-behavior-analysis) |
| [3549-ceo-subordinate-hierarchy](https://github.com/MarkPhamm/Leetcode/tree/master/3549-ceo-subordinate-hierarchy) |
| [3554-premier-league-table-ranking](https://github.com/MarkPhamm/Leetcode/tree/master/3554-premier-league-table-ranking) |
| [3554-find-category-recommendation-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/3554-find-category-recommendation-pairs) |
| [3574-find-overlapping-shifts](https://github.com/MarkPhamm/Leetcode/tree/master/3574-find-overlapping-shifts) |
| [3589-find-candidates-for-data-scientist-position-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3589-find-candidates-for-data-scientist-position-ii) |
| [3611-find-overbooked-employees](https://github.com/MarkPhamm/Leetcode/tree/master/3611-find-overbooked-employees) |
| [3624-find-top-performing-driver](https://github.com/MarkPhamm/Leetcode/tree/master/3624-find-top-performing-driver) |
| [3642-premier-league-table-ranking-iii](https://github.com/MarkPhamm/Leetcode/tree/master/3642-premier-league-table-ranking-iii) |
| [3650-find-cities-in-each-state-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3650-find-cities-in-each-state-ii) |
| [3695-books-with-null-ratings](https://github.com/MarkPhamm/Leetcode/tree/master/3695-books-with-null-ratings) |
| [3719-team-dominance-by-pass-success](https://github.com/MarkPhamm/Leetcode/tree/master/3719-team-dominance-by-pass-success) |
| [3757-find-products-with-three-consecutive-digits](https://github.com/MarkPhamm/Leetcode/tree/master/3757-find-products-with-three-consecutive-digits) |
| [3782-find-valid-emails](https://github.com/MarkPhamm/Leetcode/tree/master/3782-find-valid-emails) |
| [3792-find-invalid-ip-addresses](https://github.com/MarkPhamm/Leetcode/tree/master/3792-find-invalid-ip-addresses) |
| [3865-find-product-recommendation-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/3865-find-product-recommendation-pairs) |
| [3898-seasonal-sales-analysis](https://github.com/MarkPhamm/Leetcode/tree/master/3898-seasonal-sales-analysis) |
| [3910-find-books-with-no-available-copies](https://github.com/MarkPhamm/Leetcode/tree/master/3910-find-books-with-no-available-copies) |
| [3921-find-consistently-improving-employees](https://github.com/MarkPhamm/Leetcode/tree/master/3921-find-consistently-improving-employees) |
| [3932-find-covid-recovery-patients](https://github.com/MarkPhamm/Leetcode/tree/master/3932-find-covid-recovery-patients) |
## Math
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0002-add-two-numbers) |
| [0007-reverse-integer](https://github.com/MarkPhamm/Leetcode/tree/master/0007-reverse-integer) |
| [0009-palindrome-number](https://github.com/MarkPhamm/Leetcode/tree/master/0009-palindrome-number) |
| [0013-roman-to-integer](https://github.com/MarkPhamm/Leetcode/tree/master/0013-roman-to-integer) |
| [0066-plus-one](https://github.com/MarkPhamm/Leetcode/tree/master/0066-plus-one) |
| [0067-add-binary](https://github.com/MarkPhamm/Leetcode/tree/master/0067-add-binary) |
| [0069-sqrtx](https://github.com/MarkPhamm/Leetcode/tree/master/0069-sqrtx) |
| [0070-climbing-stairs](https://github.com/MarkPhamm/Leetcode/tree/master/0070-climbing-stairs) |
| [0168-excel-sheet-column-title](https://github.com/MarkPhamm/Leetcode/tree/master/0168-excel-sheet-column-title) |
| [0171-excel-sheet-column-number](https://github.com/MarkPhamm/Leetcode/tree/master/0171-excel-sheet-column-number) |
| [0326-power-of-three](https://github.com/MarkPhamm/Leetcode/tree/master/0326-power-of-three) |
| [0367-valid-perfect-square](https://github.com/MarkPhamm/Leetcode/tree/master/0367-valid-perfect-square) |
| [0412-fizz-buzz](https://github.com/MarkPhamm/Leetcode/tree/master/0412-fizz-buzz) |
| [0509-fibonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/0509-fibonacci-number) |
| [0628-maximum-product-of-three-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0628-maximum-product-of-three-numbers) |
| [0633-sum-of-square-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0633-sum-of-square-numbers) |
| [1013-fibonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/1013-fibonacci-number) |
| [1137-n-th-tribonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/1137-n-th-tribonacci-number) |
| [1236-n-th-tribonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/1236-n-th-tribonacci-number) |
| [1304-find-n-unique-integers-sum-up-to-zero](https://github.com/MarkPhamm/Leetcode/tree/master/1304-find-n-unique-integers-sum-up-to-zero) |
| [1345-perform-string-shifts](https://github.com/MarkPhamm/Leetcode/tree/master/1345-perform-string-shifts) |
| [1406-subtract-the-product-and-sum-of-digits-of-an-integer](https://github.com/MarkPhamm/Leetcode/tree/master/1406-subtract-the-product-and-sum-of-digits-of-an-integer) |
| [1411-convert-binary-number-in-a-linked-list-to-integer](https://github.com/MarkPhamm/Leetcode/tree/master/1411-convert-binary-number-in-a-linked-list-to-integer) |
| [1444-number-of-steps-to-reduce-a-number-to-zero](https://github.com/MarkPhamm/Leetcode/tree/master/1444-number-of-steps-to-reduce-a-number-to-zero) |
| [1448-maximum-69-number](https://github.com/MarkPhamm/Leetcode/tree/master/1448-maximum-69-number) |
| [1477-product-of-the-last-k-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/1477-product-of-the-last-k-numbers) |
| [1500-count-largest-group](https://github.com/MarkPhamm/Leetcode/tree/master/1500-count-largest-group) |
| [1585-the-kth-factor-of-n](https://github.com/MarkPhamm/Leetcode/tree/master/1585-the-kth-factor-of-n) |
| [1635-number-of-good-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/1635-number-of-good-pairs) |
| [1642-water-bottles](https://github.com/MarkPhamm/Leetcode/tree/master/1642-water-bottles) |
| [1889-check-if-number-is-a-sum-of-powers-of-three](https://github.com/MarkPhamm/Leetcode/tree/master/1889-check-if-number-is-a-sum-of-powers-of-three) |
| [2160-minimum-operations-to-make-a-uni-value-grid](https://github.com/MarkPhamm/Leetcode/tree/master/2160-minimum-operations-to-make-a-uni-value-grid) |
| [2481-strictly-palindromic-number](https://github.com/MarkPhamm/Leetcode/tree/master/2481-strictly-palindromic-number) |
| [2525-count-number-of-distinct-integers-after-reverse-operations](https://github.com/MarkPhamm/Leetcode/tree/master/2525-count-number-of-distinct-integers-after-reverse-operations) |
| [2571-find-the-pivot-integer](https://github.com/MarkPhamm/Leetcode/tree/master/2571-find-the-pivot-integer) |
| [2649-count-total-number-of-colored-cells](https://github.com/MarkPhamm/Leetcode/tree/master/2649-count-total-number-of-colored-cells) |
| [2998-count-symmetric-integers](https://github.com/MarkPhamm/Leetcode/tree/master/2998-count-symmetric-integers) |
| [3581-the-two-sneaky-numbers-of-digitville](https://github.com/MarkPhamm/Leetcode/tree/master/3581-the-two-sneaky-numbers-of-digitville) |
## String
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/MarkPhamm/Leetcode/tree/master/0003-longest-substring-without-repeating-characters) |
| [0005-longest-palindromic-substring](https://github.com/MarkPhamm/Leetcode/tree/master/0005-longest-palindromic-substring) |
| [0013-roman-to-integer](https://github.com/MarkPhamm/Leetcode/tree/master/0013-roman-to-integer) |
| [0014-longest-common-prefix](https://github.com/MarkPhamm/Leetcode/tree/master/0014-longest-common-prefix) |
| [0017-letter-combinations-of-a-phone-number](https://github.com/MarkPhamm/Leetcode/tree/master/0017-letter-combinations-of-a-phone-number) |
| [0020-valid-parentheses](https://github.com/MarkPhamm/Leetcode/tree/master/0020-valid-parentheses) |
| [0022-generate-parentheses](https://github.com/MarkPhamm/Leetcode/tree/master/0022-generate-parentheses) |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
| [0049-group-anagrams](https://github.com/MarkPhamm/Leetcode/tree/master/0049-group-anagrams) |
| [0058-length-of-last-word](https://github.com/MarkPhamm/Leetcode/tree/master/0058-length-of-last-word) |
| [0067-add-binary](https://github.com/MarkPhamm/Leetcode/tree/master/0067-add-binary) |
| [0125-valid-palindrome](https://github.com/MarkPhamm/Leetcode/tree/master/0125-valid-palindrome) |
| [0168-excel-sheet-column-title](https://github.com/MarkPhamm/Leetcode/tree/master/0168-excel-sheet-column-title) |
| [0171-excel-sheet-column-number](https://github.com/MarkPhamm/Leetcode/tree/master/0171-excel-sheet-column-number) |
| [0242-valid-anagram](https://github.com/MarkPhamm/Leetcode/tree/master/0242-valid-anagram) |
| [0266-palindrome-permutation](https://github.com/MarkPhamm/Leetcode/tree/master/0266-palindrome-permutation) |
| [0290-word-pattern](https://github.com/MarkPhamm/Leetcode/tree/master/0290-word-pattern) |
| [0344-reverse-string](https://github.com/MarkPhamm/Leetcode/tree/master/0344-reverse-string) |
| [0345-reverse-vowels-of-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0345-reverse-vowels-of-a-string) |
| [0383-ransom-note](https://github.com/MarkPhamm/Leetcode/tree/master/0383-ransom-note) |
| [0387-first-unique-character-in-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0387-first-unique-character-in-a-string) |
| [0389-find-the-difference](https://github.com/MarkPhamm/Leetcode/tree/master/0389-find-the-difference) |
| [0392-is-subsequence](https://github.com/MarkPhamm/Leetcode/tree/master/0392-is-subsequence) |
| [0412-fizz-buzz](https://github.com/MarkPhamm/Leetcode/tree/master/0412-fizz-buzz) |
| [0424-longest-repeating-character-replacement](https://github.com/MarkPhamm/Leetcode/tree/master/0424-longest-repeating-character-replacement) |
| [0438-find-all-anagrams-in-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0438-find-all-anagrams-in-a-string) |
| [0782-jewels-and-stones](https://github.com/MarkPhamm/Leetcode/tree/master/0782-jewels-and-stones) |
| [0812-rotate-string](https://github.com/MarkPhamm/Leetcode/tree/master/0812-rotate-string) |
| [0874-backspace-string-compare](https://github.com/MarkPhamm/Leetcode/tree/master/0874-backspace-string-compare) |
| [1044-find-common-characters](https://github.com/MarkPhamm/Leetcode/tree/master/1044-find-common-characters) |
| [1089-remove-vowels-from-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/1089-remove-vowels-from-a-string) |
| [1128-remove-all-adjacent-duplicates-in-string](https://github.com/MarkPhamm/Leetcode/tree/master/1128-remove-all-adjacent-duplicates-in-string) |
| [1297-maximum-number-of-balloons](https://github.com/MarkPhamm/Leetcode/tree/master/1297-maximum-number-of-balloons) |
| [1302-delete-characters-to-make-fancy-string](https://github.com/MarkPhamm/Leetcode/tree/master/1302-delete-characters-to-make-fancy-string) |
| [1345-perform-string-shifts](https://github.com/MarkPhamm/Leetcode/tree/master/1345-perform-string-shifts) |
| [1460-number-of-substrings-containing-all-three-characters](https://github.com/MarkPhamm/Leetcode/tree/master/1460-number-of-substrings-containing-all-three-characters) |
| [1524-string-matching-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/1524-string-matching-in-an-array) |
| [1537-maximum-score-after-splitting-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/1537-maximum-score-after-splitting-a-string) |
| [1542-consecutive-characters](https://github.com/MarkPhamm/Leetcode/tree/master/1542-consecutive-characters) |
| [1666-make-the-string-great](https://github.com/MarkPhamm/Leetcode/tree/master/1666-make-the-string-great) |
| [1720-crawler-log-folder](https://github.com/MarkPhamm/Leetcode/tree/master/1720-crawler-log-folder) |
| [1737-maximum-nesting-depth-of-the-parentheses](https://github.com/MarkPhamm/Leetcode/tree/master/1737-maximum-nesting-depth-of-the-parentheses) |
| [1797-goal-parser-interpretation](https://github.com/MarkPhamm/Leetcode/tree/master/1797-goal-parser-interpretation) |
| [1894-merge-strings-alternately](https://github.com/MarkPhamm/Leetcode/tree/master/1894-merge-strings-alternately) |
| [1915-check-if-one-string-swap-can-make-strings-equal](https://github.com/MarkPhamm/Leetcode/tree/master/1915-check-if-one-string-swap-can-make-strings-equal) |
| [1944-truncate-sentence](https://github.com/MarkPhamm/Leetcode/tree/master/1944-truncate-sentence) |
| [1999-longer-contiguous-segments-of-ones-than-zeros](https://github.com/MarkPhamm/Leetcode/tree/master/1999-longer-contiguous-segments-of-ones-than-zeros) |
| [2021-remove-all-occurrences-of-a-substring](https://github.com/MarkPhamm/Leetcode/tree/master/2021-remove-all-occurrences-of-a-substring) |
| [2107-find-unique-binary-string](https://github.com/MarkPhamm/Leetcode/tree/master/2107-find-unique-binary-string) |
| [2128-reverse-prefix-of-word](https://github.com/MarkPhamm/Leetcode/tree/master/2128-reverse-prefix-of-word) |
| [2137-final-value-of-variable-after-performing-operations](https://github.com/MarkPhamm/Leetcode/tree/master/2137-final-value-of-variable-after-performing-operations) |
| [2163-kth-distinct-string-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/2163-kth-distinct-string-in-an-array) |
| [2168-check-if-numbers-are-ascending-in-a-sentence](https://github.com/MarkPhamm/Leetcode/tree/master/2168-check-if-numbers-are-ascending-in-a-sentence) |
| [2190-count-common-words-with-one-occurrence](https://github.com/MarkPhamm/Leetcode/tree/master/2190-count-common-words-with-one-occurrence) |
| [2219-maximum-number-of-words-found-in-sentences](https://github.com/MarkPhamm/Leetcode/tree/master/2219-maximum-number-of-words-found-in-sentences) |
| [2220-find-all-possible-recipes-from-given-supplies](https://github.com/MarkPhamm/Leetcode/tree/master/2220-find-all-possible-recipes-from-given-supplies) |
| [2232-adding-spaces-to-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/2232-adding-spaces-to-a-string) |
| [2243-check-if-all-as-appears-before-all-bs](https://github.com/MarkPhamm/Leetcode/tree/master/2243-check-if-all-as-appears-before-all-bs) |
| [2292-counting-words-with-a-given-prefix](https://github.com/MarkPhamm/Leetcode/tree/master/2292-counting-words-with-a-given-prefix) |
| [2401-count-asterisks](https://github.com/MarkPhamm/Leetcode/tree/master/2401-count-asterisks) |
| [2414-move-pieces-to-obtain-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/2414-move-pieces-to-obtain-a-string) |
| [2456-construct-smallest-number-from-di-string](https://github.com/MarkPhamm/Leetcode/tree/master/2456-construct-smallest-number-from-di-string) |
| [2463-minimum-recolors-to-get-k-consecutive-black-blocks](https://github.com/MarkPhamm/Leetcode/tree/master/2463-minimum-recolors-to-get-k-consecutive-black-blocks) |
| [2470-removing-stars-from-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/2470-removing-stars-from-a-string) |
| [2691-count-vowel-strings-in-ranges](https://github.com/MarkPhamm/Leetcode/tree/master/2691-count-vowel-strings-in-ranges) |
| [2800-minimum-string-length-after-removing-substrings](https://github.com/MarkPhamm/Leetcode/tree/master/2800-minimum-string-length-after-removing-substrings) |
| [2977-check-if-a-string-is-an-acronym-of-words](https://github.com/MarkPhamm/Leetcode/tree/master/2977-check-if-a-string-is-an-acronym-of-words) |
| [3018-make-string-a-subsequence-using-cyclic-increments](https://github.com/MarkPhamm/Leetcode/tree/master/3018-make-string-a-subsequence-using-cyclic-increments) |
| [3267-find-longest-special-substring-that-occurs-thrice-i](https://github.com/MarkPhamm/Leetcode/tree/master/3267-find-longest-special-substring-that-occurs-thrice-i) |
| [3312-number-of-changing-keys](https://github.com/MarkPhamm/Leetcode/tree/master/3312-number-of-changing-keys) |
| [3349-maximum-length-substring-with-two-occurrences](https://github.com/MarkPhamm/Leetcode/tree/master/3349-maximum-length-substring-with-two-occurrences) |
| [3379-score-of-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/3379-score-of-a-string) |
| [3447-clear-digits](https://github.com/MarkPhamm/Leetcode/tree/master/3447-clear-digits) |
| [3543-count-substrings-that-satisfy-k-constraint-i](https://github.com/MarkPhamm/Leetcode/tree/master/3543-count-substrings-that-satisfy-k-constraint-i) |
## Simulation
|  |
| ------- |
| [0067-add-binary](https://github.com/MarkPhamm/Leetcode/tree/master/0067-add-binary) |
| [0412-fizz-buzz](https://github.com/MarkPhamm/Leetcode/tree/master/0412-fizz-buzz) |
| [0682-baseball-game](https://github.com/MarkPhamm/Leetcode/tree/master/0682-baseball-game) |
| [0735-asteroid-collision](https://github.com/MarkPhamm/Leetcode/tree/master/0735-asteroid-collision) |
| [0874-backspace-string-compare](https://github.com/MarkPhamm/Leetcode/tree/master/0874-backspace-string-compare) |
| [0987-reveal-cards-in-increasing-order](https://github.com/MarkPhamm/Leetcode/tree/master/0987-reveal-cards-in-increasing-order) |
| [1505-create-target-array-in-the-given-order](https://github.com/MarkPhamm/Leetcode/tree/master/1505-create-target-array-in-the-given-order) |
| [1642-water-bottles](https://github.com/MarkPhamm/Leetcode/tree/master/1642-water-bottles) |
| [2021-remove-all-occurrences-of-a-substring](https://github.com/MarkPhamm/Leetcode/tree/master/2021-remove-all-occurrences-of-a-substring) |
| [2132-convert-1d-array-into-2d-array](https://github.com/MarkPhamm/Leetcode/tree/master/2132-convert-1d-array-into-2d-array) |
| [2137-final-value-of-variable-after-performing-operations](https://github.com/MarkPhamm/Leetcode/tree/master/2137-final-value-of-variable-after-performing-operations) |
| [2195-time-needed-to-buy-tickets](https://github.com/MarkPhamm/Leetcode/tree/master/2195-time-needed-to-buy-tickets) |
| [2232-adding-spaces-to-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/2232-adding-spaces-to-a-string) |
| [2470-removing-stars-from-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/2470-removing-stars-from-a-string) |
| [2692-take-gifts-from-the-richest-pile](https://github.com/MarkPhamm/Leetcode/tree/master/2692-take-gifts-from-the-richest-pile) |
| [2695-find-score-of-an-array-after-marking-all-elements](https://github.com/MarkPhamm/Leetcode/tree/master/2695-find-score-of-an-array-after-marking-all-elements) |
| [2800-minimum-string-length-after-removing-substrings](https://github.com/MarkPhamm/Leetcode/tree/master/2800-minimum-string-length-after-removing-substrings) |
| [3447-clear-digits](https://github.com/MarkPhamm/Leetcode/tree/master/3447-clear-digits) |
## Bit Manipulation
|  |
| ------- |
| [0067-add-binary](https://github.com/MarkPhamm/Leetcode/tree/master/0067-add-binary) |
| [0078-subsets](https://github.com/MarkPhamm/Leetcode/tree/master/0078-subsets) |
| [0090-subsets-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0090-subsets-ii) |
| [0136-single-number](https://github.com/MarkPhamm/Leetcode/tree/master/0136-single-number) |
| [0266-palindrome-permutation](https://github.com/MarkPhamm/Leetcode/tree/master/0266-palindrome-permutation) |
| [0389-find-the-difference](https://github.com/MarkPhamm/Leetcode/tree/master/0389-find-the-difference) |
| [0645-set-mismatch](https://github.com/MarkPhamm/Leetcode/tree/master/0645-set-mismatch) |
| [1444-number-of-steps-to-reduce-a-number-to-zero](https://github.com/MarkPhamm/Leetcode/tree/master/1444-number-of-steps-to-reduce-a-number-to-zero) |
| [2308-divide-array-into-equal-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/2308-divide-array-into-equal-pairs) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/MarkPhamm/Leetcode/tree/master/0001-two-sum) |
| [0003-longest-substring-without-repeating-characters](https://github.com/MarkPhamm/Leetcode/tree/master/0003-longest-substring-without-repeating-characters) |
| [0013-roman-to-integer](https://github.com/MarkPhamm/Leetcode/tree/master/0013-roman-to-integer) |
| [0017-letter-combinations-of-a-phone-number](https://github.com/MarkPhamm/Leetcode/tree/master/0017-letter-combinations-of-a-phone-number) |
| [0049-group-anagrams](https://github.com/MarkPhamm/Leetcode/tree/master/0049-group-anagrams) |
| [0128-longest-consecutive-sequence](https://github.com/MarkPhamm/Leetcode/tree/master/0128-longest-consecutive-sequence) |
| [0141-linked-list-cycle](https://github.com/MarkPhamm/Leetcode/tree/master/0141-linked-list-cycle) |
| [0146-lru-cache](https://github.com/MarkPhamm/Leetcode/tree/master/0146-lru-cache) |
| [0169-majority-element](https://github.com/MarkPhamm/Leetcode/tree/master/0169-majority-element) |
| [0170-two-sum-iii-data-structure-design](https://github.com/MarkPhamm/Leetcode/tree/master/0170-two-sum-iii-data-structure-design) |
| [0217-contains-duplicate](https://github.com/MarkPhamm/Leetcode/tree/master/0217-contains-duplicate) |
| [0219-contains-duplicate-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0219-contains-duplicate-ii) |
| [0242-valid-anagram](https://github.com/MarkPhamm/Leetcode/tree/master/0242-valid-anagram) |
| [0266-palindrome-permutation](https://github.com/MarkPhamm/Leetcode/tree/master/0266-palindrome-permutation) |
| [0290-word-pattern](https://github.com/MarkPhamm/Leetcode/tree/master/0290-word-pattern) |
| [0325-maximum-size-subarray-sum-equals-k](https://github.com/MarkPhamm/Leetcode/tree/master/0325-maximum-size-subarray-sum-equals-k) |
| [0347-top-k-frequent-elements](https://github.com/MarkPhamm/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [0349-intersection-of-two-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/0349-intersection-of-two-arrays) |
| [0350-intersection-of-two-arrays-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0350-intersection-of-two-arrays-ii) |
| [0359-logger-rate-limiter](https://github.com/MarkPhamm/Leetcode/tree/master/0359-logger-rate-limiter) |
| [0383-ransom-note](https://github.com/MarkPhamm/Leetcode/tree/master/0383-ransom-note) |
| [0387-first-unique-character-in-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0387-first-unique-character-in-a-string) |
| [0389-find-the-difference](https://github.com/MarkPhamm/Leetcode/tree/master/0389-find-the-difference) |
| [0424-longest-repeating-character-replacement](https://github.com/MarkPhamm/Leetcode/tree/master/0424-longest-repeating-character-replacement) |
| [0438-find-all-anagrams-in-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0438-find-all-anagrams-in-a-string) |
| [0496-next-greater-element-i](https://github.com/MarkPhamm/Leetcode/tree/master/0496-next-greater-element-i) |
| [0560-subarray-sum-equals-k](https://github.com/MarkPhamm/Leetcode/tree/master/0560-subarray-sum-equals-k) |
| [0645-set-mismatch](https://github.com/MarkPhamm/Leetcode/tree/master/0645-set-mismatch) |
| [0782-jewels-and-stones](https://github.com/MarkPhamm/Leetcode/tree/master/0782-jewels-and-stones) |
| [0888-fair-candy-swap](https://github.com/MarkPhamm/Leetcode/tree/master/0888-fair-candy-swap) |
| [1044-find-common-characters](https://github.com/MarkPhamm/Leetcode/tree/master/1044-find-common-characters) |
| [1098-largest-unique-number](https://github.com/MarkPhamm/Leetcode/tree/master/1098-largest-unique-number) |
| [1149-intersection-of-three-sorted-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/1149-intersection-of-three-sorted-arrays) |
| [1256-rank-transform-of-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/1256-rank-transform-of-an-array) |
| [1297-maximum-number-of-balloons](https://github.com/MarkPhamm/Leetcode/tree/master/1297-maximum-number-of-balloons) |
| [1391-counting-elements](https://github.com/MarkPhamm/Leetcode/tree/master/1391-counting-elements) |
| [1392-find-the-difference-of-two-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/1392-find-the-difference-of-two-arrays) |
| [1407-group-the-people-given-the-group-size-they-belong-to](https://github.com/MarkPhamm/Leetcode/tree/master/1407-group-the-people-given-the-group-size-they-belong-to) |
| [1460-number-of-substrings-containing-all-three-characters](https://github.com/MarkPhamm/Leetcode/tree/master/1460-number-of-substrings-containing-all-three-characters) |
| [1468-check-if-n-and-its-double-exist](https://github.com/MarkPhamm/Leetcode/tree/master/1468-check-if-n-and-its-double-exist) |
| [1500-count-largest-group](https://github.com/MarkPhamm/Leetcode/tree/master/1500-count-largest-group) |
| [1635-number-of-good-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/1635-number-of-good-pairs) |
| [1741-sort-array-by-increasing-frequency](https://github.com/MarkPhamm/Leetcode/tree/master/1741-sort-array-by-increasing-frequency) |
| [1848-sum-of-unique-elements](https://github.com/MarkPhamm/Leetcode/tree/master/1848-sum-of-unique-elements) |
| [1903-design-most-recently-used-queue](https://github.com/MarkPhamm/Leetcode/tree/master/1903-design-most-recently-used-queue) |
| [1915-check-if-one-string-swap-can-make-strings-equal](https://github.com/MarkPhamm/Leetcode/tree/master/1915-check-if-one-string-swap-can-make-strings-equal) |
| [2107-find-unique-binary-string](https://github.com/MarkPhamm/Leetcode/tree/master/2107-find-unique-binary-string) |
| [2163-kth-distinct-string-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/2163-kth-distinct-string-in-an-array) |
| [2190-count-common-words-with-one-occurrence](https://github.com/MarkPhamm/Leetcode/tree/master/2190-count-common-words-with-one-occurrence) |
| [2220-find-all-possible-recipes-from-given-supplies](https://github.com/MarkPhamm/Leetcode/tree/master/2220-find-all-possible-recipes-from-given-supplies) |
| [2308-divide-array-into-equal-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/2308-divide-array-into-equal-pairs) |
| [2525-count-number-of-distinct-integers-after-reverse-operations](https://github.com/MarkPhamm/Leetcode/tree/master/2525-count-number-of-distinct-integers-after-reverse-operations) |
| [2634-minimum-common-value](https://github.com/MarkPhamm/Leetcode/tree/master/2634-minimum-common-value) |
| [2640-maximum-number-of-integers-to-choose-from-a-range-i](https://github.com/MarkPhamm/Leetcode/tree/master/2640-maximum-number-of-integers-to-choose-from-a-range-i) |
| [2695-find-score-of-an-array-after-marking-all-elements](https://github.com/MarkPhamm/Leetcode/tree/master/2695-find-score-of-an-array-after-marking-all-elements) |
| [2707-merge-two-2d-arrays-by-summing-values](https://github.com/MarkPhamm/Leetcode/tree/master/2707-merge-two-2d-arrays-by-summing-values) |
| [2888-minimum-index-of-a-valid-split](https://github.com/MarkPhamm/Leetcode/tree/master/2888-minimum-index-of-a-valid-split) |
| [3267-find-longest-special-substring-that-occurs-thrice-i](https://github.com/MarkPhamm/Leetcode/tree/master/3267-find-longest-special-substring-that-occurs-thrice-i) |
| [3318-find-x-sum-of-all-k-long-subarrays-i](https://github.com/MarkPhamm/Leetcode/tree/master/3318-find-x-sum-of-all-k-long-subarrays-i) |
| [3349-maximum-length-substring-with-two-occurrences](https://github.com/MarkPhamm/Leetcode/tree/master/3349-maximum-length-substring-with-two-occurrences) |
| [3359-linked-list-frequency](https://github.com/MarkPhamm/Leetcode/tree/master/3359-linked-list-frequency) |
| [3446-find-the-number-of-good-pairs-i](https://github.com/MarkPhamm/Leetcode/tree/master/3446-find-the-number-of-good-pairs-i) |
| [3581-the-two-sneaky-numbers-of-digitville](https://github.com/MarkPhamm/Leetcode/tree/master/3581-the-two-sneaky-numbers-of-digitville) |
| [3594-identify-the-largest-outlier-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/3594-identify-the-largest-outlier-in-an-array) |
| [3610-find-x-sum-of-all-k-long-subarrays-i](https://github.com/MarkPhamm/Leetcode/tree/master/3610-find-x-sum-of-all-k-long-subarrays-i) |
| [3621-minimum-operations-to-make-array-values-equal-to-k](https://github.com/MarkPhamm/Leetcode/tree/master/3621-minimum-operations-to-make-array-values-equal-to-k) |
| [3656-minimum-number-of-operations-to-make-elements-in-array-distinct](https://github.com/MarkPhamm/Leetcode/tree/master/3656-minimum-number-of-operations-to-make-elements-in-array-distinct) |
## Two Pointers
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/MarkPhamm/Leetcode/tree/master/0005-longest-palindromic-substring) |
| [0011-container-with-most-water](https://github.com/MarkPhamm/Leetcode/tree/master/0011-container-with-most-water) |
| [0015-3sum](https://github.com/MarkPhamm/Leetcode/tree/master/0015-3sum) |
| [0018-4sum](https://github.com/MarkPhamm/Leetcode/tree/master/0018-4sum) |
| [0026-remove-duplicates-from-sorted-array](https://github.com/MarkPhamm/Leetcode/tree/master/0026-remove-duplicates-from-sorted-array) |
| [0027-remove-element](https://github.com/MarkPhamm/Leetcode/tree/master/0027-remove-element) |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
| [0042-trapping-rain-water](https://github.com/MarkPhamm/Leetcode/tree/master/0042-trapping-rain-water) |
| [0061-rotate-list](https://github.com/MarkPhamm/Leetcode/tree/master/0061-rotate-list) |
| [0080-remove-duplicates-from-sorted-array-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0080-remove-duplicates-from-sorted-array-ii) |
| [0082-remove-duplicates-from-sorted-list-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0082-remove-duplicates-from-sorted-list-ii) |
| [0088-merge-sorted-array](https://github.com/MarkPhamm/Leetcode/tree/master/0088-merge-sorted-array) |
| [0125-valid-palindrome](https://github.com/MarkPhamm/Leetcode/tree/master/0125-valid-palindrome) |
| [0141-linked-list-cycle](https://github.com/MarkPhamm/Leetcode/tree/master/0141-linked-list-cycle) |
| [0143-reorder-list](https://github.com/MarkPhamm/Leetcode/tree/master/0143-reorder-list) |
| [0167-two-sum-ii-input-array-is-sorted](https://github.com/MarkPhamm/Leetcode/tree/master/0167-two-sum-ii-input-array-is-sorted) |
| [0170-two-sum-iii-data-structure-design](https://github.com/MarkPhamm/Leetcode/tree/master/0170-two-sum-iii-data-structure-design) |
| [0234-palindrome-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/0234-palindrome-linked-list) |
| [0259-3sum-smaller](https://github.com/MarkPhamm/Leetcode/tree/master/0259-3sum-smaller) |
| [0283-move-zeroes](https://github.com/MarkPhamm/Leetcode/tree/master/0283-move-zeroes) |
| [0295-find-median-from-data-stream](https://github.com/MarkPhamm/Leetcode/tree/master/0295-find-median-from-data-stream) |
| [0344-reverse-string](https://github.com/MarkPhamm/Leetcode/tree/master/0344-reverse-string) |
| [0345-reverse-vowels-of-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0345-reverse-vowels-of-a-string) |
| [0349-intersection-of-two-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/0349-intersection-of-two-arrays) |
| [0350-intersection-of-two-arrays-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0350-intersection-of-two-arrays-ii) |
| [0392-is-subsequence](https://github.com/MarkPhamm/Leetcode/tree/master/0392-is-subsequence) |
| [0633-sum-of-square-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0633-sum-of-square-numbers) |
| [0874-backspace-string-compare](https://github.com/MarkPhamm/Leetcode/tree/master/0874-backspace-string-compare) |
| [0908-middle-of-the-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/0908-middle-of-the-linked-list) |
| [1019-squares-of-a-sorted-array](https://github.com/MarkPhamm/Leetcode/tree/master/1019-squares-of-a-sorted-array) |
| [1083-two-sum-less-than-k](https://github.com/MarkPhamm/Leetcode/tree/master/1083-two-sum-less-than-k) |
| [1468-check-if-n-and-its-double-exist](https://github.com/MarkPhamm/Leetcode/tree/master/1468-check-if-n-and-its-double-exist) |
| [1894-merge-strings-alternately](https://github.com/MarkPhamm/Leetcode/tree/master/1894-merge-strings-alternately) |
| [2128-reverse-prefix-of-word](https://github.com/MarkPhamm/Leetcode/tree/master/2128-reverse-prefix-of-word) |
| [2216-delete-the-middle-node-of-a-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/2216-delete-the-middle-node-of-a-linked-list) |
| [2232-adding-spaces-to-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/2232-adding-spaces-to-a-string) |
| [2236-maximum-twin-sum-of-a-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/2236-maximum-twin-sum-of-a-linked-list) |
| [2392-successful-pairs-of-spells-and-potions](https://github.com/MarkPhamm/Leetcode/tree/master/2392-successful-pairs-of-spells-and-potions) |
| [2414-move-pieces-to-obtain-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/2414-move-pieces-to-obtain-a-string) |
| [2481-strictly-palindromic-number](https://github.com/MarkPhamm/Leetcode/tree/master/2481-strictly-palindromic-number) |
| [2634-minimum-common-value](https://github.com/MarkPhamm/Leetcode/tree/master/2634-minimum-common-value) |
| [2699-count-the-number-of-fair-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/2699-count-the-number-of-fair-pairs) |
| [2707-merge-two-2d-arrays-by-summing-values](https://github.com/MarkPhamm/Leetcode/tree/master/2707-merge-two-2d-arrays-by-summing-values) |
| [2917-count-pairs-whose-sum-is-less-than-target](https://github.com/MarkPhamm/Leetcode/tree/master/2917-count-pairs-whose-sum-is-less-than-target) |
| [3018-make-string-a-subsequence-using-cyclic-increments](https://github.com/MarkPhamm/Leetcode/tree/master/3018-make-string-a-subsequence-using-cyclic-increments) |
## Dynamic Programming
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/MarkPhamm/Leetcode/tree/master/0005-longest-palindromic-substring) |
| [0022-generate-parentheses](https://github.com/MarkPhamm/Leetcode/tree/master/0022-generate-parentheses) |
| [0042-trapping-rain-water](https://github.com/MarkPhamm/Leetcode/tree/master/0042-trapping-rain-water) |
| [0053-maximum-subarray](https://github.com/MarkPhamm/Leetcode/tree/master/0053-maximum-subarray) |
| [0070-climbing-stairs](https://github.com/MarkPhamm/Leetcode/tree/master/0070-climbing-stairs) |
| [0118-pascals-triangle](https://github.com/MarkPhamm/Leetcode/tree/master/0118-pascals-triangle) |
| [0119-pascals-triangle-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0119-pascals-triangle-ii) |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/MarkPhamm/Leetcode/tree/master/0121-best-time-to-buy-and-sell-stock) |
| [0392-is-subsequence](https://github.com/MarkPhamm/Leetcode/tree/master/0392-is-subsequence) |
| [0509-fibonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/0509-fibonacci-number) |
| [0746-min-cost-climbing-stairs](https://github.com/MarkPhamm/Leetcode/tree/master/0746-min-cost-climbing-stairs) |
| [1013-fibonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/1013-fibonacci-number) |
| [1137-n-th-tribonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/1137-n-th-tribonacci-number) |
| [1236-n-th-tribonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/1236-n-th-tribonacci-number) |
| [2164-two-best-non-overlapping-events](https://github.com/MarkPhamm/Leetcode/tree/master/2164-two-best-non-overlapping-events) |
## Sorting
|  |
| ------- |
| [0015-3sum](https://github.com/MarkPhamm/Leetcode/tree/master/0015-3sum) |
| [0018-4sum](https://github.com/MarkPhamm/Leetcode/tree/master/0018-4sum) |
| [0049-group-anagrams](https://github.com/MarkPhamm/Leetcode/tree/master/0049-group-anagrams) |
| [0056-merge-intervals](https://github.com/MarkPhamm/Leetcode/tree/master/0056-merge-intervals) |
| [0088-merge-sorted-array](https://github.com/MarkPhamm/Leetcode/tree/master/0088-merge-sorted-array) |
| [0169-majority-element](https://github.com/MarkPhamm/Leetcode/tree/master/0169-majority-element) |
| [0217-contains-duplicate](https://github.com/MarkPhamm/Leetcode/tree/master/0217-contains-duplicate) |
| [0242-valid-anagram](https://github.com/MarkPhamm/Leetcode/tree/master/0242-valid-anagram) |
| [0252-meeting-rooms](https://github.com/MarkPhamm/Leetcode/tree/master/0252-meeting-rooms) |
| [0259-3sum-smaller](https://github.com/MarkPhamm/Leetcode/tree/master/0259-3sum-smaller) |
| [0295-find-median-from-data-stream](https://github.com/MarkPhamm/Leetcode/tree/master/0295-find-median-from-data-stream) |
| [0347-top-k-frequent-elements](https://github.com/MarkPhamm/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [0349-intersection-of-two-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/0349-intersection-of-two-arrays) |
| [0350-intersection-of-two-arrays-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0350-intersection-of-two-arrays-ii) |
| [0389-find-the-difference](https://github.com/MarkPhamm/Leetcode/tree/master/0389-find-the-difference) |
| [0414-third-maximum-number](https://github.com/MarkPhamm/Leetcode/tree/master/0414-third-maximum-number) |
| [0628-maximum-product-of-three-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0628-maximum-product-of-three-numbers) |
| [0645-set-mismatch](https://github.com/MarkPhamm/Leetcode/tree/master/0645-set-mismatch) |
| [0748-largest-number-at-least-twice-of-others](https://github.com/MarkPhamm/Leetcode/tree/master/0748-largest-number-at-least-twice-of-others) |
| [0888-fair-candy-swap](https://github.com/MarkPhamm/Leetcode/tree/master/0888-fair-candy-swap) |
| [0987-reveal-cards-in-increasing-order](https://github.com/MarkPhamm/Leetcode/tree/master/0987-reveal-cards-in-increasing-order) |
| [1019-squares-of-a-sorted-array](https://github.com/MarkPhamm/Leetcode/tree/master/1019-squares-of-a-sorted-array) |
| [1083-two-sum-less-than-k](https://github.com/MarkPhamm/Leetcode/tree/master/1083-two-sum-less-than-k) |
| [1098-largest-unique-number](https://github.com/MarkPhamm/Leetcode/tree/master/1098-largest-unique-number) |
| [1256-rank-transform-of-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/1256-rank-transform-of-an-array) |
| [1306-minimum-absolute-difference](https://github.com/MarkPhamm/Leetcode/tree/master/1306-minimum-absolute-difference) |
| [1468-check-if-n-and-its-double-exist](https://github.com/MarkPhamm/Leetcode/tree/master/1468-check-if-n-and-its-double-exist) |
| [1741-sort-array-by-increasing-frequency](https://github.com/MarkPhamm/Leetcode/tree/master/1741-sort-array-by-increasing-frequency) |
| [2160-minimum-operations-to-make-a-uni-value-grid](https://github.com/MarkPhamm/Leetcode/tree/master/2160-minimum-operations-to-make-a-uni-value-grid) |
| [2164-two-best-non-overlapping-events](https://github.com/MarkPhamm/Leetcode/tree/master/2164-two-best-non-overlapping-events) |
| [2210-find-target-indices-after-sorting-array](https://github.com/MarkPhamm/Leetcode/tree/master/2210-find-target-indices-after-sorting-array) |
| [2392-successful-pairs-of-spells-and-potions](https://github.com/MarkPhamm/Leetcode/tree/master/2392-successful-pairs-of-spells-and-potions) |
| [2640-maximum-number-of-integers-to-choose-from-a-range-i](https://github.com/MarkPhamm/Leetcode/tree/master/2640-maximum-number-of-integers-to-choose-from-a-range-i) |
| [2695-find-score-of-an-array-after-marking-all-elements](https://github.com/MarkPhamm/Leetcode/tree/master/2695-find-score-of-an-array-after-marking-all-elements) |
| [2699-count-the-number-of-fair-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/2699-count-the-number-of-fair-pairs) |
| [2888-minimum-index-of-a-valid-split](https://github.com/MarkPhamm/Leetcode/tree/master/2888-minimum-index-of-a-valid-split) |
| [2891-maximum-beauty-of-an-array-after-applying-operation](https://github.com/MarkPhamm/Leetcode/tree/master/2891-maximum-beauty-of-an-array-after-applying-operation) |
| [2917-count-pairs-whose-sum-is-less-than-target](https://github.com/MarkPhamm/Leetcode/tree/master/2917-count-pairs-whose-sum-is-less-than-target) |
| [3334-apple-redistribution-into-boxes](https://github.com/MarkPhamm/Leetcode/tree/master/3334-apple-redistribution-into-boxes) |
## Counting
|  |
| ------- |
| [0169-majority-element](https://github.com/MarkPhamm/Leetcode/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/MarkPhamm/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [0383-ransom-note](https://github.com/MarkPhamm/Leetcode/tree/master/0383-ransom-note) |
| [0387-first-unique-character-in-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0387-first-unique-character-in-a-string) |
| [1149-intersection-of-three-sorted-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/1149-intersection-of-three-sorted-arrays) |
| [1297-maximum-number-of-balloons](https://github.com/MarkPhamm/Leetcode/tree/master/1297-maximum-number-of-balloons) |
| [1635-number-of-good-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/1635-number-of-good-pairs) |
| [1848-sum-of-unique-elements](https://github.com/MarkPhamm/Leetcode/tree/master/1848-sum-of-unique-elements) |
| [1915-check-if-one-string-swap-can-make-strings-equal](https://github.com/MarkPhamm/Leetcode/tree/master/1915-check-if-one-string-swap-can-make-strings-equal) |
| [2163-kth-distinct-string-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/2163-kth-distinct-string-in-an-array) |
| [2190-count-common-words-with-one-occurrence](https://github.com/MarkPhamm/Leetcode/tree/master/2190-count-common-words-with-one-occurrence) |
| [2308-divide-array-into-equal-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/2308-divide-array-into-equal-pairs) |
| [2525-count-number-of-distinct-integers-after-reverse-operations](https://github.com/MarkPhamm/Leetcode/tree/master/2525-count-number-of-distinct-integers-after-reverse-operations) |
| [2614-maximum-count-of-positive-integer-and-negative-integer](https://github.com/MarkPhamm/Leetcode/tree/master/2614-maximum-count-of-positive-integer-and-negative-integer) |
| [3267-find-longest-special-substring-that-occurs-thrice-i](https://github.com/MarkPhamm/Leetcode/tree/master/3267-find-longest-special-substring-that-occurs-thrice-i) |
| [3359-linked-list-frequency](https://github.com/MarkPhamm/Leetcode/tree/master/3359-linked-list-frequency) |
| [3594-identify-the-largest-outlier-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/3594-identify-the-largest-outlier-in-an-array) |
## Stack
|  |
| ------- |
| [0020-valid-parentheses](https://github.com/MarkPhamm/Leetcode/tree/master/0020-valid-parentheses) |
| [0042-trapping-rain-water](https://github.com/MarkPhamm/Leetcode/tree/master/0042-trapping-rain-water) |
| [0143-reorder-list](https://github.com/MarkPhamm/Leetcode/tree/master/0143-reorder-list) |
| [0155-min-stack](https://github.com/MarkPhamm/Leetcode/tree/master/0155-min-stack) |
| [0225-implement-stack-using-queues](https://github.com/MarkPhamm/Leetcode/tree/master/0225-implement-stack-using-queues) |
| [0232-implement-queue-using-stacks](https://github.com/MarkPhamm/Leetcode/tree/master/0232-implement-queue-using-stacks) |
| [0234-palindrome-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/0234-palindrome-linked-list) |
| [0496-next-greater-element-i](https://github.com/MarkPhamm/Leetcode/tree/master/0496-next-greater-element-i) |
| [0682-baseball-game](https://github.com/MarkPhamm/Leetcode/tree/master/0682-baseball-game) |
| [0735-asteroid-collision](https://github.com/MarkPhamm/Leetcode/tree/master/0735-asteroid-collision) |
| [0874-backspace-string-compare](https://github.com/MarkPhamm/Leetcode/tree/master/0874-backspace-string-compare) |
| [1128-remove-all-adjacent-duplicates-in-string](https://github.com/MarkPhamm/Leetcode/tree/master/1128-remove-all-adjacent-duplicates-in-string) |
| [1570-final-prices-with-a-special-discount-in-a-shop](https://github.com/MarkPhamm/Leetcode/tree/master/1570-final-prices-with-a-special-discount-in-a-shop) |
| [1666-make-the-string-great](https://github.com/MarkPhamm/Leetcode/tree/master/1666-make-the-string-great) |
| [1720-crawler-log-folder](https://github.com/MarkPhamm/Leetcode/tree/master/1720-crawler-log-folder) |
| [1737-maximum-nesting-depth-of-the-parentheses](https://github.com/MarkPhamm/Leetcode/tree/master/1737-maximum-nesting-depth-of-the-parentheses) |
| [1903-design-most-recently-used-queue](https://github.com/MarkPhamm/Leetcode/tree/master/1903-design-most-recently-used-queue) |
| [2021-remove-all-occurrences-of-a-substring](https://github.com/MarkPhamm/Leetcode/tree/master/2021-remove-all-occurrences-of-a-substring) |
| [2128-reverse-prefix-of-word](https://github.com/MarkPhamm/Leetcode/tree/master/2128-reverse-prefix-of-word) |
| [2236-maximum-twin-sum-of-a-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/2236-maximum-twin-sum-of-a-linked-list) |
| [2456-construct-smallest-number-from-di-string](https://github.com/MarkPhamm/Leetcode/tree/master/2456-construct-smallest-number-from-di-string) |
| [2470-removing-stars-from-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/2470-removing-stars-from-a-string) |
| [2800-minimum-string-length-after-removing-substrings](https://github.com/MarkPhamm/Leetcode/tree/master/2800-minimum-string-length-after-removing-substrings) |
| [3447-clear-digits](https://github.com/MarkPhamm/Leetcode/tree/master/3447-clear-digits) |
## String Matching
|  |
| ------- |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
| [0812-rotate-string](https://github.com/MarkPhamm/Leetcode/tree/master/0812-rotate-string) |
| [1524-string-matching-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/1524-string-matching-in-an-array) |
| [2292-counting-words-with-a-given-prefix](https://github.com/MarkPhamm/Leetcode/tree/master/2292-counting-words-with-a-given-prefix) |
## Trie
|  |
| ------- |
| [0014-longest-common-prefix](https://github.com/MarkPhamm/Leetcode/tree/master/0014-longest-common-prefix) |
## Binary Search
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/0004-median-of-two-sorted-arrays) |
| [0035-search-insert-position](https://github.com/MarkPhamm/Leetcode/tree/master/0035-search-insert-position) |
| [0069-sqrtx](https://github.com/MarkPhamm/Leetcode/tree/master/0069-sqrtx) |
| [0074-search-a-2d-matrix](https://github.com/MarkPhamm/Leetcode/tree/master/0074-search-a-2d-matrix) |
| [0162-find-peak-element](https://github.com/MarkPhamm/Leetcode/tree/master/0162-find-peak-element) |
| [0167-two-sum-ii-input-array-is-sorted](https://github.com/MarkPhamm/Leetcode/tree/master/0167-two-sum-ii-input-array-is-sorted) |
| [0209-minimum-size-subarray-sum](https://github.com/MarkPhamm/Leetcode/tree/master/0209-minimum-size-subarray-sum) |
| [0259-3sum-smaller](https://github.com/MarkPhamm/Leetcode/tree/master/0259-3sum-smaller) |
| [0278-first-bad-version](https://github.com/MarkPhamm/Leetcode/tree/master/0278-first-bad-version) |
| [0349-intersection-of-two-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/0349-intersection-of-two-arrays) |
| [0350-intersection-of-two-arrays-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0350-intersection-of-two-arrays-ii) |
| [0367-valid-perfect-square](https://github.com/MarkPhamm/Leetcode/tree/master/0367-valid-perfect-square) |
| [0633-sum-of-square-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0633-sum-of-square-numbers) |
| [0792-binary-search](https://github.com/MarkPhamm/Leetcode/tree/master/0792-binary-search) |
| [0888-fair-candy-swap](https://github.com/MarkPhamm/Leetcode/tree/master/0888-fair-candy-swap) |
| [0907-koko-eating-bananas](https://github.com/MarkPhamm/Leetcode/tree/master/0907-koko-eating-bananas) |
| [1066-fixed-point](https://github.com/MarkPhamm/Leetcode/tree/master/1066-fixed-point) |
| [1083-two-sum-less-than-k](https://github.com/MarkPhamm/Leetcode/tree/master/1083-two-sum-less-than-k) |
| [1102-check-if-a-number-is-majority-element-in-a-sorted-array](https://github.com/MarkPhamm/Leetcode/tree/master/1102-check-if-a-number-is-majority-element-in-a-sorted-array) |
| [1149-intersection-of-three-sorted-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/1149-intersection-of-three-sorted-arrays) |
| [1468-check-if-n-and-its-double-exist](https://github.com/MarkPhamm/Leetcode/tree/master/1468-check-if-n-and-its-double-exist) |
| [1476-count-negative-numbers-in-a-sorted-matrix](https://github.com/MarkPhamm/Leetcode/tree/master/1476-count-negative-numbers-in-a-sorted-matrix) |
| [1646-kth-missing-positive-number](https://github.com/MarkPhamm/Leetcode/tree/master/1646-kth-missing-positive-number) |
| [1886-minimum-limit-of-balls-in-a-bag](https://github.com/MarkPhamm/Leetcode/tree/master/1886-minimum-limit-of-balls-in-a-bag) |
| [2164-two-best-non-overlapping-events](https://github.com/MarkPhamm/Leetcode/tree/master/2164-two-best-non-overlapping-events) |
| [2210-find-target-indices-after-sorting-array](https://github.com/MarkPhamm/Leetcode/tree/master/2210-find-target-indices-after-sorting-array) |
| [2392-successful-pairs-of-spells-and-potions](https://github.com/MarkPhamm/Leetcode/tree/master/2392-successful-pairs-of-spells-and-potions) |
| [2614-maximum-count-of-positive-integer-and-negative-integer](https://github.com/MarkPhamm/Leetcode/tree/master/2614-maximum-count-of-positive-integer-and-negative-integer) |
| [2634-minimum-common-value](https://github.com/MarkPhamm/Leetcode/tree/master/2634-minimum-common-value) |
| [2640-maximum-number-of-integers-to-choose-from-a-range-i](https://github.com/MarkPhamm/Leetcode/tree/master/2640-maximum-number-of-integers-to-choose-from-a-range-i) |
| [2699-count-the-number-of-fair-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/2699-count-the-number-of-fair-pairs) |
| [2891-maximum-beauty-of-an-array-after-applying-operation](https://github.com/MarkPhamm/Leetcode/tree/master/2891-maximum-beauty-of-an-array-after-applying-operation) |
| [2917-count-pairs-whose-sum-is-less-than-target](https://github.com/MarkPhamm/Leetcode/tree/master/2917-count-pairs-whose-sum-is-less-than-target) |
| [3267-find-longest-special-substring-that-occurs-thrice-i](https://github.com/MarkPhamm/Leetcode/tree/master/3267-find-longest-special-substring-that-occurs-thrice-i) |
| [3427-special-array-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3427-special-array-ii) |
## Memoization
|  |
| ------- |
| [0070-climbing-stairs](https://github.com/MarkPhamm/Leetcode/tree/master/0070-climbing-stairs) |
| [0509-fibonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/0509-fibonacci-number) |
| [1013-fibonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/1013-fibonacci-number) |
| [1137-n-th-tribonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/1137-n-th-tribonacci-number) |
| [1236-n-th-tribonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/1236-n-th-tribonacci-number) |
## Recursion
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0002-add-two-numbers) |
| [0021-merge-two-sorted-lists](https://github.com/MarkPhamm/Leetcode/tree/master/0021-merge-two-sorted-lists) |
| [0024-swap-nodes-in-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/0024-swap-nodes-in-pairs) |
| [0143-reorder-list](https://github.com/MarkPhamm/Leetcode/tree/master/0143-reorder-list) |
| [0206-reverse-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/0206-reverse-linked-list) |
| [0234-palindrome-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/0234-palindrome-linked-list) |
| [0326-power-of-three](https://github.com/MarkPhamm/Leetcode/tree/master/0326-power-of-three) |
| [0509-fibonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/0509-fibonacci-number) |
| [1013-fibonacci-number](https://github.com/MarkPhamm/Leetcode/tree/master/1013-fibonacci-number) |
## Interactive
|  |
| ------- |
| [0278-first-bad-version](https://github.com/MarkPhamm/Leetcode/tree/master/0278-first-bad-version) |
## Divide and Conquer
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/MarkPhamm/Leetcode/tree/master/0004-median-of-two-sorted-arrays) |
| [0023-merge-k-sorted-lists](https://github.com/MarkPhamm/Leetcode/tree/master/0023-merge-k-sorted-lists) |
| [0053-maximum-subarray](https://github.com/MarkPhamm/Leetcode/tree/master/0053-maximum-subarray) |
| [0169-majority-element](https://github.com/MarkPhamm/Leetcode/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/MarkPhamm/Leetcode/tree/master/0347-top-k-frequent-elements) |
## Heap (Priority Queue)
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/MarkPhamm/Leetcode/tree/master/0023-merge-k-sorted-lists) |
| [0295-find-median-from-data-stream](https://github.com/MarkPhamm/Leetcode/tree/master/0295-find-median-from-data-stream) |
| [0347-top-k-frequent-elements](https://github.com/MarkPhamm/Leetcode/tree/master/0347-top-k-frequent-elements) |
| [1917-maximum-average-pass-ratio](https://github.com/MarkPhamm/Leetcode/tree/master/1917-maximum-average-pass-ratio) |
| [2164-two-best-non-overlapping-events](https://github.com/MarkPhamm/Leetcode/tree/master/2164-two-best-non-overlapping-events) |
| [2692-take-gifts-from-the-richest-pile](https://github.com/MarkPhamm/Leetcode/tree/master/2692-take-gifts-from-the-richest-pile) |
| [2695-find-score-of-an-array-after-marking-all-elements](https://github.com/MarkPhamm/Leetcode/tree/master/2695-find-score-of-an-array-after-marking-all-elements) |
| [2868-continuous-subarrays](https://github.com/MarkPhamm/Leetcode/tree/master/2868-continuous-subarrays) |
| [3318-find-x-sum-of-all-k-long-subarrays-i](https://github.com/MarkPhamm/Leetcode/tree/master/3318-find-x-sum-of-all-k-long-subarrays-i) |
| [3610-find-x-sum-of-all-k-long-subarrays-i](https://github.com/MarkPhamm/Leetcode/tree/master/3610-find-x-sum-of-all-k-long-subarrays-i) |
## Bucket Sort
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/MarkPhamm/Leetcode/tree/master/0347-top-k-frequent-elements) |
## Quickselect
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/MarkPhamm/Leetcode/tree/master/0347-top-k-frequent-elements) |
## Design
|  |
| ------- |
| [0146-lru-cache](https://github.com/MarkPhamm/Leetcode/tree/master/0146-lru-cache) |
| [0155-min-stack](https://github.com/MarkPhamm/Leetcode/tree/master/0155-min-stack) |
| [0170-two-sum-iii-data-structure-design](https://github.com/MarkPhamm/Leetcode/tree/master/0170-two-sum-iii-data-structure-design) |
| [0225-implement-stack-using-queues](https://github.com/MarkPhamm/Leetcode/tree/master/0225-implement-stack-using-queues) |
| [0232-implement-queue-using-stacks](https://github.com/MarkPhamm/Leetcode/tree/master/0232-implement-queue-using-stacks) |
| [0295-find-median-from-data-stream](https://github.com/MarkPhamm/Leetcode/tree/master/0295-find-median-from-data-stream) |
| [0303-range-sum-query-immutable](https://github.com/MarkPhamm/Leetcode/tree/master/0303-range-sum-query-immutable) |
| [0346-moving-average-from-data-stream](https://github.com/MarkPhamm/Leetcode/tree/master/0346-moving-average-from-data-stream) |
| [0359-logger-rate-limiter](https://github.com/MarkPhamm/Leetcode/tree/master/0359-logger-rate-limiter) |
| [0969-number-of-recent-calls](https://github.com/MarkPhamm/Leetcode/tree/master/0969-number-of-recent-calls) |
| [1477-product-of-the-last-k-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/1477-product-of-the-last-k-numbers) |
| [1903-design-most-recently-used-queue](https://github.com/MarkPhamm/Leetcode/tree/master/1903-design-most-recently-used-queue) |
## Matrix
|  |
| ------- |
| [0074-search-a-2d-matrix](https://github.com/MarkPhamm/Leetcode/tree/master/0074-search-a-2d-matrix) |
| [1476-count-negative-numbers-in-a-sorted-matrix](https://github.com/MarkPhamm/Leetcode/tree/master/1476-count-negative-numbers-in-a-sorted-matrix) |
| [2132-convert-1d-array-into-2d-array](https://github.com/MarkPhamm/Leetcode/tree/master/2132-convert-1d-array-into-2d-array) |
| [2160-minimum-operations-to-make-a-uni-value-grid](https://github.com/MarkPhamm/Leetcode/tree/master/2160-minimum-operations-to-make-a-uni-value-grid) |
## Greedy
|  |
| ------- |
| [0011-container-with-most-water](https://github.com/MarkPhamm/Leetcode/tree/master/0011-container-with-most-water) |
| [0605-can-place-flowers](https://github.com/MarkPhamm/Leetcode/tree/master/0605-can-place-flowers) |
| [1407-group-the-people-given-the-group-size-they-belong-to](https://github.com/MarkPhamm/Leetcode/tree/master/1407-group-the-people-given-the-group-size-they-belong-to) |
| [1448-maximum-69-number](https://github.com/MarkPhamm/Leetcode/tree/master/1448-maximum-69-number) |
| [1917-maximum-average-pass-ratio](https://github.com/MarkPhamm/Leetcode/tree/master/1917-maximum-average-pass-ratio) |
| [2456-construct-smallest-number-from-di-string](https://github.com/MarkPhamm/Leetcode/tree/master/2456-construct-smallest-number-from-di-string) |
| [2640-maximum-number-of-integers-to-choose-from-a-range-i](https://github.com/MarkPhamm/Leetcode/tree/master/2640-maximum-number-of-integers-to-choose-from-a-range-i) |
| [3334-apple-redistribution-into-boxes](https://github.com/MarkPhamm/Leetcode/tree/master/3334-apple-redistribution-into-boxes) |
## Linked List
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/0002-add-two-numbers) |
| [0021-merge-two-sorted-lists](https://github.com/MarkPhamm/Leetcode/tree/master/0021-merge-two-sorted-lists) |
| [0023-merge-k-sorted-lists](https://github.com/MarkPhamm/Leetcode/tree/master/0023-merge-k-sorted-lists) |
| [0024-swap-nodes-in-pairs](https://github.com/MarkPhamm/Leetcode/tree/master/0024-swap-nodes-in-pairs) |
| [0061-rotate-list](https://github.com/MarkPhamm/Leetcode/tree/master/0061-rotate-list) |
| [0082-remove-duplicates-from-sorted-list-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0082-remove-duplicates-from-sorted-list-ii) |
| [0083-remove-duplicates-from-sorted-list](https://github.com/MarkPhamm/Leetcode/tree/master/0083-remove-duplicates-from-sorted-list) |
| [0141-linked-list-cycle](https://github.com/MarkPhamm/Leetcode/tree/master/0141-linked-list-cycle) |
| [0143-reorder-list](https://github.com/MarkPhamm/Leetcode/tree/master/0143-reorder-list) |
| [0146-lru-cache](https://github.com/MarkPhamm/Leetcode/tree/master/0146-lru-cache) |
| [0206-reverse-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/0206-reverse-linked-list) |
| [0234-palindrome-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/0234-palindrome-linked-list) |
| [0237-delete-node-in-a-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/0237-delete-node-in-a-linked-list) |
| [0328-odd-even-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/0328-odd-even-linked-list) |
| [0908-middle-of-the-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/0908-middle-of-the-linked-list) |
| [1411-convert-binary-number-in-a-linked-list-to-integer](https://github.com/MarkPhamm/Leetcode/tree/master/1411-convert-binary-number-in-a-linked-list-to-integer) |
| [1765-merge-in-between-linked-lists](https://github.com/MarkPhamm/Leetcode/tree/master/1765-merge-in-between-linked-lists) |
| [2216-delete-the-middle-node-of-a-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/2216-delete-the-middle-node-of-a-linked-list) |
| [2236-maximum-twin-sum-of-a-linked-list](https://github.com/MarkPhamm/Leetcode/tree/master/2236-maximum-twin-sum-of-a-linked-list) |
| [3359-linked-list-frequency](https://github.com/MarkPhamm/Leetcode/tree/master/3359-linked-list-frequency) |
| [3577-convert-doubly-linked-list-to-array-i](https://github.com/MarkPhamm/Leetcode/tree/master/3577-convert-doubly-linked-list-to-array-i) |
| [3615-convert-doubly-linked-list-to-array-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3615-convert-doubly-linked-list-to-array-ii) |
## Brainteaser
|  |
| ------- |
| [2481-strictly-palindromic-number](https://github.com/MarkPhamm/Leetcode/tree/master/2481-strictly-palindromic-number) |
## Doubly-Linked List
|  |
| ------- |
| [0146-lru-cache](https://github.com/MarkPhamm/Leetcode/tree/master/0146-lru-cache) |
| [3577-convert-doubly-linked-list-to-array-i](https://github.com/MarkPhamm/Leetcode/tree/master/3577-convert-doubly-linked-list-to-array-i) |
| [3615-convert-doubly-linked-list-to-array-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3615-convert-doubly-linked-list-to-array-ii) |
## Number Theory
|  |
| ------- |
| [1585-the-kth-factor-of-n](https://github.com/MarkPhamm/Leetcode/tree/master/1585-the-kth-factor-of-n) |
## Data Stream
|  |
| ------- |
| [0170-two-sum-iii-data-structure-design](https://github.com/MarkPhamm/Leetcode/tree/master/0170-two-sum-iii-data-structure-design) |
| [0295-find-median-from-data-stream](https://github.com/MarkPhamm/Leetcode/tree/master/0295-find-median-from-data-stream) |
| [0346-moving-average-from-data-stream](https://github.com/MarkPhamm/Leetcode/tree/master/0346-moving-average-from-data-stream) |
| [0359-logger-rate-limiter](https://github.com/MarkPhamm/Leetcode/tree/master/0359-logger-rate-limiter) |
| [0969-number-of-recent-calls](https://github.com/MarkPhamm/Leetcode/tree/master/0969-number-of-recent-calls) |
| [1477-product-of-the-last-k-numbers](https://github.com/MarkPhamm/Leetcode/tree/master/1477-product-of-the-last-k-numbers) |
## Queue
|  |
| ------- |
| [0225-implement-stack-using-queues](https://github.com/MarkPhamm/Leetcode/tree/master/0225-implement-stack-using-queues) |
| [0232-implement-queue-using-stacks](https://github.com/MarkPhamm/Leetcode/tree/master/0232-implement-queue-using-stacks) |
| [0346-moving-average-from-data-stream](https://github.com/MarkPhamm/Leetcode/tree/master/0346-moving-average-from-data-stream) |
| [0387-first-unique-character-in-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0387-first-unique-character-in-a-string) |
| [0969-number-of-recent-calls](https://github.com/MarkPhamm/Leetcode/tree/master/0969-number-of-recent-calls) |
| [0987-reveal-cards-in-increasing-order](https://github.com/MarkPhamm/Leetcode/tree/master/0987-reveal-cards-in-increasing-order) |
| [2195-time-needed-to-buy-tickets](https://github.com/MarkPhamm/Leetcode/tree/master/2195-time-needed-to-buy-tickets) |
| [2868-continuous-subarrays](https://github.com/MarkPhamm/Leetcode/tree/master/2868-continuous-subarrays) |
## Enumeration
|  |
| ------- |
| [1656-count-good-triplets](https://github.com/MarkPhamm/Leetcode/tree/master/1656-count-good-triplets) |
| [2998-count-symmetric-integers](https://github.com/MarkPhamm/Leetcode/tree/master/2998-count-symmetric-integers) |
| [3594-identify-the-largest-outlier-in-an-array](https://github.com/MarkPhamm/Leetcode/tree/master/3594-identify-the-largest-outlier-in-an-array) |
## Sliding Window
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/MarkPhamm/Leetcode/tree/master/0003-longest-substring-without-repeating-characters) |
| [0209-minimum-size-subarray-sum](https://github.com/MarkPhamm/Leetcode/tree/master/0209-minimum-size-subarray-sum) |
| [0219-contains-duplicate-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0219-contains-duplicate-ii) |
| [0424-longest-repeating-character-replacement](https://github.com/MarkPhamm/Leetcode/tree/master/0424-longest-repeating-character-replacement) |
| [0438-find-all-anagrams-in-a-string](https://github.com/MarkPhamm/Leetcode/tree/master/0438-find-all-anagrams-in-a-string) |
| [1460-number-of-substrings-containing-all-three-characters](https://github.com/MarkPhamm/Leetcode/tree/master/1460-number-of-substrings-containing-all-three-characters) |
| [2211-k-radius-subarray-averages](https://github.com/MarkPhamm/Leetcode/tree/master/2211-k-radius-subarray-averages) |
| [2463-minimum-recolors-to-get-k-consecutive-black-blocks](https://github.com/MarkPhamm/Leetcode/tree/master/2463-minimum-recolors-to-get-k-consecutive-black-blocks) |
| [2868-continuous-subarrays](https://github.com/MarkPhamm/Leetcode/tree/master/2868-continuous-subarrays) |
| [2891-maximum-beauty-of-an-array-after-applying-operation](https://github.com/MarkPhamm/Leetcode/tree/master/2891-maximum-beauty-of-an-array-after-applying-operation) |
| [3267-find-longest-special-substring-that-occurs-thrice-i](https://github.com/MarkPhamm/Leetcode/tree/master/3267-find-longest-special-substring-that-occurs-thrice-i) |
| [3318-find-x-sum-of-all-k-long-subarrays-i](https://github.com/MarkPhamm/Leetcode/tree/master/3318-find-x-sum-of-all-k-long-subarrays-i) |
| [3349-maximum-length-substring-with-two-occurrences](https://github.com/MarkPhamm/Leetcode/tree/master/3349-maximum-length-substring-with-two-occurrences) |
| [3463-alternating-groups-i](https://github.com/MarkPhamm/Leetcode/tree/master/3463-alternating-groups-i) |
| [3483-alternating-groups-ii](https://github.com/MarkPhamm/Leetcode/tree/master/3483-alternating-groups-ii) |
| [3543-count-substrings-that-satisfy-k-constraint-i](https://github.com/MarkPhamm/Leetcode/tree/master/3543-count-substrings-that-satisfy-k-constraint-i) |
| [3610-find-x-sum-of-all-k-long-subarrays-i](https://github.com/MarkPhamm/Leetcode/tree/master/3610-find-x-sum-of-all-k-long-subarrays-i) |
| [3644-minimum-positive-sum-subarray](https://github.com/MarkPhamm/Leetcode/tree/master/3644-minimum-positive-sum-subarray) |
## Ordered Set
|  |
| ------- |
| [1903-design-most-recently-used-queue](https://github.com/MarkPhamm/Leetcode/tree/master/1903-design-most-recently-used-queue) |
| [2868-continuous-subarrays](https://github.com/MarkPhamm/Leetcode/tree/master/2868-continuous-subarrays) |
## Monotonic Queue
|  |
| ------- |
| [2868-continuous-subarrays](https://github.com/MarkPhamm/Leetcode/tree/master/2868-continuous-subarrays) |
## Binary Indexed Tree
|  |
| ------- |
| [1903-design-most-recently-used-queue](https://github.com/MarkPhamm/Leetcode/tree/master/1903-design-most-recently-used-queue) |
## Backtracking
|  |
| ------- |
| [0017-letter-combinations-of-a-phone-number](https://github.com/MarkPhamm/Leetcode/tree/master/0017-letter-combinations-of-a-phone-number) |
| [0022-generate-parentheses](https://github.com/MarkPhamm/Leetcode/tree/master/0022-generate-parentheses) |
| [0039-combination-sum](https://github.com/MarkPhamm/Leetcode/tree/master/0039-combination-sum) |
| [0078-subsets](https://github.com/MarkPhamm/Leetcode/tree/master/0078-subsets) |
| [0090-subsets-ii](https://github.com/MarkPhamm/Leetcode/tree/master/0090-subsets-ii) |
| [0216-combination-sum-iii](https://github.com/MarkPhamm/Leetcode/tree/master/0216-combination-sum-iii) |
| [2107-find-unique-binary-string](https://github.com/MarkPhamm/Leetcode/tree/master/2107-find-unique-binary-string) |
| [2456-construct-smallest-number-from-di-string](https://github.com/MarkPhamm/Leetcode/tree/master/2456-construct-smallest-number-from-di-string) |
## Graph
|  |
| ------- |
| [2220-find-all-possible-recipes-from-given-supplies](https://github.com/MarkPhamm/Leetcode/tree/master/2220-find-all-possible-recipes-from-given-supplies) |
## Topological Sort
|  |
| ------- |
| [2220-find-all-possible-recipes-from-given-supplies](https://github.com/MarkPhamm/Leetcode/tree/master/2220-find-all-possible-recipes-from-given-supplies) |
## Monotonic Stack
|  |
| ------- |
| [0042-trapping-rain-water](https://github.com/MarkPhamm/Leetcode/tree/master/0042-trapping-rain-water) |
| [0496-next-greater-element-i](https://github.com/MarkPhamm/Leetcode/tree/master/0496-next-greater-element-i) |
| [1570-final-prices-with-a-special-discount-in-a-shop](https://github.com/MarkPhamm/Leetcode/tree/master/1570-final-prices-with-a-special-discount-in-a-shop) |
## Union-Find
|  |
| ------- |
| [0128-longest-consecutive-sequence](https://github.com/MarkPhamm/Leetcode/tree/master/0128-longest-consecutive-sequence) |
## Merge Sort
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/MarkPhamm/Leetcode/tree/master/0023-merge-k-sorted-lists) |
<!---LeetCode Topics End-->
