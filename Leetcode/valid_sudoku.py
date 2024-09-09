class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize data structures to keep track of the numbers we've seen.
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Iterate over each cell in the 9x9 board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':  # Skip empty cells
                    continue

                # Determine which box the current cell belongs to
                box_index = (i // 3) * 3 + j // 3

                # Check if the current number is already seen in the current row, column, or box
                if (num in rows[i]) or (num in columns[j]) or (num in boxes[box_index]):
                    return False  # If found, the board is not valid

                # Add the number to the row, column, and box sets
                rows[i].add(num)
                columns[j].add(num)
                boxes[box_index].add(num)

        # If no conflicts are found, the board is valid
        return True
