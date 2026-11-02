# Thinking Out Loud: A Framework for Technical Interviews

The interviewer isn't only grading whether you solve the problem. They're grading
**whether they'd want to debug a problem next to you.** That means they need to
*hear* your reasoning: what you noticed, what you tried, why you threw it away.

A silent, correct solution scores worse than a narrated solution that needed a hint.

Use this framework every time you practice, **including when you're alone.** Talk
out loud to an empty room or record yourself. It feels awkward for about a week.

---

## The 8 steps (45-minute interview budget)

| # | Step | Time | Goal |
|---|------|------|------|
| 1 | Restate | ~0:30 | Prove you understood the problem |
| 2 | Clarify | 2–4 min | Pin down inputs, outputs, and edge cases |
| 3 | Examples | 2–3 min | Build small cases by hand, including edge cases |
| 4 | Brute force | 2–3 min | Get *a* correct answer and state its cost |
| 5 | Optimize | 5–10 min | Find the wasted work and remove it |
| 6 | Plan | 2–3 min | Pseudocode, then get the interviewer's buy-in |
| 7 | Code | 10–15 min | Explain *intent* as you write, not syntax |
| 8 | Test + analyze | 5 min | Trace, check edge cases, give Big-O, follow-ups |

---

### 1. Restate (≈30 seconds)

Say the problem back in your own words, and name the input and output types.

> "So I'm given two non-empty linked lists. Each node holds one digit, and the
> digits are stored least-significant first. I need to return their sum as a
> linked list in the same format. Is that right?"

This catches misreadings before they cost you 20 minutes.

### 2. Clarify

Go through these categories in order. You won't need all of them every time, but
running the list keeps you from forgetting one under pressure.

| Category | Questions to ask |
|----------|------------------|
| **Size** | How big can the input get? (This tells you the target complexity: n ≤ 10⁵ → O(n log n) or better. n ≤ 20 → exponential might be OK.) |
| **Values** | Negatives? Zeros? Duplicates? Value range, and could it overflow? |
| **Shape** | Can it be empty or null? A single element? Already sorted? |
| **Output** | Any order requirement? Return a new structure or modify in place? What do I return if there's no answer? |
| **Mutation** | Am I allowed to modify the input? |
| **Multiplicity** | Is there always exactly one answer? Or zero, or many? |

Phrases you can use:
- "Before I start, I want to check a few edge cases…"
- "Can I assume ___, or should I handle ___?"
- "If ___ happens, what should I return?"

> **Your repo shows this gap.** In `longest-consecutive-sequence/submission-6.py`
> you added `if len(seen) == 0` / `if len(seen) == 1` checks *after* the main
> logic, which looks like a patch for failed test cases. Asking "can the input
> be empty?" up front would have shaped the algorithm from the start.

### 3. Examples

- Work through the given example **by hand**: draw it, write the values.
- Then **make up your own**: the smallest possible input, an edge case, and a case
  that breaks a naive approach.
- **Shrink the problem.** In `reverse-bits` you traced a 6-bit version before
  doing 32 bits. That's exactly right, and you should say it out loud:
  *"Let me try this on 6 bits first so I can see the pattern."*

### 4. Brute force: say it, cost it, then decide

**Always state the brute force, even if you already know the optimal answer.** It:
1. Shows the interviewer you can get *a* correct answer.
2. Gives you a baseline to improve on.
3. Usually shows you where the wasted work is.

Script:
> "The simplest approach is ___. That's O(___) time and O(___) space, because ___.
> I don't think that's good enough for n up to 10⁵, so let me see where the wasted
> work is." *(or: "Would you like me to code this first, or try to optimize?")*

You usually **don't need to code the brute force.** Describe it in 2–3 sentences
and analyze it. Ask the interviewer if you're not sure.

### 5. Optimize: hunt for the bottleneck

Ask yourself these questions **out loud**. They're the core of building intuition:

1. **"What work am I repeating?"** → cache it (hash map, prefix sums, DP)
2. **"What information am I throwing away?"** → keep it (stack, heap, running variable)
3. **"What structure is the input giving me that I'm not using?"** Sorted? Reversed?
   Bounded range? Unusual input formats are often hints.
4. **"At step i, what is the *minimum* I need to remember to decide in O(1)?"**
   This defines your state (a carry, a running max, a window).
5. **"Can I trade space for time?"**
6. **"Does this look like a problem I've seen?"** → see the pattern table below

#### Pattern triggers

| If you see… | Think… | Your repo examples |
|-------------|--------|--------------------|
| "have I seen X?" / complement / counts | Hash set / hash map | `two-integer-sum`, `duplicate-integer`, `anagram-groups` |
| Sorted array, pairs/triples summing to target | Two pointers | `three-integer-sum` |
| Palindrome, compare both ends | Two pointers converging | `is-palindrome` |
| k largest / k smallest / k most frequent | Heap of size k (min-heap for largest). O(n log k) | `kth-largest-*`, `top-k-elements`, `k-closest-points` |
| "Next greater/warmer element" | Monotonic stack | `daily-temperatures` |
| Product/sum of everything except i, range queries | Prefix + suffix arrays | `products-of-array-discluding-self` |
| Linked list middle / cycle | Fast & slow pointers | `middle-of-the-linked-list` |
| Building a new linked list | Dummy head node | `add-two-numbers` (optimal) |
| Powers of 2, missing/single number, bit counts | `n & (n-1)`, XOR cancellation, shifts | `power-of-two`, `missing-number`, `number-of-one-bits`, `counting-bits` |
| Contiguous subarray/substring with a constraint | Sliding window | *(not practiced yet)* |
| Sorted input or monotonic answer space | Binary search | *(not practiced yet)* |
| Trees / graphs / grids | DFS / BFS | *(not practiced yet)* |
| "All combinations / permutations / subsets" | Backtracking | *(not practiced yet)* |
| "Number of ways", min/max cost, overlapping choices | Dynamic programming | `counting-bits` is a small DP |

### 6. Plan: get buy-in before coding

Write 4–8 lines of pseudocode or comments, then ask:

> "Does this approach sound reasonable before I start coding?"

This is the cheapest point to get redirected. Interviewers often hint here.

### 7. Code: explain intent, not syntax

| Don't say | Say |
|-----------|-----|
| "Now I set `dummy` equal to `ListNode` open paren close paren…" | "I'll use a dummy head so I don't have to special-case the first node." |
| *(silence for 3 minutes)* | "This loop handles the case where one list is longer, which I'll come back to test." |
| "Wait, no, um…" | "Actually, I realize this misses ___. Let me fix that." |

- **Use names that say what a variable is.** Don't reuse one variable for several
  types. (Your add-two-numbers `s1` is a string, then an int, then a string, then
  a list, which is hard to narrate.)
- **If you're stuck, say so out loud:** "I'm stuck on how to handle ___. Let me try a
  smaller example." Silence is the worst signal. Saying you're stuck invites help.
- **Remove debug `print`s** before saying you're done (`add-two-numbers`,
  `is-palindrome/submission-2`).

### 8. Test, analyze, and handle follow-ups

1. **Trace your code**, not the algorithm in your head, on a small example. Keep a
   variable table out loud:
   > "First iteration: v1 is 9, v2 is 1, carry is 0, total is 10, so I write 0 and carry 1…"
2. **Check edge cases** from step 2 (empty, one element, all the same, overflow, final carry).
3. **State complexity unprompted:** time *and* space, with a one-line reason.
   > "O(max(m, n)) time because each node is visited once. O(1) extra space, not
   > counting the output list."
4. **Expect follow-ups:** "What if the input were huge / streamed / you couldn't
   modify it / it was in a different order?"

---

## Fallback strategy: lock in partial credit

A correct slow solution beats a fast broken one. Plan for this before the interview.

**Time checkpoints (45-minute interview):**

| Clock | If you have… | Do this |
|-------|--------------|---------|
| ~15 min | No optimal idea yet | **Code the brute force now.** Ask: *"I have a correct O(n²) approach. Can I code it so we have something working, then keep optimizing?"* Most interviewers say yes. |
| ~15 min | An optimal idea you're confident in | Skip coding the brute force, but keep it described out loud as your backup. |
| ~30 min | Optimal code that's mostly done | Trace it. Fix bugs out loud. |
| ~35 min | Optimal code that's badly broken | **Stop digging.** Say: *"I'm going to switch to the brute force so we have a correct solution, then explain the fix for the optimal one."* |
| Last 3 min | Anything | Narrate what's left: the bug, the fix, the complexity. Don't code in silence. |

**How to make the fallback cheap:**
- **Write shared helpers** (`is_pal`, `count`, `is_valid`) as separate functions.
  The brute force and the optimal solution usually share them, so the upgrade is
  a small change, not a rewrite.
- **Keep the brute force simple enough to be obviously right**: slicing, nested
  loops, `sorted()`. Don't optimize it.
- **Use it as a test oracle.** Running both on the same example and getting the
  same answer is a quick check of your optimal code.

**Be honest about where the brute force stands:**
> "This is O(n²), which would time out at n = 10⁵, but it's correct. The bottleneck
> is ___, and here's my idea for removing it…"

A working brute force plus a clear explanation of the optimal idea usually scores
much better than a half-finished optimal solution. At most companies it's not a
guaranteed pass on its own, but it keeps you in the running.

---

## Recovering when things go wrong

| Situation | What to say |
|-----------|-------------|
| No idea where to start | "Let me start with a brute force and work from there." Then do it. |
| Got a hint | "Oh, that's helpful. So if I ___, then ___." Build on it out loud. |
| Found a bug while tracing | "Good, the trace caught something. ___ is wrong because ___." Bugs you find yourself count *for* you. |
| Running out of time | "I'm running short on time, so here's how I'd finish: ___." Narrate the rest. |
| Interviewer is silent | Keep narrating. Ask "Does that make sense so far?" every few minutes. |

---

## Solo practice routine (per problem)

1. **Set a timer for 25 minutes.** Talk out loud the whole time, even alone.
2. **Before coding:** write the clarifying questions, examples, brute force + Big-O,
   and the optimization idea as comments at the top of the file. *Your repo already
   does part of this. Make it a full checklist.*
3. Code it, trace it out loud, submit.
4. **After:** fill in [`problems/_TEMPLATE.md`](problems/_TEMPLATE.md) for any problem
   where you got stuck or needed the solution. Writing down *the one insight you
   missed* is the most valuable part.
5. **Record yourself** on one problem every few days, then watch it back. Count your
   silent gaps longer than 15 seconds and your "ums". Both should go down week to week.
