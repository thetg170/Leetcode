# Roadmap 28 tuần · Python, thiết kế phần mềm và Data Engineering IoT

**Nhịp học** 60–90 phút mỗi ngày. Sáu buổi tiến độ và một buổi ôn nhẹ mỗi tuần. Dùng terminal, Neovim, deck **LeetCode** hiện có và AI ở vai trò reviewer.

| Tuần | Chặng | Sản phẩm hoặc năng lực cần kiểm chứng |
| --- | --- | --- |
| 1–15 | Tiếp cận đủ 150 bài NeetCode | Có lần thử cho 150 bài, biết dạng nào tự làm được và dạng nào cần ôn lại. |
| 16 | Củng cố | Giải lại bài từ các dạng khác nhau với bản nháp mới, bù bài bỏ sót và kiểm tra khả năng giải thích. |
| 17–21 | Project Python và thiết kế | Một CLI tổng hợp đơn hàng có test, đọc được hai nguồn, lưu SQLite và chịu được việc nhập lại dữ liệu. |
| 22–28 | Project DE IoT | Một pipeline telemetry có hợp đồng dữ liệu, xử lý trùng và đến muộn, chạy lại an toàn, và có runbook. |

**Mốc thời gian** 28 tuần là kế hoạch cơ sở, khoảng 6–7 tháng. Mốc 150 bài tính theo lần tiếp cận có ghi nhận. Khi hai tuần liên tiếp vượt quá 90 phút hoặc còn nhiều bài chưa thể giải thích, giảm số bài mới và dời lịch. Tuần 16 dành để bù và ôn.

## Nhịp học hằng ngày

| Thời gian | Bắt đầu | Tự làm | Kết thúc |
| --- | --- | --- | --- |
| 60 phút | 10 phút Anki | 40 phút code, vẽ luồng hoặc kiểm thử | 10 phút tự review, hỏi AI nếu cần và ghi kết quả |
| 90 phút | 15 phút Anki | 60 phút làm việc trên một hoặc hai mục tiêu | 15 phút review, chạy lại test và ghi kết quả |

- **Buổi có hai bài:** chọn một bài để code và kiểm thử kỹ. Bài còn lại có thể chỉ làm đến bước tự phân tích, viết pseudocode và xác định ca biên. Ghi riêng nếu chưa chạy được. Đừng kéo quá 90 phút để bù số lượng.
- **Buổi bài Hard:** dùng phần lớn thời gian cho một bài. Sau khoảng 20–25 phút tự làm, nếu kẹt thì hỏi AI một câu gợi ý. Sau khi xem gợi ý, đóng câu trả lời, tự viết lại cách nghĩ và lên lịch thử lại.
- **Buổi 7:** xử lý thẻ đến hạn, giải lại một bài chưa chắc hoặc bù một bài chưa thử. Cuối buổi, ghi số bài đã thử, số bài tự giải được và một lỗi lặp lại. Với project, dùng buổi này để chạy lại từ checkout sạch hoặc demo và dọn phần đang làm dở.

### Dùng Anki

1. Ôn các thẻ đến hạn trước. Nhắc lại cách giải, điều kiện đúng hoặc ca lỗi trước khi lật thẻ. Nếu quên ý chính, chọn **Again**. Nếu nhớ đúng nhưng rất chật vật, chọn **Hard**. Nếu nhớ đúng với nỗ lực vừa phải, chọn **Good**. [Cách chấm thẻ trong Anki](https://docs.ankiweb.net/manual/studying#answer-buttons)
2. Chọn bài mới theo tuần bên dưới. Trong Anki, có thể tìm theo tên bài hoặc lệnh in trên thẻ. Chạy `lc review <thư-mục>` để tạo nháp mới. `lc resume` đưa bạn về phiên đang làm dở. Trong Neovim, `Space l l` đổi EN/VI và `Space l t` lưu, chạy test trên bản nháp đang mở.
3. Mỗi ngày chỉ chọn **tối đa một bài cũ** để code lại. Tất cả 150 bài đều mở được bằng `lc review` và có test local chạy bằng `Space l t`.
4. Từ tuần 17, dùng thêm deck **Python Project Design** nếu bạn muốn tách thẻ lý thuyết khỏi thẻ thuật toán. Tạo **1–2 thẻ mỗi tuần** từ quyết định đã thực hiện hoặc lỗi đã tái hiện. Mặt trước nêu tình huống, mặt sau ghi quyết định, lý do và cách kiểm chứng.

### Dùng AI để review

Trước khi hỏi, tự viết một hướng giải, một ví dụ có kết quả mong đợi và phần mình đang vướng. Chạy thử trên ví dụ đó nếu đã có code. Sau review, bạn tự chọn thay đổi, sửa code và chạy lại test.

> **Khi kẹt bài:** “Đây là hướng của tôi và ca đang sai. Hãy cho một gợi ý nhỏ dưới dạng câu hỏi. Dừng trước lời giải và code hoàn chỉnh.”
>
> **Khi review code:** “Chỉ review, chưa sửa file. Hãy chỉ ra một phản ví dụ, một ca biên và độ phức tạp. Với project, xem ranh giới module và cho biết test nào chứng minh hành vi cần giữ.”
>
> **Khi review thiết kế IoT:** “Đây là schema, quy tắc xử lý và output tính tay. Hãy tìm một tình huống retry hoặc late event có thể làm kết quả sai. Dừng ở tình huống và tiêu chí test.”

Khi dùng ví dụ từ công việc, ưu tiên fixture giả lập và thông tin đã được phép chia sẻ. Giữ ghi chú gọn theo mẫu `bài hoặc tính năng · tự làm / có gợi ý / cần quay lại · một ca biên · bước tiếp theo`.

## Tuần 1–15 · 150 bài LeetCode

Mỗi tuần có **10 bài để tiếp cận**. Các mục dùng tên thư mục thật trong repo, kể cả khi số đầu tên thư mục khác mã trên LeetCode. **H** là Hard. Hai buổi cuối dành cho một bài mỗi buổi. Chủ đề và thứ tự đã được sắp lại để thực hành các dạng liên quan trước. [Danh sách NeetCode 150](https://neetcode.io/practice/practice/neetcode150)

### Tuần 1 · Mảng và hashing

**Đích cuối tuần** Dùng bảng tần suất, set và khóa chuẩn hóa. Giải thích khi nào tra cứu một lần giúp bỏ vòng lặp lồng.

- **Buổi 1** · Contains Duplicate (`lc review 0217-contains-duplicate`) · Valid Anagram (`lc review 0242-valid-anagram`)
- **Buổi 2** · Two Sum (`lc review 0001-two-sum`) · Group Anagrams (`lc review 0049-group-anagrams`)
- **Buổi 3** · Valid Sudoku (`lc review 0036-valid-sudoku`) · Encode and Decode Strings (`lc review 0271-encode-and-decode-strings`)
- **Buổi 4** · Top K Frequent Elements (`lc review 0347-top-k-frequent-elements`) · Product of Array Except Self (`lc review 0238-product-of-array-except-self`)
- **Buổi 5** · Longest Consecutive Sequence (`lc review 0128-longest-consecutive-sequence`)
- **Buổi 6** · Valid Palindrome (`lc review 0125-valid-palindrome`)

### Tuần 2 · Hai con trỏ và sliding window

**Đích cuối tuần** Vẽ biên trái/phải và nêu điều kiện giữ cửa sổ hợp lệ. Phân biệt cửa sổ cố định với cửa sổ co giãn.

- **Buổi 1** · Two Sum II Input Array Is Sorted (`lc review 0167-two-sum-ii-input-array-is-sorted`) · Container With Most Water (`lc review 0011-container-with-most-water`)
- **Buổi 2** · 3Sum (`lc review 0015-3sum`) · Best Time to Buy And Sell Stock (`lc review 0121-best-time-to-buy-and-sell-stock`)
- **Buổi 3** · Longest Substring Without Repeating Characters (`lc review 0003-longest-substring-without-repeating-characters`) · Permutation In String (`lc review 0567-permutation-in-string`)
- **Buổi 4** · Longest Repeating Character Replacement (`lc review 0424-longest-repeating-character-replacement`) · Valid Parentheses (`lc review 0020-valid-parentheses`)
- **Buổi 5** · Trapping Rain Water **H** (`lc review 0042-trapping-rain-water`)
- **Buổi 6** · Minimum Window Substring **H** (`lc review 0076-minimum-window-substring`)

### Tuần 3 · Stack, deque và tìm kiếm nhị phân

**Đích cuối tuần** Theo dõi stack đơn điệu trên một ví dụ. Viết bất biến cho hai biên binary search trước khi code.

- **Buổi 1** · Min Stack (`lc review 0155-min-stack`) · Evaluate Reverse Polish Notation (`lc review 0150-evaluate-reverse-polish-notation`)
- **Buổi 2** · Generate Parentheses (`lc review 0022-generate-parentheses`) · Daily Temperatures (`lc review 0739-daily-temperatures`)
- **Buổi 3** · Car Fleet (`lc review 0853-car-fleet`) · Binary Search (`lc review 0792-binary-search`)
- **Buổi 4** · Search a 2D Matrix (`lc review 0074-search-a-2d-matrix`) · Koko Eating Bananas (`lc review 0907-koko-eating-bananas`)
- **Buổi 5** · Largest Rectangle In Histogram **H** (`lc review 0084-largest-rectangle-in-histogram`)
- **Buổi 6** · Sliding Window Maximum **H** (`lc review 0239-sliding-window-maximum`)

### Tuần 4 · Binary search nâng cao và linked list

**Đích cuối tuần** Phân biệt tìm giá trị với tìm đáp án đơn điệu. Vẽ con trỏ trước khi thay đổi liên kết.

- **Buổi 1** · Find Minimum In Rotated Sorted Array (`lc review 0153-find-minimum-in-rotated-sorted-array`) · Search In Rotated Sorted Array (`lc review 0033-search-in-rotated-sorted-array`)
- **Buổi 2** · Time Based Key Value Store (`lc review 0981-time-based-key-value-store`) · Reverse Linked List (`lc review 0206-reverse-linked-list`)
- **Buổi 3** · Merge Two Sorted Lists (`lc review 0021-merge-two-sorted-lists`) · Reorder List (`lc review 0143-reorder-list`)
- **Buổi 4** · Remove Nth Node From End of List (`lc review 0019-remove-nth-node-from-end-of-list`) · Copy List With Random Pointer (`lc review 0138-copy-list-with-random-pointer`)
- **Buổi 5** · Add Two Numbers (`lc review 0002-add-two-numbers`)
- **Buổi 6** · Median of Two Sorted Arrays **H** (`lc review 0004-median-of-two-sorted-arrays`)

### Tuần 5 · Linked list và DFS trên cây

**Đích cuối tuần** Giải thích khóa tra cứu của LRU và tự lần một đường DFS trên cây rỗng, cây lệch.

- **Buổi 1** · Linked List Cycle (`lc review 0141-linked-list-cycle`) · Find The Duplicate Number (`lc review 0287-find-the-duplicate-number`)
- **Buổi 2** · LRU Cache (`lc review 0146-lru-cache`) · Invert Binary Tree (`lc review 0226-invert-binary-tree`)
- **Buổi 3** · Maximum Depth of Binary Tree (`lc review 0104-maximum-depth-of-binary-tree`) · Diameter of Binary Tree (`lc review 0543-diameter-of-binary-tree`)
- **Buổi 4** · Balanced Binary Tree (`lc review 0110-balanced-binary-tree`) · Same Tree (`lc review 0100-same-tree`)
- **Buổi 5** · Merge K Sorted Lists **H** (`lc review 0023-merge-k-sorted-lists`)
- **Buổi 6** · Reverse Nodes In K Group **H** (`lc review 0025-reverse-nodes-in-k-group`)

### Tuần 6 · Cây nhị phân và BST

**Đích cuối tuần** Tự chọn BFS hay DFS, phân biệt trạng thái truyền xuống với giá trị trả lên. Kiểm tra BST bằng cận từ tổ tiên.

- **Buổi 1** · Subtree of Another Tree (`lc review 0572-subtree-of-another-tree`) · Lowest Common Ancestor of a Binary Search Tree (`lc review 0235-lowest-common-ancestor-of-a-binary-search-tree`)
- **Buổi 2** · Binary Tree Level Order Traversal (`lc review 0102-binary-tree-level-order-traversal`) · Binary Tree Right Side View (`lc review 0199-binary-tree-right-side-view`)
- **Buổi 3** · Count Good Nodes In Binary Tree (`lc review 1448-count-good-nodes-in-binary-tree`) · Validate Binary Search Tree (`lc review 0098-validate-binary-search-tree`)
- **Buổi 4** · Kth Smallest Element In a Bst (`lc review 0230-kth-smallest-element-in-a-bst`) · Construct Binary Tree From Preorder And Inorder Traversal (`lc review 0105-construct-binary-tree-from-preorder-and-inorder-traversal`)
- **Buổi 5** · Binary Tree Maximum Path Sum **H** (`lc review 0124-binary-tree-maximum-path-sum`)
- **Buổi 6** · Serialize And Deserialize Binary Tree **H** (`lc review 0297-serialize-and-deserialize-binary-tree`)

### Tuần 7 · Trie và priority queue

**Đích cuối tuần** Tách khái niệm prefix với từ hoàn chỉnh. Giải thích heap chứa gì, phần tử nào ở đỉnh và lúc nào cần cân bằng.

- **Buổi 1** · Implement Trie Prefix Tree (`lc review 0208-implement-trie-prefix-tree`) · Design Add And Search Words Data Structure (`lc review 0211-design-add-and-search-words-data-structure`)
- **Buổi 2** · Kth Largest Element In a Stream (`lc review 0703-kth-largest-element-in-a-stream`) · Last Stone Weight (`lc review 1046-last-stone-weight`)
- **Buổi 3** · K Closest Points to Origin (`lc review 0973-k-closest-points-to-origin`) · Kth Largest Element In An Array (`lc review 0215-kth-largest-element-in-an-array`)
- **Buổi 4** · Task Scheduler (`lc review 0621-task-scheduler`) · Design Twitter (`lc review 0355-design-twitter`)
- **Buổi 5** · Word Search II **H** (`lc review 0212-word-search-ii`)
- **Buổi 6** · Find Median From Data Stream **H** (`lc review 0295-find-median-from-data-stream`)

### Tuần 8 · Backtracking và flood fill

**Đích cuối tuần** Vẽ cây quyết định, định nghĩa điểm dừng và hoàn tác trạng thái. Phân biệt visited theo đường với visited toàn bộ.

- **Buổi 1** · Subsets (`lc review 0078-subsets`) · Combination Sum (`lc review 0039-combination-sum`)
- **Buổi 2** · Permutations (`lc review 0046-permutations`) · Subsets II (`lc review 0090-subsets-ii`)
- **Buổi 3** · Combination Sum II (`lc review 0040-combination-sum-ii`) · Word Search (`lc review 0079-word-search`)
- **Buổi 4** · Palindrome Partitioning (`lc review 0131-palindrome-partitioning`) · Letter Combinations of a Phone Number (`lc review 0017-letter-combinations-of-a-phone-number`)
- **Buổi 5** · Number of Islands (`lc review 0200-number-of-islands`)
- **Buổi 6** · N Queens **H** (`lc review 0051-n-queens`)

### Tuần 9 · Đồ thị, BFS đa nguồn và thứ tự topo

**Đích cuối tuần** Đánh dấu khi đưa vào queue. Dự đoán thứ tự topo và giải thích cách phát hiện chu kỳ.

- **Buổi 1** · Clone Graph (`lc review 0133-clone-graph`) · Max Area of Island (`lc review 0695-max-area-of-island`)
- **Buổi 2** · Pacific Atlantic Water Flow (`lc review 0417-pacific-atlantic-water-flow`) · Surrounded Regions (`lc review 0130-surrounded-regions`)
- **Buổi 3** · Rotting Oranges (`lc review 0994-rotting-oranges`) · Walls And Gates (`lc review 0286-walls-and-gates`)
- **Buổi 4** · Course Schedule (`lc review 0207-course-schedule`) · Course Schedule II (`lc review 0210-course-schedule-ii`)
- **Buổi 5** · Word Ladder **H** (`lc review 0127-word-ladder`)
- **Buổi 6** · Alien Dictionary **H** (`lc review 0269-alien-dictionary`)

### Tuần 10 · Union-find, đường đi và cây khung

**Đích cuối tuần** Chọn thuật toán dựa trên cạnh có trọng số và giới hạn số bước. Giải thích vì sao số điểm dừng là một phần của trạng thái.

- **Buổi 1** · Redundant Connection (`lc review 0684-redundant-connection`) · Number of Connected Components In An Undirected Graph (`lc review 0323-number-of-connected-components-in-an-undirected-graph`)
- **Buổi 2** · Graph Valid Tree (`lc review 0261-graph-valid-tree`) · Min Cost to Connect All Points (`lc review 1584-min-cost-to-connect-all-points`)
- **Buổi 3** · Network Delay Time (`lc review 0743-network-delay-time`) · Cheapest Flights Within K Stops (`lc review 0787-cheapest-flights-within-k-stops`)
- **Buổi 4** · Climbing Stairs (`lc review 0070-climbing-stairs`) · Min Cost Climbing Stairs (`lc review 0746-min-cost-climbing-stairs`)
- **Buổi 5** · Reconstruct Itinerary **H** (`lc review 0332-reconstruct-itinerary`)
- **Buổi 6** · Swim In Rising Water **H** (`lc review 0778-swim-in-rising-water`)

### Tuần 11 · Dynamic programming một chiều

**Đích cuối tuần** Với từng bài, viết một dòng định nghĩa trạng thái, ca cơ sở và thứ tự cập nhật. So sánh hai cách giữ bộ nhớ.

- **Buổi 1** · House Robber (`lc review 0198-house-robber`) · House Robber II (`lc review 0213-house-robber-ii`)
- **Buổi 2** · Longest Palindromic Substring (`lc review 0005-longest-palindromic-substring`) · Palindromic Substrings (`lc review 0647-palindromic-substrings`)
- **Buổi 3** · Decode Ways (`lc review 0091-decode-ways`) · Coin Change (`lc review 0322-coin-change`)
- **Buổi 4** · Maximum Product Subarray (`lc review 0152-maximum-product-subarray`) · Word Break (`lc review 0139-word-break`)
- **Buổi 5** · Longest Increasing Subsequence (`lc review 0300-longest-increasing-subsequence`)
- **Buổi 6** · Partition Equal Subset Sum (`lc review 0416-partition-equal-subset-sum`)

### Tuần 12 · Dynamic programming hai chiều

**Đích cuối tuần** Vẽ bảng nhỏ và tính tay hai ô. Kiểm tra thứ tự vòng lặp và cách xử lý prefix rỗng.

- **Buổi 1** · Unique Paths (`lc review 0062-unique-paths`) · Longest Common Subsequence (`lc review 1143-longest-common-subsequence`)
- **Buổi 2** · Best Time to Buy And Sell Stock With Cooldown (`lc review 0309-best-time-to-buy-and-sell-stock-with-cooldown`) · Coin Change II (`lc review 0518-coin-change-ii`)
- **Buổi 3** · Target Sum (`lc review 0494-target-sum`) · Interleaving String (`lc review 0097-interleaving-string`)
- **Buổi 4** · Edit Distance (`lc review 0072-edit-distance`) · Maximum Subarray (`lc review 0053-maximum-subarray`)
- **Buổi 5** · Longest Increasing Path In a Matrix **H** (`lc review 0329-longest-increasing-path-in-a-matrix`)
- **Buổi 6** · Distinct Subsequences **H** (`lc review 0115-distinct-subsequences`)

### Tuần 13 · Greedy, interval và hai bài DP khó

**Đích cuối tuần** Viết lý do lựa chọn cục bộ an toàn cho một bài greedy. Với DP khó, ưu tiên mô tả trạng thái và tính tay ví dụ nhỏ.

- **Buổi 1** · Jump Game (`lc review 0055-jump-game`) · Jump Game II (`lc review 0045-jump-game-ii`)
- **Buổi 2** · Gas Station (`lc review 0134-gas-station`) · Hand of Straights (`lc review 0846-hand-of-straights`)
- **Buổi 3** · Merge Triplets to Form Target Triplet (`lc review 1899-merge-triplets-to-form-target-triplet`) · Partition Labels (`lc review 0763-partition-labels`)
- **Buổi 4** · Valid Parenthesis String (`lc review 0678-valid-parenthesis-string`) · Insert Interval (`lc review 0057-insert-interval`)
- **Buổi 5** · Burst Balloons **H** (`lc review 0312-burst-balloons`)
- **Buổi 6** · Regular Expression Matching **H** (`lc review 0010-regular-expression-matching`)

### Tuần 14 · Intervals và thao tác ma trận

**Đích cuối tuần** Kiểm tra quy ước hai khoảng chạm biên. Với ma trận, test một hàng, một cột và cập nhật tại chỗ.

- **Buổi 1** · Merge Intervals (`lc review 0056-merge-intervals`) · Non Overlapping Intervals (`lc review 0435-non-overlapping-intervals`)
- **Buổi 2** · Meeting Rooms (`lc review 0252-meeting-rooms`) · Meeting Rooms II (`lc review 0253-meeting-rooms-ii`)
- **Buổi 3** · Rotate Image (`lc review 0048-rotate-image`) · Spiral Matrix (`lc review 0054-spiral-matrix`)
- **Buổi 4** · Set Matrix Zeroes (`lc review 0073-set-matrix-zeroes`) · Happy Number (`lc review 0202-happy-number`)
- **Buổi 5** · Plus One (`lc review 0066-plus-one`)
- **Buổi 6** · Minimum Interval to Include Each Query **H** (`lc review 1851-minimum-interval-to-include-each-query`)

### Tuần 15 · Bit manipulation và số học

**Đích cuối tuần** Theo dõi bit trên ví dụ 4 bit, giải thích mask hoặc XOR. Kiểm tra dấu, carry và giới hạn số nguyên.

- **Buổi 1** · Single Number (`lc review 0136-single-number`) · Number of 1 Bits (`lc review 0191-number-of-1-bits`)
- **Buổi 2** · Counting Bits (`lc review 0338-counting-bits`) · Reverse Bits (`lc review 0190-reverse-bits`)
- **Buổi 3** · Missing Number (`lc review 0268-missing-number`) · Sum of Two Integers (`lc review 0371-sum-of-two-integers`)
- **Buổi 4** · Pow(x, n) (`lc review 0050-powx-n`) · Multiply Strings (`lc review 0043-multiply-strings`)
- **Buổi 5** · Detect Squares (`lc review 2013-detect-squares`)
- **Buổi 6** · Reverse Integer (`lc review 0007-reverse-integer`)

### Tuần 16 · Ôn tổng hợp và bù phần còn thiếu

- **Buổi 1–2** · Chọn hai bài còn dang dở. Từ nháp mới, tự viết lại phần mình từng phải xem gợi ý.
- **Buổi 3–4** · Lấy một bài mảng hoặc cửa sổ và một bài cây hoặc đồ thị. Tự chọn hướng, giải thích bất biến và kiểm tra hai ca biên trước khi nhờ review.
- **Buổi 5–6** · Lấy một bài DP và một bài từng sai. Viết trạng thái hoặc nguyên nhân sai từ trí nhớ, rồi đối chiếu bằng code.
- **Buổi 7** · Kiểm tra đã tiếp cận đủ 150 bài. Chọn ba điểm yếu để tiếp tục ôn trên Anki trong giai đoạn project.

**Tiêu chí chuyển chặng** Với ít nhất 3 trong 4 bài kiểm tra lại, bạn tự nêu được hướng giải, độ phức tạp và một ca biên. Nếu nhiều bài vẫn chỉ dừng ở đọc lời giải, dành thêm một tuần cho đúng các dạng đó.

## Tuần 17–21 · Project Python thực hành thiết kế

**Đề bài** Làm CLI tổng hợp đơn hàng trong một repo riêng, dùng dữ liệu giả lập. Một dòng CSV tương ứng một đơn. Dùng Neovim, `uv`, `pytest`, Git và SQLite. Mỗi tuần chốt tiêu chí nghiệm thu bằng một đặc tả ngắn trước khi code. Có thể dùng Spec Kit cho bản đầu và các thay đổi có nhiều quyết định.

**Nhịp mỗi tuần** Buổi 1 viết đầu vào, đầu ra và ví dụ tính tay. Buổi 2–4 tự viết code và test. Buổi 5 chạy test tích hợp. Buổi 6 nhờ AI review một phần đã chạy được. Buổi 7 demo và tạo thẻ Anki từ lỗi hoặc quyết định có thật.

| Tuần | Bài tập và thứ tự thực hiện | Đầu ra kiểm chứng | Thẻ Anki gợi ý |
| --- | --- | --- | --- |
| **17 · CLI v1** | Chọn cột `order_id`, ngày và số tiền. Tạo `src/order_report/` với `cli.py`, `csv_input.py`, `report.py`, cùng `tests/`. Viết luồng đọc CSV → kiểm tra → cộng tiền theo ngày. | Một lệnh chạy trên fixture. Test file rỗng, dòng thiếu cột, tiền sai định dạng và báo cáo hai ngày. Dùng số thập phân chính xác cho tiền. | Hàm cộng tiền theo ngày cần biết gì về CSV? |
| **18 · Thêm nguồn thứ hai** | Viết fixture cho file có tên cột và định dạng ngày khác. Tạo kiểu `Order` chung. Đưa phần chuyển đổi riêng của từng nguồn vào adapter và dùng lại báo cáo. | Hai file khác định dạng nhưng biểu diễn cùng đơn cho cùng kết quả. Test cũ của `report.py` vẫn chạy. | Khi nguồn thứ ba xuất hiện, nơi nào được phép thay đổi? |
| **19 · SQLite và nhập lại** | Thêm lệnh import. Dùng khóa ổn định `(source, order_id)` theo hợp đồng một dòng mỗi đơn. Tách truy vấn khỏi logic báo cáo và chốt cách xử lý nếu cùng khóa có số tiền khác. | Nhập cùng file hai lần giữ nguyên số dòng và tổng tiền. Fixture có lỗi giữa lô chứng minh phần đã ghi tuân theo quy tắc transaction bạn chọn. | Đâu là ranh giới commit? Retry có thể ghi lại gì? |
| **20 · Báo cáo gộp và thuần** | Thêm hoàn tiền vào dữ liệu giả lập. Viết hai cách tính, dùng cùng đầu vào và chọn qua CLI. Chỉ tách Strategy khi hai cách tính đã có quy tắc riêng. | Fixture có đơn trả một phần và hoàn toàn cho ra hai kết quả đã tính tay. Có test cho mỗi chính sách. | Khi nào thêm một tham số là đủ, khi nào cần hai hàm tính? |
| **21 · Hoàn thiện và đọc lại** | Từ checkout sạch, cài và chạy bằng README. Review đường import, cách chia module và tên hàm. Tự thực hiện một thay đổi nhỏ, chẳng hạn lọc theo khoảng ngày. | Một người đọc README chạy được báo cáo. Bạn chỉ ra file thay đổi, test mới và cách kiểm chứng tính năng cũ. | Một dấu hiệu cụ thể cho thấy module đang có quá nhiều trách nhiệm là gì? |

**Điều kiện chuyển sang IoT** Tự lần được một dòng CSV từ đầu vào đến kết quả. Tự giải thích cách thêm nguồn mới và chứng minh nhập lại không nhân đôi dữ liệu. Giữ lại sơ đồ luồng, fixture, README và bộ test để làm mẫu cho project sau.

## Tuần 22–28 · Pipeline telemetry IoT

**Kịch bản** Gateway mất mạng 30 phút rồi gửi bù bản đo. Một số event bị gửi lại, một số đến sai thứ tự, và bản ghi firmware mới có cấu trúc khác. Dùng dữ liệu giả lập với Python và SQL trên stack bạn đã quen. Bắt đầu bằng batch nhỏ có thể chạy ở máy cá nhân.

**Luồng tối thiểu** `raw event → validate và chuẩn hóa → clean event → aggregate 5 phút theo thiết bị`. Lưu riêng `event_time` và `ingest_time`. Chỉ dùng khóa dedup mà fixture và hợp đồng producer chứng minh là ổn định khi gửi lại. Quy ước UTC và cửa sổ dạng `[start, end)`. [Event time và dữ liệu đến muộn](https://beam.apache.org/documentation/programming-guide/#watermarks-and-late-data)

| Tuần | Việc làm trong tuần | Tiêu chí nghiệm thu | Thẻ Anki gợi ý |
| --- | --- | --- | --- |
| **22 · Data contract và fixture** | Buổi 1 vẽ luồng và định nghĩa `device_id`, `event_id`, hai timestamp, giá trị, đơn vị và schema version. Buổi 2–4 tạo fixture cho hai thiết bị với event đúng, thiếu trường, sai kiểu và sai timestamp. Buổi 5–7 review cách ghi raw và ghi lý do reject. | Mỗi event được chấp nhận hoặc có lý do reject cụ thể. Có thể lần từ bản ghi chuẩn hóa về raw event. | Nếu gateway gửi lại, trường nào chứng minh đây là cùng một event? |
| **23 · Aggregate bằng SQL** | Buổi 1 tính tay số mẫu và trung bình cho hai thiết bị. Buổi 2–4 viết query bucket 5 phút theo `event_time`. Buổi 5–7 kiểm tra mốc 10:04:59 và 10:05:00, cùng sự khác biệt giữa hai timestamp. | Query khớp với bảng tính tay và gán đúng hai event ở hai phía biên. | Event ở đúng 10:05:00 thuộc cửa sổ nào? |
| **24 · Dedup và bản ghi xung đột** | Tạo fixture gồm bản gửi lại giống hệt và bản cùng khóa nhưng khác payload. Chọn quy tắc báo xung đột. Đặt kiểm tra khóa ở lớp lưu clean event. | Replay cùng lô hai lần giữ nguyên số event sạch và aggregate. Hai bản đo thật có cùng timestamp vẫn được tính riêng nếu ID khác nhau. | Vì sao `device_id + event_time` có thể làm mất dữ liệu? |
| **25 · Late event và backfill** | Mô phỏng event đo 10:02 nhưng nhận 10:35. Chọn khoảng chấp nhận đến muộn cho lab. Nếu quá khoảng này, ghi vào danh sách chờ backfill. Viết lệnh tính lại khoảng bị ảnh hưởng từ dữ liệu gốc. | Ca trong ngưỡng cập nhật đúng bucket. Ca ngoài ngưỡng xuất hiện trong danh sách backfill. Chạy lại chỉ sửa cửa sổ bị ảnh hưởng và khớp kết quả tính toàn bộ. | Khi event đến sau khi đã xuất báo cáo, dựa vào gì để chọn cập nhật hay backfill? |
| **26 · Retry và checkpoint** | Chèn lỗi giả sau khi ghi output nhưng trước khi ghi checkpoint. Đọc lại log và kiểm tra trạng thái. Dùng transaction chung hoặc cách ghi kết quả an toàn khi chạy lại, tùy kho dữ liệu đã chọn. | Cố tình dừng rồi chạy lại cho kết quả giống lần chạy sạch. Có test đối chiếu số dòng và aggregate. | Sau khi output ghi xong nhưng checkpoint chưa cập nhật, retry lặp lại phần nào? |
| **27 · Schema evolution và quan sát** | Thêm firmware v2 đổi tên trường hoặc đơn vị. Viết adapter cho v2 và giữ fixture v1. Ghi số event lỗi, trùng, muộn và độ trễ ingest. Viết runbook ngắn để lần từ số liệu bất thường tới raw. | V1 và v2 cùng quy về giá trị chuẩn trên fixture. Các bộ đếm khớp dữ liệu đã tiêm. Người đọc runbook biết kiểm tra đâu khi tỷ lệ trùng tăng. | Phân biệt đổi schema với thiết bị thực sự ngừng gửi thế nào? |
| **28 · Diễn tập sự cố và chuyển vào công việc** | Dựng lại toàn bộ gateway offline rồi replay. Tự debug một lỗi do mình tiêm mà chưa nhìn lời giải. Nhờ AI review runbook và test. Chọn một việc nhỏ trong hệ thống thật, ví dụ thêm regression test cho lỗi đếm trùng trong phạm vi được phép. | Có demo từ raw event tới aggregate và một trang mô tả nguyên nhân, cách tái hiện, bản sửa, bằng chứng. Có thể trình bày đường đi của một event cụ thể trong review. | Tín hiệu nào phân biệt tăng lưu lượng thật với replay sau mất mạng? |

## Kiểm tra tiến độ cuối mỗi tuần

- [ ] Tôi giải thích được một quyết định hoặc một lỗi bằng ví dụ cụ thể, trước khi mở AI.
- [ ] Tôi có ít nhất một bằng chứng chạy được, như test, query đối chiếu hoặc bản nháp tự giải.
- [ ] Tôi đã ôn các thẻ đến hạn trong ngân sách thời gian và chọn một điều cần ôn lại.
- [ ] Tôi đã chọn mục đầu tiên cho tuần tới. Nếu tuần này thiếu thời gian, tôi đã dời mục ít quan trọng sang tuần đệm.

**Kết quả cuối roadmap** Bạn có hai project chạy được, một quy trình ôn Anki và bằng chứng cho một năng lực sát công việc: khi dashboard IoT đếm gấp đôi sau khi gateway online, bạn tự lần về raw event, tái hiện lỗi và chứng minh cách chạy lại cho kết quả đúng.

### Tài liệu dùng khi tới từng chặng

- [NeetCode 150](https://neetcode.io/practice/practice/neetcode150)
- [Học và chấm thẻ trong Anki](https://docs.ankiweb.net/manual/studying)
- [Tổ chức Python package theo bố cục src](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [Python sqlite3 và transaction](https://docs.python.org/3/library/sqlite3.html)
- [Event time, cửa sổ và late data](https://beam.apache.org/documentation/programming-guide/#watermarks-and-late-data)
