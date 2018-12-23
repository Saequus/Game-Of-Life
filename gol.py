class GoL():
    def solveGoL(self, board):
        for y in range(len(board)):
            for x in range(len(board[0])):
                t = board[y][x]
                if t % 2 == 0 and self.n_neighbours(board, x, y, 3):
                    board[y][x] += 2
                elif t % 2 == 1:
                    if self.n_neighbours(board, x, y, 2) or self.n_neighbours(board, x, y, 3):
                        board[y][x] += 2

        for y in range(len(board)):        
            for x in range(len(board[0])):
                board[y][x] >>= 1
        return board

    def n_neighbours(self, board, x, y, target):
        result = 0
        for dx, dy in (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1),
        ):
            if 0 <= x + dx < len(board[0]) and 0 <= y + dy < len(board):
                if board[y+dy][x+dx] % 2 == 1:
                    result += 1
        return result == target

f = GoL()
u = [[1, 1, 0, 1], 
     [0, 1, 0, 0], 
     [1, 0, 0, 0], 
     [1, 0, 0, 1]]

print(f.solveGoL(u))

# the result should be the same;
#     [[1, 1, 1, 0], 
#      [0, 1, 1, 0], 
#      [1, 1, 0, 0], 
#      [0, 0, 0, 0]]




