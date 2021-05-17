
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def count():
    ans = 0
    # stack = []
    print(grid)
    for i, j in enumerate(grid):
        # print(i, j)
        for k, v in enumerate(j):
            # print("Pushing index tupel into stack")
            if v == "1":
                print("Pushing index tupel into stack")
                stack = [(i, k)]
                ans += 1
                print("incrementing ans " , ans)
                # print(stack)
                while stack:
                    row, col = stack.pop()
                    if (0 <= row <= len(grid) and 0 <= col <= len(grid[0]) and grid[row][col] == "1"):
                        grid[row][col] = "0" 
                        print("Replacing 1 by 0")
                        current = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]
                        print(current)
    
    print(ans)

def num_islands()-> int :
    row_count = len(grid)
    col_count = len(grid[0])
    ans = 0
    stack = []
    for i in range(row_count):
        for j in range(col_count):
            if grid[i][j] == "1":
                ans += 1
                stack.append((i, j))
                # print(stack)
                while stack:
                    current_i, current_j = stack.pop()
                    grid[current_i][current_j] = "0"

                    if current_i > 0 and grid[current_i-1][current_j] == "1":
                        stack.append((current_i-1, current_j))
                    
                    if current_i < row_count-1 and grid[current_i+1][current_j] == "1":
                        stack.append((current_i+1, current_j))

                    if current_j > 0 and grid[current_i][current_j-1] == "1":
                        stack.append((current_i, current_j-1))

                    if current_j < col_count-1 and grid[current_i][current_j+1] == "1":
                        stack.append(current_i, current_j+1)
    return ans
    

if __name__ == '__main__':
    # count()
    num_islands()
    