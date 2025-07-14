
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()

        # Process the node here (e.g., print, check, etc.)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# on the grid how
                
def bfs(r, c):
    queue = deque([(r, c)])
    visited = set([(r, c)])

    while queue:
        r, c = queue.popleft()

        # Process current cell here

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 1:
                visited.add((nr, nc))
                queue.append((nr, nc))

