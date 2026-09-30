class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while queue and fresh > 0:
            length = len(queue)

            for i in range(length):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            
            minutes += 1

        return minutes if fresh == 0 else -1