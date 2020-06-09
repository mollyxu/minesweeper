# Minesweeper game with 3 difficulty levels and customizable grid size
import random


# Beginner: 10 mines square of side length 8-10
dimensions = random.randint(8,10)
grid = [[0 for i in range(dimensions)] for j in range(dimensions)]
for i in grid:
    print(i)

mines = 0
while mines < 10:
    i = random.randint(0, dimensions-1)
    j = random.randint(0, dimensions-1)
    if grid[i][j] == 0:
        grid[i][j] = "*"
        mines += 1 

        # Corner cases   
        if (i == 0 and j == 0):
            if grid[i][j + 1] != "*":
                grid[i][j + 1] += 1
            if grid[i + 1][j + 1] != "*":
                grid[i + 1][j + 1] += 1
            if grid[i + 1][j] != "*":
                grid[i + 1][j] += 1
            
        if (i == 0 and j == dimensions-1):
            if grid[i][j - 1] != "*":
                grid[i][j - 1] += 1
            if grid[i + 1][j - 1] != "*":
                grid[i + 1][j - 1] += 1
            if grid[i + 1][j] != "*":
                grid[i + 1][j] += 1
        if (i == dimensions-1 and j == 0):
            if grid[i][j + 1] != "*":
                grid[i][j + 1] += 1
            if grid[i - 1][j + 1] != "*":
                grid[i - 1][j + 1] += 1
            if grid[i - 1][j] != "*":
                grid[i - 1][j] += 1
        if (i == dimensions-1 and j == dimensions-1):
            if grid[i][j - 1] != "*":
                grid[i][j - 1] += 1
            if grid[i - 1][j - 1] != "*":
                grid[i - 1][j - 1] += 1
            if grid[i - 1][j] != "*":
                grid[i - 1][j] += 1
        
        # edge cases
        if (j == 0 and i != 0 and i <= dimensions-2):
            if grid[i][j + 1] != "*":
                grid[i][j + 1] += 1
            if grid[i+ 1][j + 1] != "*":
                grid[i+ 1][j + 1] += 1
            if grid[i+ 1][j] != "*":
                grid[i+ 1][j] += 1
            if grid[i- 1][j + 1] != "*":
                grid[i- 1][j + 1] += 1
            if grid[i- 1][j] != "*":
                grid[i- 1][j] += 1
                
        if (j == dimensions - 1 and j != 0 and j <= dimensions-2):
            if grid[i][j - 1] != "*":
                grid[i][j - 1] += 1
            if grid[i- 1][j - 1] != "*":
                grid[i- 1][j - 1] += 1
            if grid[i- 1][j] != "*":
                grid[i- 1][j] += 1
            if grid[i+ 1][j - 1] != "*":
                grid[i+ 1][j - 1] += 1
            if grid[i+ 1][j]!= "*":
                grid[i+ 1][j] += 1

        if (i == 0 and j != 0 and j <= dimensions-2):
            if grid[i][j - 1] != "*":
                grid[i][j - 1] += 1
            if grid[i + 1][j - 1] != "*":
                grid[i + 1][j - 1] += 1
            if grid[i + 1][j] != "*":
                grid[i + 1][j] += 1
            if grid[i][j + 1] != "*":
                grid[i][j + 1] += 1
            if grid[i + 1][j + 1] != "*":
                grid[i + 1][j + 1] += 1

        if (i == dimensions - 1 and j != 0 and j <= dimensions-2):
            if grid[i][j - 1] != "*":
                grid[i][j - 1] += 1
            if grid[i - 1][j - 1] != "*":
                grid[i - 1][j - 1] += 1
            if grid[i - 1][j] != "*":
                grid[i - 1][j] += 1
            if grid[i - 1][j + 1] != "*":
                grid[i - 1][j + 1] += 1
            if grid[i][j + 1] != "*":
                grid[i][j + 1] += 1
        
        # all other cases
        elif (i != 0 and j != 0 and i <= dimensions-2 and j <= dimensions-2): 
            if grid[i][j - 1] != "*":
                grid[i][j - 1] += 1
            if grid[i + 1][j] != "*":
                grid[i + 1][j] += 1
            if grid[i + 1][j - 1] != "*":
                grid[i + 1][j - 1] += 1
            if grid[i + 1][j + 1] != "*":
                grid[i + 1][j + 1] += 1
            if grid[i - 1][j - 1] != "*":
                grid[i - 1][j - 1] += 1
            if grid[i - 1][j] != "*":
                grid[i - 1][j] += 1
            if grid[i - 1][j + 1] != "*":
                grid[i - 1][j + 1] += 1
            if grid[i][j + 1] != "*":
                grid[i][j + 1] += 1

board = ""


# Intermediate: 40 mines varies in size between 13x15 and 16x16

# Expert: 99 mines 16x30 or 30x16

# Custom: # of mines = (x-1)(y-1)


