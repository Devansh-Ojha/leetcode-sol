import heapq

class Solution:
    def dijkstra(self, n: int, edges: List[List[int]], start: int) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))  # if undirected graph

        dist = [float('inf')] * n
        dist[start] = 0
        heap = [(0, start)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nei, w in graph[node]:
                if dist[nei] > dist[node] + w:
                    dist[nei] = dist[node] + w
                    heapq.heappush(heap, (dist[nei], nei))

        return dist
