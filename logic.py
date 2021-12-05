import random

def print_grid(grid):
    print("┌─┬─┬─┐")
    c = 0
    while c < len(grid):
        print(f"│{'│'.join(grid[c])}│")
        if c != len(grid) - 1: print("├─┼─┼─┤")
        c += 1
    print("└─┴─┴─┘")

def check(grid):
    for row in grid:
        row = ''.join(row)
        if row in ("XXX", "OOO"):
            return row[0]
    
    for c in range(3):
        row = [grid[x][c] for x in range(3)]
        row = ''.join(row)
        if row in ("XXX", "OOO"):
            return row[0]

    row = []
    for c in range(3):
        row.append(grid[c][c])
    row = ''.join(row)
    if row in ("XXX", "OOO"):
        return row[0]

    row = []
    for c in range(3):
        row.append(grid[c][2 - c])
    row = ''.join(row)
    if row in ("XXX", "OOO"):
        return row[0]

    g = ""
    for row in grid:
        g += ''.join(row)
    if " " not in g:
        return "tie"

    return None  

class tictactoe:
    def __init__(self):
        self.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
    
    def step(self, move):
        x, y = move
        self.grid[x][y] = "X"

        if check(self.grid) is not None: return "check result"
        # AI
        aiChoice = self.ai()
        self.grid[aiChoice[0]][aiChoice[1]] = "O"
        return aiChoice
    
    def ai(self):
        emptySquares = []
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == " ":
                    emptySquares.append((i, j))
        
        return random.choice(emptySquares)
        