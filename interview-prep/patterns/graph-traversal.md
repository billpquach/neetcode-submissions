# Graph Traversal: One Template, Six Adjustments

Your `numIslands` flood fill is the base template. Most NeetCode 150 graph problems
are that template with one or two of the adjustments below.

All code here was tested (scratch tests: components, course schedule including a
"diamond" case, word search, rotting oranges, surrounded regions, and iterative DFS
on a 200×200 grid).

---

## The base template (your numIslands)

```python
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(r, c):
    if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != "1":
        return                      # out of bounds / water / already visited
    grid[r][c] = "0"                # mark visited
    for dr, dc in DIRS:
        dfs(r + dr, c + dc)         # visit ALL neighbors, no early return

count = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == "1":       # every unvisited start = one new component
            count += 1
            dfs(r, c)
```

Four parts: **validity check → mark visited → recurse on neighbors → outer loop over
start points.** Every variation changes one of these parts.

---

## The six adjustments

### Adjustment 1: What does the DFS return?

| Return | When | Rule | Problems |
|--------|------|------|----------|
| **Nothing** | Only marking/sinking cells | Plain recursive calls | Number of Islands, Surrounded Regions |
| **A count** | "How big?" | `return 1 + sum of children`. **Never return inside the neighbor loop** | Max Area of Island |
| **A bool** | "Does a path/cycle exist?" | Early return is correct here: `if dfs(nei): return True` | Word Search, Course Schedule |
| **A best value** | "Longest / deepest" | `return 1 + max(children)` | Longest Increasing Path in a Matrix |

### Adjustment 2: How is "visited" tracked?

| Method | When | Problems |
|--------|------|----------|
| **Change the grid** (`"1"` → `"0"`) | Allowed to mutate the input; cells never need revisiting | Number of Islands, Max Area |
| **`visited` set** | Can't mutate, the graph is an adjacency list, or you need several separate visited sets | Connected Components, Pacific Atlantic (one set per ocean), Clone Graph (dict old → new) |
| **Mark, recurse, unmark** (backtracking) | "Visited" means *on the current path*, so other paths may reuse the cell | **Word Search** |
| **Three states** (unvisited / on current path / done) | Detecting cycles in a **directed** graph | **Course Schedule I & II** |

Ask out loud: *"Can I modify the input?"* That decides between the first two rows.

### Adjustment 3: Where do traversals start?

| Start from | When | Problems |
|------------|------|----------|
| **Every unvisited cell/node** | Counting or measuring components | Number of Islands, Max Area, Connected Components |
| **The border, working inward** | "Which cells can reach the edge?" Reverse the question and start *from* the edge | **Surrounded Regions**, **Pacific Atlantic** |
| **All sources at once** (multi-source BFS) | Something spreads from several places at the same time | **Rotting Oranges**, Walls and Gates |

When a problem asks "can this cell reach X?" for every cell, try starting from X instead.
That's usually one traversal instead of one per cell.

### Adjustment 4: What counts as a neighbor?

| Neighbor rule | Problems |
|---------------|----------|
| 4 directions, same value | Number of Islands, Max Area |
| 8 directions (add diagonals) | Shortest Path in Binary Matrix |
| 4 directions + a **condition** (height ≥ current) | Pacific Atlantic (flowing *uphill* from the ocean) |
| 4 directions + **matches the next character** | Word Search |
| `adj[node]` from an edge list | Every non-grid graph problem |

### Adjustment 5: Grid → adjacency list

Same template. Neighbors come from a dict instead of `DIRS`, and visited is a set:

```python
adj = defaultdict(list)
for a, b in edges:              # undirected: add both directions
    adj[a].append(b)
    adj[b].append(a)

visited = set()
def dfs(node):
    visited.add(node)
    for nei in adj[node]:
        if nei not in visited:
            dfs(nei)

count = 0
for node in range(n):           # same outer loop as numIslands
    if node not in visited:
        count += 1
        dfs(node)
```
This is **Number of Connected Components**: numIslands on a graph.

### Adjustment 6: Need the *shortest* distance? Use BFS, not DFS

DFS goes deep along one path, so the first time it reaches a cell isn't necessarily
the shortest route. BFS explores by layers (distance 1, then 2, …), so the first time
it reaches a cell **is** the shortest distance.

**Multi-source BFS (Rotting Oranges):**
```python
q = deque()
fresh = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 2: q.append((r, c))      # all sources start together
        elif grid[r][c] == 1: fresh += 1

minutes = 0
while q and fresh:
    for _ in range(len(q)):                       # process exactly one layer
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                grid[nr][nc] = 2                  # mark when ADDED, not when popped
                fresh -= 1
                q.append((nr, nc))
    minutes += 1
return minutes if fresh == 0 else -1
```
- `for _ in range(len(q))` lets you count layers (minutes, steps, distance).
- **Mark visited when you add to the queue**, not when you pop. Otherwise the same
  cell can be queued more than once.

Signals for BFS: "minimum steps", "shortest path", "minutes until", "nearest".

---

## Variations worth memorizing

### Backtracking DFS: Word Search
```python
def dfs(r, c, i):
    if i == len(word): return True
    if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
        return False
    tmp, board[r][c] = board[r][c], "#"           # mark: on current path
    found = any(dfs(r + dr, c + dc, i + 1) for dr, dc in DIRS)
    board[r][c] = tmp                             # UNMARK: other paths may use it
    return found
```
**Difference from numIslands:** islands are sunk permanently, because each cell
belongs to exactly one island. In Word Search a cell can belong to many candidate
paths, so you un-mark it when you backtrack.

### Directed cycle detection: Course Schedule
```python
state = [0] * n          # 0 = unvisited, 1 = on current path, 2 = fully explored
def has_cycle(c):
    if state[c] == 1: return True     # reached a node on our own path → cycle
    if state[c] == 2: return False    # already checked, known to be safe
    state[c] = 1
    for nxt in adj[c]:
        if has_cycle(nxt): return True    # early return OK: searching for one thing
    state[c] = 2
    return False
```
**Why one `visited` set isn't enough:** in a "diamond" (0→1, 0→2, 1→3, 2→3), node 3 is
reached twice, but there's no cycle. A single set can't tell "on my current path" (a
cycle) from "finished earlier by another branch" (fine). Course Schedule II is the same
code, plus appending `c` to an ordering when it becomes `2` (topological sort).

### Undirected cycle detection: Graph Valid Tree
Pass the `parent` into DFS, and skip it when looking at neighbors. Reaching any other
visited node means there's a cycle. Also check that `len(edges) == n - 1` and
everything is connected.

### Border-first: Surrounded Regions
```python
# 1. From every border "O", mark connected "O"s as safe ("S")
# 2. Every remaining "O" is surrounded → flip to "X"
# 3. Turn "S" back into "O"
```
Instead of asking, for every region, whether it touches the border, start at the
border and mark what's reachable.

### Iterative DFS (if recursion depth is a concern)
```python
stack = [(r, c)]
grid[r][c] = "0"
while stack:
    cr, cc = stack.pop()
    for dr, dc in DIRS:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
            grid[nr][nc] = "0"
            stack.append((nr, nc))
```
This is the BFS code with `stack.pop()` instead of `q.popleft()`. Python's default
recursion limit is 1000, and a 50×50 all-land grid needs a depth of 2500.

### Union-Find (alternative for connectivity)
Connected Components, Redundant Connection, Graph Valid Tree. Each edge is a
`union(a, b)`. If `find(a) == find(b)` before the union, that edge closes a cycle.
Worth knowing as a second approach to mention after DFS.

---

## NeetCode 150 graphs: which adjustments each needs

| Problem | Adjustments |
|---------|-------------|
| Number of Islands | Base template |
| Max Area of Island | Returns a count |
| Clone Graph | Adjacency list; visited = dict `old → new` |
| Walls and Gates | Multi-source BFS from gates |
| Rotting Oranges | Multi-source BFS, count layers |
| Pacific Atlantic | Start from the borders, two visited sets, neighbor rule "height ≥ current" |
| Surrounded Regions | Start from the border, mark safe, flip the rest |
| Course Schedule | Directed graph, 3-state cycle detection |
| Course Schedule II | Same + record the order (topological sort) |
| Graph Valid Tree | Undirected cycle (skip parent) + connected + `edges == n-1` |
| Number of Connected Components | numIslands on an adjacency list |
| Redundant Connection | Union-Find: the first edge joining already-connected nodes |
| Word Ladder | BFS (shortest), neighbors = words one letter apart |

---

## Questions to ask out loud at the start of any graph problem

1. **What's a node and what's an edge?** (Cell plus 4 directions? Course plus prerequisite? Word plus one-letter change?)
2. **What do I need back from each traversal?** Nothing, a count, a bool, or a distance?
3. **Shortest distance?** → BFS.
4. **Directed with possible cycles?** → 3-state DFS.
5. **Can I mutate the input? Does "visited" need to be undone?** → mutate / set / backtrack.
6. **Where do traversals start?** Every cell, the border, or all sources at once?
7. **How deep can the recursion go?** → mention an iterative stack.
