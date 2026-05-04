class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fruits = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fruits += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        minutes = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue and fruits:
            minutes += 1

            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        fruits -= 1
                        queue.append((r, c))
        
        return minutes if not fruits else -1
                
