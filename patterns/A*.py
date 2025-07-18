import heapq

class Solution:
    def aStar(self, grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> int:
        m, n = len(grid), len(grid[0])
        def h(x, y):
            # Heuristic: Manhattan distance to goal
            return abs(x - goal[0]) + abs(y - goal[1])

        heap = [(h(*start), 0, start)]  # (f = g + h, g = cost so far, position)
        visited = set()

        while heap:
            f, g, (x, y) = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if (x, y) == goal:
                return g

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    if (nx, ny) not in visited:
                        heapq.heappush(heap, (g + 1 + h(nx, ny), g + 1, (nx, ny)))

        return -1  # No path
