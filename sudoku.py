import pprint, timeit

# Find the next empty space
def find_empty(row, column):
  for i in range(row, 9):
    for j in range(column, 9):
      if table[i][j] == 0:
        return i, j
    column = 0
  return -1, -1

# Check if the number in this row and column is valid, returns True if it is
def check_valid(row, column):
  # Check the numbers in the row
  for i, num in enumerate(table[row]):
    if i != column and num == table[row][column]:
      return False

  # Check the numbers in the column
  for index in range(9):
    num = table[index][column]
    if index != row and num == table[row][column]:
      return False

  # Check the numbers in the quadrant
  quad_x = column // 3
  quad_y = row // 3

  for i in range(quad_y*3, quad_y*3 + 3):
    for j in range(quad_x*3, quad_x*3 + 3):
      num = table[i][j]
      if i != row and j != column and num == table[row][column]:
        return False

  return True

def solve():
  i = 0
  pos.append(find_empty(0, 0))

  while 1:
    pos_x = pos[i][0]
    pos_y = pos[i][1]
    check = False

    for num in range(9 - table[pos_x][pos_y]):
      table[pos_x][pos_y] += 1

      if check_valid(pos_x, pos_y):
        check = True
        i += 1

        if pos_y + 1 >= 9:
          pos.append(find_empty(pos_x + 1, 0))
        else:
          pos.append(find_empty(pos_x, pos_y + 1))

        if pos[i][0] == -1:
          return 0

        break

    if check == False:
      table[pos_x][pos_y] = 0
      del pos[i]
      i -= 1
    
pos = []

board1 = [
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

board2 = [
  [1, 0, 0, 0, 0, 0, 7, 6, 0],
  [0, 9, 3, 6, 0, 0, 1, 4, 0],
  [0, 0, 0, 2, 0, 0, 8, 0, 0],
  [0, 0, 0, 0, 0, 0, 5, 0, 3],
  [0, 4, 0, 3, 0, 8, 0, 1, 0],
  [2, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 6, 0, 0, 4, 0, 0, 0],
  [0, 2, 9, 0, 0, 1, 3, 5, 0],
  [0, 7, 5, 0, 0, 0, 0, 0, 1]
]

board3 = [
  [6, 0, 0, 9, 0, 0, 8, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 4],
  [0, 2, 0, 6, 8, 0, 7, 0, 0],
  [0, 0, 0, 0, 0, 1, 6, 0, 9],
  [3, 1, 0, 0, 0, 0, 0, 8, 5],
  [9, 0, 5, 2, 0, 0, 0, 0, 0],
  [0, 0, 7, 0, 1, 4, 0, 2, 0],
  [2, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 4, 0, 0, 6, 0, 0, 3]
]

table = board1.copy()

solve()
pp = pprint.PrettyPrinter(width=29, compact=True)
print('Result:\n')
pp.pprint(table)