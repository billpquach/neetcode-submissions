# Review of My Submissions: Strengths, Gaps, and Habits to Build

Snapshot: 25 problems synced so far (Arrays & Hashing, Two Pointers, Stack, Linked
List, Heap, Bit Manipulation).

---

## Strengths to build on

### 1. You already think on paper
Many files have hand traces in the comments. That's exactly what interviewers want
to see, so **turn it into speech.**
- `kth-largest-integer-in-a-stream`: you traced the heap state after every `add`.
- `number-of-one-bits/submission-1`: you traced `n & (n-1)` bit by bit.
- `counting-bits`: you wrote out the 0–8 binary table to find a pattern.
- `three-integer-sum`: you drew `i`, `l`, `r` positions on the array.

### 2. You shrink problems
`reverse-bits/submission-0` and `-1` work out a **6-bit** version before the 32-bit
one. That's a strong problem-solving habit. **Say it out loud in interviews:**
*"Let me try a smaller version first."*

### 3. You ask yourself the right questions
`k-closest-points-to-origin`: `# Data structure?` → `# closest == smallest distance`
`top-k-elements-in-list/submission-6`: `# maxHeap or minHeap?`

These are the questions you should be saying to the interviewer. The next step is
to **answer them out loud with a reason**: *"Min-heap, because I want to throw
away the smallest frequency whenever the heap grows past k."*

### 4. You iterate toward cleaner solutions
- `middle-of-the-linked-list`: submission-0 had a nested `if` inside the loop.
  Submission-1 is the standard `while fast and fast.next`.
- `counting-bits`: submission-0 used a "last power of two" offset. Submission-1 uses
  `res[i // 2] + i % 2`. **Two different DP recurrences.** Being able to explain
  both is a strong signal.
- `number-of-one-bits`: you know both the shift approach (O(32)) and
  `n & (n-1)` (O(number of set bits)). **Offer both in an interview** and compare them.

### 5. Your bit manipulation is strong
`power-of-two`, `missing-number` (XOR), `reverse-bits`, `counting-bits`,
`number-of-one-bits` are all clean. For an NVIDIA interview this is a real asset;
low-level and bit-level questions are common at hardware companies. Be ready to
explain *why* each trick works, not just the trick:
- `n & (n-1)` clears the lowest set bit, because subtracting 1 flips that bit and every bit below it.
- XOR cancels pairs (`a ^ a = 0`), so XOR-ing 0..n with all the nums leaves only the missing number.

### 6. You know the size-k heap pattern
Used consistently in `kth-largest-element-in-an-array`, `kth-largest-integer-in-a-stream`,
`top-k-elements-in-list`, and `k-closest-points-to-origin`. You can now state the
general rule: *"Top-k → heap of size k → O(n log k)."*

---

## Gaps to work on, and the habit that fixes each

### 1. Complexity is almost never written down
Almost no file states its time/space cost.
**Habit:** end every solution with a comment like `# O(n) time, O(n) space: one pass + hash set`.
In interviews, **say it before they ask.**

### 2. Edge cases get patched instead of planned
`longest-consecutive-sequence/submission-6`:
```python
if len(seen) == 0: return 0
if len(seen) == 1: return 1
```
These come after the main logic, and the solution also builds a full list of each
sequence when it only needs the *length*. The clean version is:
```python
for n in seen:
    if n - 1 not in seen:          # n starts a sequence
        length = 1
        while n + length in seen:
            length += 1
        best = max(best, length)
```
That version handles empty and single-element input naturally (`best = 0`).
**Habit:** ask "empty? single element? duplicates?" in the **clarify** step, and
check that your main algorithm handles them *without* special cases.
**Ask yourself:** "Do I need the sequence itself, or only its length?" Store the
minimum that answers the question.

### 3. Comments describe *what*, not *why*, or stop halfway
`daily-temperatures`:
```python
# the length of the stack is the value of the idx of the
```
The comment trails off, and it doesn't match the code (`results[index] = i - index`
uses distance, not stack length). The code is right, but the **explanation** was
still fuzzy. In an interview, the explanation is what's being graded.
**Habit:** state the **invariant** in one sentence: *"The stack holds indices of
days still waiting for a warmer day, in decreasing temperature order. When a
warmer day shows up, I pop each waiting day and record the distance."*

### 4. Comments that contradict the code
`k-closest-points-to-origin`: the comment says `# therefore we want a minHeap`,
and the code (correctly) uses a **max-heap** of size k. Saying one thing and
writing another confuses interviewers.
**Habit:** when you change your mind, *say so*: "Actually, I want a max-heap, so I
can evict the farthest point."

### 5. Language feature risks
- `heapq.heappush_max`, `heappop_max`, and `heapify_max` became public only in
  **Python 3.14**. Many interview platforms run older Python versions, where those
  calls fail. **Know the classic trick:** push `-x` into a min-heap. Say that in an
  interview even if you use the newer API.
- `add-two-numbers`: converting to `int` only works because Python integers have
  no size limit. In C++/Java a 100-digit number overflows.
- `k-closest-points-to-origin`: `math.sqrt` isn't needed. Comparing `x² + y²` gives
  the same ordering, and you avoid floating-point issues. Interviewers like hearing
  that you noticed.

### 6. Know your tools exactly
- `anagram-groups`: `defaultdict(int)` and then manually assigning lists, plus an
  `if / elif` that checks the same condition twice. `defaultdict(list)` with
  `hMap[key].append(word)` does the whole thing in one line. An interviewer may ask
  *"why `int`?"*
- `is-anagram/submission-3`: `t.replace(i, "", 1)` in a loop is O(n²), worse than
  your earlier O(n) counting solution. Exploring is fine. Just **know the cost of
  every built-in you call** (`replace`, `in` on a list, slicing, `sorted`).

### 7. Mutating inputs without asking
`kth-largest-integer-in-a-stream` sets `self.minHeap = nums` and heapifies the
caller's list. `last-stone-weight` heapifies `stones` in place.
**Habit:** ask *"Can I modify the input?"* during clarification. It costs 3 seconds
and shows maturity.

### 8. Loop conditions that are hard to justify
- `last-stone-weight`: `for i in range(len(maxHeap)): if len(maxHeap) <= 1: break`
  really means `while len(maxHeap) > 1:`. Write it that way so the condition says
  what you mean.
  - Also: you push `y - x` even when it's 0. That's harmless here, since a 0 stone
    acts like a destroyed one, but **say so** so the interviewer knows it's deliberate.
- `is-palindrome/submission-2`: the inner bounds `l < len(s)-1` and `r > 0` work (I
  checked every string up to length 6 over `{a, b, .}`), but they're hard to argue
  out loud. `while l < r and not s[l].isalnum()` states the real invariant: the
  pointers never cross.

### 9. Leftover debug output
`print(...)` in `add-two-numbers` and `is-palindrome/submission-2`, plus many
commented-out `#print`s. **Habit:** before saying "done," scan the code and remove them.

---

## Follow-up questions to prepare for problems you've solved

| Problem | Likely follow-up | Answer direction |
|---------|------------------|------------------|
| `top-k-elements-in-list` | "Can you beat O(n log k)?" | Bucket sort by frequency → O(n) |
| `kth-largest-element-in-an-array` | "Can you do it without a heap?" | Quickselect: average O(n), worst O(n²) |
| `products-of-array-discluding-self` | "O(1) extra space, not counting the output?" | Write prefix products into the output array, then multiply in suffix products using a single running variable |
| `two-integer-sum` | "Can you do it in one pass?" | Check for the complement *before* inserting the current number |
| `three-integer-sum` | "Any early exit?" | After sorting, `if nums[i] > 0: break` |
| `missing-number` | "Another way?" | `n(n+1)/2 - sum(nums)`. Mention that in C++ the sum could overflow, while XOR can't |
| `middle-of-the-linked-list` | "Detect a cycle?" | Same fast/slow pointers (Floyd's algorithm) |

---

## Coverage gaps (NeetCode 150 topics not practiced yet)

You haven't attempted these yet: **sliding window, binary search, trees, tries,
backtracking, graphs, 1-D/2-D DP, intervals, greedy.**
With about a month left, breadth matters more than doing a 6th submission of the
same heap problem. See the plan in [`README.md`](README.md).
