class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visit = set()
        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                possible_moves = [[1,0], [0,1], [-1,0], [0,-1]]
                row, col = q.popleft()
                for row_dir, col_dir in possible_moves:
                    new_row = row + row_dir
                    new_col = col + col_dir
                    if new_row in range(len(grid)) and new_col in range(len(grid[0])) and (new_row, new_col) not in visit and grid[new_row][new_col] == "1":
                        visit.add((new_row, new_col))
                        q.append((new_row, new_col))
                        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visit:
                    visit.add((row, col))
                    bfs(row, col)
                    islands += 1
        return islands
                