class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        rows = range(len(grid))
        cols = range(len(grid[0]))
        minutes = 0

        for row in rows:
            for col in cols:
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                possible_directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for row_dir, col_dir in possible_directions:
                    new_r = r + row_dir
                    new_c = c + col_dir
                    if new_r in rows and new_c in cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2 #mark fresh as rotten
                        fresh -= 1
                        q.append((new_r, new_c))
            minutes += 1
        return minutes if fresh == 0 else -1
                