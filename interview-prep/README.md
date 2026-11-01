# Interview Prep: Communication-First Problem Solving

The goal is to make my thinking audible: clarify, build examples, state a brute force,
find the bottleneck, plan, code, trace, analyze.

| File | What it is |
|------|------------|
| [`01-thinking-out-loud-framework.md`](01-thinking-out-loud-framework.md) | The 8-step spoken framework, phrase scripts, pattern-trigger table, recovery moves |
| [`02-repo-review.md`](02-repo-review.md) | Strengths and gaps found in my NeetCode submissions, with fixes and likely follow-ups |
| [`problems/add-two-numbers.md`](problems/add-two-numbers.md) | Full worked example: review of my submission → spoken interview → optimal → follow-ups |
| [`problems/valid-palindrome-ii.md`](problems/valid-palindrome-ii.md) | Review of my submission: why fixed lookahead fails (counterexample), try-both fix, how to rewrite comments |
| [`problems/_TEMPLATE.md`](problems/_TEMPLATE.md) | Copy this for any problem I got stuck on |

---

## The one-card version (keep this visible while practicing)

1. **Restate** it in my own words.
2. **Clarify:** size? values/overflow? empty/single? output format? can I mutate the input?
3. **Examples:** the given one, plus my own smallest case and edge case. *Shrink the problem.*
4. **Brute force:** say it, give its Big-O, say why it's not enough.
5. **Bottleneck:** What's repeated? What am I throwing away? What structure am I ignoring? What's the minimal state?
6. **Plan** in pseudocode → *"Does this sound good before I code?"*
7. **Code:** narrate *why*, not syntax.
8. **Trace** the code on an edge case with a variable table → **Big-O** → follow-ups.

---

## 4-week plan (about 1 month to interview)

Rule: **every** problem is done out loud with a 25-minute timer. Write the
template for any problem where I needed a hint.

| Week | New topics (NeetCode 150) | Communication focus |
|------|---------------------------|---------------------|
| 1 | Finish Two Pointers, **Sliding Window**, Stack, **Binary Search** | Clarifying questions + writing Big-O on every solution |
| 2 | Rest of Linked List, **Trees** (DFS/BFS), **Tries** | State the brute force first, *every* time, even when I know the optimal answer |
| 3 | **Backtracking**, **Graphs**, Heap review | Stating invariants ("the stack always holds…"); tracing with variable tables |
| 4 | **1-D DP**, Intervals, Greedy, plus mixed review of everything | 2–3 timed mock interviews with a friend or recorded; review the recording for silences and "ums" |

Because the interview is with NVIDIA, also review: bit manipulation (already
strong), and **be ready to explain overflow / integer sizes and memory**. If the
interview might be in C/C++, practice a few problems in it.

### Weekly self-check
- [ ] Did I state the complexity without being asked, every time?
- [ ] Did I ask at least 2 clarifying questions before coding?
- [ ] Did I trace my *code*, not just the idea, before submitting?
- [ ] Longest silent stretch on my recording: ___ seconds (target: < 15)
