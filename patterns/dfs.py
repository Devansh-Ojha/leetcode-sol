def dfs_iterative(start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        # Process node if needed

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

            
# This is recursive
def dfs(node, visited):
    if node in visited:
        return
    # Mark node as visited
    visited.add(node)
    # Do any processing here (pre-order)
    for neighbor in graph[node]:
        dfs(neighbor, visited)
    # Do any processing here (post-order)


# for the grid
def dfs(r, c):
    if (r < 0 or c < 0 or 
        r >= ROWS or c >= COLS or 
        (r, c) in visited or 
        grid[r][c] == 0):
        return

    visited.add((r, c))

    # Explore 4 directions
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)