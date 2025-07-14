class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Need to use BFS as we are trying to get all rotten ones
        #dfs will cause time problem

        rows = len(grid)
        cols=len(grid[0])

        fresh=0
        time=0
        rot= collections.deque()

        #getting all the fresh ones and appending location of rotten ones
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]==1):
                    fresh+=1
                if(grid[i][j]==2):
                    rot.append((i,j))
        
        directions=([0,1],[0,-1],[1,0],[-1,0])
        #for BFS
            # Now while we got fresh and rot
            # then pop the coordinates  then go over direction to change it to 2
        
        while (fresh>0 and rot):
            length= len(rot)
            for q in range(length):
                r,c=rot.popleft()

                for dr, dc in directions:
                    new_r,new_c = r+dr, c+dc

                    if (0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1):
                        grid[new_r][new_c]=2
                        rot.append((new_r,new_c))
                        fresh-=1
            time+=1

        return time if fresh == 0 else -1