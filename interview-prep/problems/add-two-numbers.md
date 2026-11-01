# Add Two Numbers: Walkthrough

> Two non-empty linked lists represent two non-negative integers. The digits are
> stored in **reverse order** and each node holds one digit. Add the two numbers
> and return the sum as a linked list in the same format.
> Constraints: 1–100 nodes per list, `0 <= val <= 9`, no leading zeros except the number 0.

Your submission: [`Data Structures & Algorithms/add-two-numbers/submission-0.py`](../../Data%20Structures%20%26%20Algorithms/add-two-numbers/submission-0.py)

---

## Part 1: An honest review of your submission

### What you did well
- **You started with a plan in comments** (iterate → arrays → reverse → join →
  int → add). That's the right instinct: say the plan before you code it.
- **You traced values next to each line** (`# [1, 2, 3]`, `# "654" ; "321"`). In an
  interview, say these values out loud.
- **The idea is a legitimate brute force:** "convert to real integers, add, convert
  back." It's correct in Python, and it's a fine thing to *say* first.

### What an interviewer would push on

| Issue | Why it matters |
|-------|----------------|
| **Node values are strings.** `s1 = list(str(...))` produces `'7','0','8'`, and those characters go straight into `curr.val`. I ran your code: it returns `['7','0','8']`, not `[7,0,8]`. | A real type bug. A strict checker, or a typed language, would reject it. A trace that says the *type* out loud ("val is the character '7'") catches this. |
| **It only works because Python has unlimited-size integers.** Lists can be 100 digits long, so a number can be close to 10¹⁰⁰. A 64-bit integer holds about 19 digits. | In C++ or Java this overflows. The interviewer's first follow-up would be *"What if you couldn't convert to an int?"*, and that question is the whole problem. |
| **You reverse twice**: once to read the number, once to write it back. | The input was *already* in the order you need (see Part 3). Reversing it throws away the structure the problem gave you. |
| **Leftover code:** unused `res`, a `print`, two passes to build the output list, `s1` reused as str → int → str → list. | Hard to narrate clearly and looks unfinished. Use one name per meaning and remove debug output. |
| **Inconsistent traversal:** `l1` uses `curr`, `l2` is moved directly. | A small thing, but consistency makes your code easier to explain. |

**Takeaway:** your approach wasn't "wrong." What was missing was the step of
**stating the brute force, costing it, and then asking "what am I not using?"**
That question takes you straight to the optimal answer here.

---

## Part 2: The interview, spoken

### 1. Restate
> "I have two linked lists. Each one is a number with its digits stored backwards,
> so the head is the ones place. I need to return their sum in the same backwards
> format."

### 2. Clarifying questions (with the answers you'd likely get)

| Question | Likely answer | Why you ask |
|----------|---------------|-------------|
| "Can either list be empty?" | No, both have at least 1 node. | Decides whether you need a null guard at the start. |
| "Can the lists have different lengths?" | Yes. | **This is a key edge case.** Your loop must handle one list running out. |
| "Any negative numbers?" | No, each node is 0–9. | Rules out sign handling. |
| "How long can the lists be?" | Up to 100 nodes. | **Triggers the overflow concern.** You can't safely convert to an int. |
| "Should I return a new list, or can I reuse the input nodes?" | A new list is fine. | Shows you think about mutation. |
| "Can there be leading zeros?" | Only for the number 0 itself. | Means you don't need to strip zeros. |

### 3. Examples: draw them, including your own

```
Given:     2 → 4 → 3        (342)
         + 5 → 6 → 4        (465)
         = 7 → 0 → 8        (807)

Unequal lengths:   9 → 9    (99)
                 + 1        (1)
                 = 0 → 0 → 1   (100)   ← one list runs out, carry keeps going

Final carry only:  5  +  5  =  0 → 1   (10)   ← loop must keep going after both lists end

Smallest:          0  +  0  =  0
```

> Saying out loud *"Let me make an example where one list runs out and a carry is
> still left over"* shows strong edge-case thinking. Interviewers remember it.

### 4. Brute force: your solution, presented well
> "The most direct approach is to walk each list, rebuild the actual integers, add
> them, and turn the sum back into a list. That's O(m + n) time and space. The
> problem is that the lists can be 100 digits, which overflows any fixed-size
> integer type. Python would hide that, but it's relying on a language feature, so
> I'd rather do the addition digit by digit."

You've shown you can solve it, you've analyzed it, and you've explained *why*
you're moving on. That counts as good communication even though you didn't code it.

### 5. Optimize: the key insight

Ask: **"Why are the digits stored in reverse? What is the input giving me?"**

Do `342 + 465` on paper, the way you learned in grade school:

```
    carry:  0  1  0
              3  4  2
            + 4  6  5
            ---------
              8  0  7
```

You add **right to left**: ones place first, then tens, then hundreds. The *ones*
digit is the head of each list. **The lists are already in the order you add
digits by hand.** Reversing them undid the problem's gift.

Next question: *"At each column, what's the minimum I need to know?"*
- The digit from list 1 (or 0 if it has run out)
- The digit from list 2 (or 0 if it has run out)
- **The carry from the previous column**

That's all of it. The carry is your whole state, and it's always 0 or 1
(at most 9 + 9 + 1 = 19).

> Spoken: *"Since the lists start at the ones place, I can walk both at the same
> time and do column addition with a carry. I write `total % 10` to the output and
> carry `total // 10` into the next column."*

### 6. Plan, then get buy-in

```
dummy = new node; tail = dummy; carry = 0
while l1 has nodes OR l2 has nodes OR carry != 0:
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0
    total = v1 + v2 + carry
    carry = total // 10
    append node(total % 10) after tail; move tail forward
    move l1 and l2 forward if they exist
return dummy.next
```

**Explain each design choice out loud:**
- **Dummy head:** "So I don't need an `if head is None` special case for the first node."
- **`or l1 or l2`:** "This handles lists of different lengths. A list that has run out just contributes 0."
- **`or carry`:** "This handles a final carry, like 5 + 5 = 10, which needs an extra node."
- **`v = node.val if node else 0`:** "Treating a missing digit as 0 is like padding the shorter number with leading zeros."

> "Does this approach sound good before I code it?"

### 7. Code

Try writing it yourself from the plan first, then compare.

<details>
<summary>Reference solution (click to reveal)</summary>

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()          # placeholder head; real list starts at dummy.next
        tail = dummy
        carry = 0

        while l1 or l2 or carry:    # keep going while any digit or carry remains
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
```

I tested this on all the examples above, plus `[9,9,9,9,9,9,9] + [9,9,9,9]` →
`[8,9,9,9,0,0,0,1]`.
</details>

### 8. Trace it out loud: `[9, 9] + [1]`

| Iteration | l1.val | l2.val | carry in | total | write | carry out |
|-----------|--------|--------|----------|-------|-------|-----------|
| 1 | 9 | 1 | 0 | 10 | 0 | 1 |
| 2 | 9 | *(none → 0)* | 1 | 10 | 0 | 1 |
| 3 | *(none → 0)* | *(none → 0)* | 1 | 1 | 1 | 0 |
| loop ends: both lists are `None` and carry is 0 | | | | | | |

Result: `0 → 0 → 1` = 100 ✓. This single trace tests both the unequal-length
case and the final-carry case.

### Complexity
> "Time is O(max(m, n)): one pass, constant work per digit. Extra space is O(1),
> just the carry and a few pointers. The output list itself is max(m, n) + 1 nodes."

---

## Part 3: Follow-ups to prepare for

| Follow-up | How to answer |
|-----------|---------------|
| "What if the digits were stored most-significant first?" (*LeetCode 445, Add Two Numbers II*) | You can't add from the head anymore. Push both lists onto stacks, *or* reverse both lists, then do the same carry loop. Build the result by **prepending** nodes. |
| "Can you do it without allocating new nodes?" | Reuse `l1`'s nodes to store sums. Only allocate when `l1` runs out or there's a final carry. Mention that this modifies the input, so ask whether that's allowed. |
| "What if it were subtraction?" | Same column structure, but with a borrow instead of a carry. You'd need to know which number is larger, and strip leading zeros at the end. |
| "What if the numbers were in base 2 / base k?" | Replace 10 with k. The structure doesn't change. Worth saying for NVIDIA-style bit questions: binary addition with a carry is what a hardware adder does. |

---

## Part 4: Lessons that transfer to other problems

1. **An unusual input format is often a hint.** "Reverse order" here meant
   "the ones place comes first." Always ask *why* the input is shaped the way it is.
2. **Dummy head node** for building any linked list. You'll use it again in Merge
   Two Sorted Lists, Remove Nth Node, Partition List, and others.
3. **`while a or b or extra:`** handles leftover input in one loop instead of
   separate cleanup loops afterward. Merge Two Sorted Lists uses the same idea.
4. **Find the minimal state** ("what do I need to carry forward?"). Here it's one
   number. In sliding window it's a window, and in DP it's a table row.
5. **Brute force is a step, not the destination.** Your instinct to try the direct
   approach first was right. The missing piece was asking "what does this rely on,
   and what is the input giving me that I'm ignoring?"

---

## 60-second verbal summary (practice saying this)

> "Each list stores a number with the ones place first, which is the order we add
> by hand. So I walk both lists together, add the two digits plus a carry, write
> `total mod 10` to a new node, and carry `total div 10` forward. If one list runs
> out I treat its digit as 0, and I keep looping while there's still a carry, so
> a sum like 5 + 5 gets its extra digit. I use a dummy head so the first node isn't
> a special case. It's linear time in the longer list and constant extra space. I
> avoided converting to integers because 100-digit numbers would overflow in most
> languages."
