import logging
logger = logging.getLogger()

DIRECTIONS = {
  "R": (0,1),
  "D": (1,0),
  "L": (0,-1),
  "U": (-1,0)
}

def print_grid(grid: list[str]) -> None:
  for line in grid:
    print("".join(line))
  return


def part_1(data: list) -> int:
  """
  part 1
  """
  from collections import Counter
  dig_plan = [line.split() for line in data]

  GRID_ROWS = 800
  GRID_COLS = 800
  GRID_START = (GRID_ROWS // 2, GRID_COLS // 2)

  grid = []
  for r in range(GRID_ROWS):
    cols = []
    for c in range(GRID_COLS):
      cols.append(".")
    grid.append(cols)

  grid_output = []
  for r in range(GRID_ROWS):
    cols = []
    for c in range(GRID_COLS):
      cols.append(".")
    grid_output.append(cols)

  curr_row, curr_col = GRID_START
  for plan in dig_plan:
    direction, size, hex_val = plan
    for i in range(int(size)):
      dir_row, dir_col = DIRECTIONS[direction]
      grid_output[curr_row][curr_col] = "#"
      curr_row, curr_col = curr_row + dir_row, curr_col + dir_col

  total = 0

  dirs = [(1,0),(-1,0),(0,1),(0,-1)]
  def bfs(row, col):
    visited = set()
    queue = [(row, col)]
    visited.add((row, col))
    while queue:
      curr_row, curr_col = queue.pop(0)
      grid_output[curr_row][curr_col] = "#"
      for dir_row, dir_col in dirs:
        next_row, next_col = dir_row + curr_row, dir_col + curr_col
        if (
          next_row in range(GRID_ROWS) and
          next_col in range(GRID_COLS) and
          grid_output[next_row][next_col] == "." and
          (next_row, next_col) not in visited
        ):
          queue.append((next_row, next_col))
          visited.add((next_row, next_col))

  found = False
  for row in range(GRID_ROWS):
    if not found:
      for col in range(GRID_COLS):
        if not found:
          if row - 1 in range(GRID_ROWS) and col - 1 in range(GRID_COLS):
            if grid_output[row][col] == "." and grid_output[row][col - 1] == "#" and Counter(grid_output[row])["#"] == 2:
              bfs(row, col)
              found = True

  # print_grid(grid_output)

  for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
      if grid_output[row][col] == "#":
        total += 1

  return total


def part_2(data: list) -> int:
  """
  part 2
  """
  return -1      