# NeetCode 150&#x20;

# -This document is a **concept-first, interview-focused breakdown** of everything you gain from the NeetCode 150 list, with **concrete implementations for every major pattern**.

---

## 1. Arrays & Hashing

### Example: Two Sum

```python
seen = {}
for i, n in enumerate(nums):
    if target - n in seen:
        return [seen[target-n], i]
    seen[n] = i
```

Key trick: trade space for time using a hash map.

---

## 2. Two Pointers

### Example: Valid Palindrome

```python
l, r = 0, len(s)-1
while l < r:
    while l < r and not s[l].isalnum(): l += 1
    while l < r and not s[r].isalnum(): r -= 1
    if s[l].lower() != s[r].lower():
        return False
    l += 1
    r -= 1
return True
```

---

## 3. Sliding Window

### Example: Longest Substring Without Repeating Characters

```python
seen = set()
l = 0
res = 0
for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l += 1
    seen.add(s[r])
    res = max(res, r-l+1)
return res
```

---

## 4. Stack

### Example: Valid Parentheses

```python
stack = []
mp = {')':'(', '}':'{', ']':'['}
for c in s:
    if c in mp:
        if not stack or stack[-1] != mp[c]:
            return False
        stack.pop()
    else:
        stack.append(c)
return not stack
```

---

## 5. Binary Search

### Example: Search in Rotated Sorted Array

```python
l, r = 0, len(nums)-1
while l <= r:
    m = (l+r)//2
    if nums[m] == target: return m
    if nums[l] <= nums[m]:
        if nums[l] <= target < nums[m]: r = m-1
        else: l = m+1
    else:
        if nums[m] < target <= nums[r]: l = m+1
        else: r = m-1
return -1
```

---

## 6. Trees (DFS)

### Example: Max Depth of Binary Tree

```python
def dfs(root):
    if not root: return 0
    return 1 + max(dfs(root.left), dfs(root.right))
```

---

## 7. Trees (BFS)

### Example: Level Order Traversal

```python
from collections import deque
q = deque([root])
res = []
while q:
    level = []
    for _ in range(len(q)):
        node = q.popleft()
        level.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    res.append(level)
```

---

## 8. Graphs

### Example: Number of Islands (BFS)

```python
from collections import deque
def bfs(r,c):
    q = deque([(r,c)])
    grid[r][c] = '0'
    while q:
        x,y = q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]=='1':
                grid[nx][ny] = '0'
                q.append((nx,ny))
```

---

## 9. Dynamic Programming

### Example: Climbing Stairs

```python
if n <= 2: return n
prev2, prev1 = 1, 2
for _ in range(3, n+1):
    prev2, prev1 = prev1, prev1 + prev2
return prev1
```

---

## 10. Backtracking

### Example: Subsets

```python
res = []
def backtrack(i, path):
    res.append(path[:])
    for j in range(i, len(nums)):
        path.append(nums[j])
        backtrack(j+1, path)
        path.pop()
backtrack(0, [])
```

---

## 11. Heaps

### Example: Kth Largest Element

```python
import heapq
heap = nums[:k]
heapq.heapify(heap)
for n in nums[k:]:
    if n > heap[0]: heapq.heapreplace(heap, n)
return heap[0]
```

---

## 12. Greedy

### Example: Jump Game

```python
reach = 0
for i,n in enumerate(nums):
    if i > reach: return False
    reach = max(reach, i+n)
return True
```

---

## 13. Bit Manipulation

### Example: Single Number

```python
res = 0
for n in nums:
    res ^= n
return res
```

---

## Pattern-Level Tricks You MUST Know (With Examples)

This section is the **real interview sauce**. These are the reusable tricks that appear again and again across NeetCode 150.

---

## 1. Prefix Sum Trick

### When to Use

- Subarray sum
- Range queries
- Count of something between indices

### Core Idea

Store cumulative sums so range queries become O(1).

### Example: Subarray Sum Equals K

```python
prefix = {0:1}
curr = 0
res = 0
for n in nums:
    curr += n
    if curr - k in prefix:
        res += prefix[curr-k]
    prefix[curr] = prefix.get(curr,0)+1
return res
```

Interview signal: You understand how to reduce O(n²) → O(n).

---

## 2. Sorting + Logic Collapse

### When to Use

- Order doesn’t matter
- Greedy pairing
- Interval problems

### Example: Merge Intervals

```python
intervals.sort()
res = []
for s,e in intervals:
    if not res or res[-1][1] < s:
        res.append([s,e])
    else:
        res[-1][1] = max(res[-1][1], e)
```

Trick: sorting simplifies state transitions.

---

## 3. Monotonic Stack

### When to Use

- Next greater/smaller element
- Histogram problems
- Span problems

### Core Invariant

Stack is always increasing or decreasing.

### Example: Daily Temperatures

```python
res = [0]*len(T)
stack = []
for i,t in enumerate(T):
    while stack and T[stack[-1]] < t:
        idx = stack.pop()
        res[idx] = i - idx
    stack.append(i)
```

Interview signal: You know how to delay decisions.

---

## 4. Sliding Window with Invariant

### When to Use

- Longest / shortest substring
- At most / at least constraints

### Example: Longest Repeating Character Replacement

```python
count = {}
l = 0
maxf = 0
res = 0
for r in range(len(s)):
    count[s[r]] = count.get(s[r],0)+1
    maxf = max(maxf, count[s[r]])
    while (r-l+1) - maxf > k:
        count[s[l]] -= 1
        l += 1
    res = max(res, r-l+1)
return res
```

Trick: window validity defined by math, not characters.

---

## 5. Binary Search on Answer

### When to Use

- Min/max feasible value
- Monotonic condition

### Example: Koko Eating Bananas

```python
l, r = 1, max(piles)
while l < r:
    m = (l+r)//2
    hours = sum((p+m-1)//m for p in piles)
    if hours <= h:
        r = m
    else:
        l = m+1
return l
```

Mental model: guess → check → shrink range.

---

## 6. DFS Return Values

### Trick

Use DFS return values to propagate info upward.

### Example: Diameter of Binary Tree

```python
diam = 0
def dfs(node):
    nonlocal diam
    if not node: return 0
    l = dfs(node.left)
    r = dfs(node.right)
    diam = max(diam, l+r)
    return 1 + max(l,r)
dfs(root)
return diam
```

---

## 7. BFS Level Control

### Trick

Process BFS level-by-level using queue size.

### Example: Right Side View

```python
res = []
q = deque([root])
while q:
    for i in range(len(q)):
        node = q.popleft()
        if i == 0:
            res.append(node.val)
        if node.right: q.append(node.right)
        if node.left: q.append(node.left)
```

---

## 8. Graph Visited Marking

### Trick

Mark visited early to avoid cycles.

### Example: Clone Graph

```python
oldToNew = {}
def dfs(node):
    if node in oldToNew:
        return oldToNew[node]
    copy = Node(node.val)
    oldToNew[node] = copy
    for nei in node.neighbors:
        copy.neighbors.append(dfs(nei))
    return copy
```

---

## 9. DP State Definition

### Trick

DP = state + transition + base case

### Example: House Robber

```python
prev2, prev1 = 0, 0
for n in nums:
    prev2, prev1 = prev1, max(prev1, prev2+n)
return prev1
```

---

## 10. Backtracking Pruning

### Trick

Undo choice after recursion.

### Example: Permutations

```python
res = []
def backtrack(path):
    if len(path) == len(nums):
        res.append(path[:]); return
    for n in nums:
        if n in path: continue
        path.append(n)
        backtrack(path)
        path.pop()
backtrack([])
```

---

## 11. Heap Size Control

### Trick

Keep heap size fixed for top-k.

### Example: Top K Frequent Elements

```python
count = Counter(nums)
heap = []
for n,f in count.items():
    heapq.heappush(heap,(f,n))
    if len(heap) > k:
        heapq.heappop(heap)
return [n for f,n in heap]
```

---

## 12. Greedy Proof Intuition

### Trick

If a later choice is worse, greedy is safe.

### Example: Gas Station

```python
total = curr = start = 0
for i in range(len(gas)):
    diff = gas[i] - cost[i]
    total += diff
    curr += diff
    if curr < 0:
        start = i+1
        curr = 0
return start if total >= 0 else -1
```

---

## Final Interview Takeaway

If you master **these tricks**, NeetCode 150 becomes repetition, not difficulty.

Next upgrades:

- problem → trick index
- trick → verbal explanation scripts
- pattern-specific edge cases

