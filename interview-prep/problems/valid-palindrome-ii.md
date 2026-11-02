# Valid Palindrome II: Review & Walkthrough

> Given a string `s`, return `true` if it can be a palindrome after deleting **at
> most one** character.

---

## Part 1: Review of my submission

```python
l, r = 0, len(s) - 1
shifted = False
while l < r:
    print (s[l], s[r])
    if s[l] != s[r]:
        if shifted == True: return False
        elif s[l + 1] == s[r] and s[l + 2] == s[r - 1] if r - l >= 2 else True:
            l += 1
            shifted = True
        elif s[r - 1] == s[l] and s[r - 2] == s[l + 1] if r - l >= 2 else True:
            r -= 1
            shifted = True
        else:
            return False
    l += 1
    r -= 1
return True
```

### It's not correct: the lookahead is a guess

I compared it with a brute-force checker on every string over `{a, b, c}` up to
length 10. **It gives the wrong answer on 138 of them.** The shortest:

```
s = "abaabab"      expected: True   (delete the last 'b' → "abaaba")

 index: 0 1 2 3 4 5 6
        a b a a b a b
        l           r      'a' != 'b' → mismatch
```
- Skip left? It checks `s[1]=='b' == s[6]=='b'` ✓ and `s[2]=='a' == s[5]=='a'` ✓, so it **commits to skipping left**.
- Next it compares `l=2, r=5` ✓, then `l=3 ('a')` with `r=4 ('b')` ✗. Since `shifted` is True, it returns **False**.
- But skipping **right** was the correct choice.

### The real lesson: patching to pass a test vs. fixing the reasoning

Your comments tell the story:
```
# lcupuufxoohdf...ucul      ← a failing test case
# naive check for next element does not work
# prioritizes l pointer
```
A 1-character lookahead failed on that test, so you extended it to 2 characters.
That passes that test, but **any fixed-length lookahead can be beaten.** I just
made a string where 2 characters isn't enough, and the same trick works for 3, 4,
and so on.

When a heuristic fails, don't ask "how do I make it look further?" Ask:
**"Why can't I decide here? What information am I missing?"**

The answer: at a mismatch, *nothing nearby* tells you which side to delete. Only
the whole remaining substring can. **So don't guess. Try both.**

> This is the same pattern as `longest-consecutive-sequence` (see `02-repo-review.md`,
> gap #2): a failing test led to a patch instead of a rethink.

### Smaller code issues

| Issue | Fix |
|-------|-----|
| `print` inside the loop. With up to 10⁵ characters, this can be slow enough to time out, and it's leftover debug code. | Delete it. |
| `A and B if cond else True` works, because Python reads it as `(A and B) if cond else True`. But most readers (and interviewers) have to stop and work out the precedence. | If you need a conditional like this, use parentheses or an `if` block. Here you don't need one at all. |
| `if shifted == True:` | `if shifted:`. With the better approach, you don't need the flag at all. |
| The mismatch logic is tangled into the main loop. | Pull out an `is_pal(l, r)` helper. It reads better and is easier to narrate. |

---

## Part 2: The interview, spoken

### Clarify
| Question | Why |
|----------|-----|
| "Does 'at most one' include zero? So if it's already a palindrome, I return True?" | Yes. Confirms the base case. |
| "Only lowercase letters, or do I need to ignore case and punctuation like Valid Palindrome I?" | Lowercase only. That saves you from writing filtering code. |
| "How long can the string be?" | Up to 10⁵, so O(n²) is too slow. |

### Brute force
> "I could try deleting each character, one at a time, and check if the result is a
> palindrome. That's n deletions × O(n) per check = **O(n²)**. Too slow for 10⁵."

#### Brute force code (your fallback for partial credit)

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Brute force: try deleting each character (or none) and check.
        # O(n^2) time: n candidates x O(n) check. O(n) space for each sliced copy.

        def is_pal(t: str) -> bool:
            return t == t[::-1]

        if is_pal(s):                           # zero deletions
            return True
        for i in range(len(s)):                 # delete s[i]
            if is_pal(s[:i] + s[i + 1:]):
                return True
        return False
```

This takes about 2 minutes to write and is hard to get wrong. I checked it against
every `{a, b, c}` string up to length 10 with 0 failures. It takes about 10 seconds
at n = 10⁵, so it would time out on the judge, but it's **correct**, and that's
what earns partial credit.

If the interviewer asks for O(1) space, skip an index instead of slicing:
```python
def is_pal_skip(skip):              # palindrome check pretending s[skip] is gone
    l, r = 0, len(s) - 1
    while l < r:
        if l == skip: l += 1; continue
        if r == skip: r -= 1; continue
        if s[l] != s[r]: return False
        l += 1; r -= 1
    return True

return any(is_pal_skip(i) for i in range(-1, len(s)))   # -1 = delete nothing
```

#### The brute force is a stepping stone to the optimal solution

Compare them side by side. **The optimal solution *is* the brute force with the
candidate list narrowed from n to 2:**

```
brute:    for every i in 0..n-1:       is s without s[i] a palindrome?
optimal:  for i in {l, r} at first mismatch:  is s without s[i] a palindrome?
```

Say this out loud as you move from one to the other:
> "My brute force tries all n deletions. But only the two characters at the first
> mismatch can actually fix it, so I only need to try those two. Same helper, 2
> calls instead of n."

That's why writing `is_pal` as a separate helper pays off: if you code the brute
force first, the upgrade is changing one loop.

### Find the bottleneck
> "Most of those n deletions are pointless. Let me walk two pointers in from the
> ends. Every pair that matches is already fine. At the **first mismatch**,
> `s[l] != s[r]`, deleting something in between doesn't help, because `s[l]` and
> `s[r]` would still face each other. So **one of these two characters has to
> go.** That cuts n candidates down to 2."

> "I can't tell from nearby characters which one to delete. My first idea was
> lookahead, but any fixed lookahead can be fooled. So I'll check both: is
> `s[l+1..r]` a palindrome, or is `s[l..r-1]` a palindrome? Each is an ordinary
> palindrome check."

### Plan
```
walk l, r inward while s[l] == s[r]
on first mismatch:
    return is_pal(l+1, r) or is_pal(l, r-1)   # delete left OR delete right
if pointers meet: return True
```

### Code

<details>
<summary>Reference solution (click to reveal; try it first)</summary>

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Two pointers from both ends. The first mismatch is the only place a
        # deletion can help, and the deleted char must be s[l] or s[r].
        # Nearby characters can't tell us which, so try both.

        def is_pal(l: int, r: int) -> bool:
            # plain palindrome check on s[l..r], no deletions left
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pal(l + 1, r) or is_pal(l, r - 1)  # delete left or right
            l += 1
            r -= 1
        return True
        # O(n) time: each character is visited a constant number of times.
        # O(1) space: just indices.
```

I tested this against the brute force on every `{a, b, c}` string up to length 10,
with 0 failures.
</details>

### Trace: `"abaabab"`
| step | l | r | s[l] | s[r] | action |
|------|---|---|------|------|--------|
| 1 | 0 | 6 | a | b | mismatch → try `is_pal(1,6)` = "baabab" ✗, try `is_pal(0,5)` = "abaaba" ✓ |
| → | | | | | return **True** |

### Complexity
> "O(n) time. The outer walk plus the two helper checks together cover each
> character at most about 3 times. O(1) extra space, since I pass indices instead
> of slicing. Slicing with `t == t[::-1]` is simpler to write but uses O(n) space,
> which is worth mentioning as a tradeoff."

---

## Part 3: Follow-ups

| Follow-up | Answer direction |
|-----------|------------------|
| "What if you can delete up to **k** characters?" | Recursion: `check(l, r, k)`. On a mismatch, branch both ways with `k-1`. That's exponential without memoization; add memo on `(l, r, k)`. Or use DP: the minimum deletions to make `s` a palindrome is `n - LPS(s)` (longest palindromic subsequence). |
| "Return *which* index to delete." | At the mismatch: return `l` if `is_pal(l+1, r)` succeeds, `r` if `is_pal(l, r-1)` succeeds, otherwise -1. Ask what to return if no deletion is needed. |
| "Why not greedily pick a side?" | Show the counterexample `"abaabab"`. Being able to *break* your own heuristic is a strong interview signal. |

---

## Part 4: How to comment better

Your comments read like a **debugging log** (what broke). Interview comments
should read like a **design doc** (what's true and why).

**Before (what you wrote):**
```python
# NEEDS:
# basic palindrome checker; left, right two pointer
#   if l != r: return False
# l != r logic change
#   if shifted == True: return False
# naive check for next element does not work
# prioritizes l pointer
```

**After (what to write and say):**
```python
# Brute force: delete each char, check palindrome → O(n^2).
# Insight: outer matching pairs are already fine. At the FIRST mismatch,
#   one of s[l] / s[r] must be deleted. Nearby chars can't tell which,
#   so try both with a plain palindrome check.
# Edge: already a palindrome → True (zero deletions allowed).
# O(n) time, O(1) space.
```

A checklist for every comment block:
1. **Brute force + cost** (one line)
2. **The insight**: why the optimization is *correct*, not only what it does
3. **Edge cases** you've considered
4. **Complexity**

Keep traces and failing test cases in your scratch notes while you work. Once you
understand why something failed, replace the log with the *reason*. "Lookahead
fails because nearby characters can't decide the side" is worth more than the
50-character test string.

---

## 60-second verbal summary

> "Two pointers from both ends. While characters match, move inward. At the first
> mismatch, one of those two characters has to be the deletion, because deleting
> anything between them leaves them still facing each other. I can't tell from
> nearby characters which one, and fixed lookahead can be fooled, so I check both
> options with a plain palindrome check on the remaining range. O(n) time, O(1)
> space, versus O(n²) for trying every deletion."
