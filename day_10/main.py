import logging
logger = logging.getLogger()


PIPES = {
  "|": [(-1,0), (1,0)],   # north, south
  "-": [(0,-1), (0,1)],   # west, east
  "L": [(-1,0), (0,1)],   # north, east
  "J": [(-1,0), (0,-1)],  # north, west
  "7": [(1,0),  (0,-1)],  # south, west
  "F": [(1,0),  (0,1)]    # south, east
}

ROWS = 0
COLS = 0
GRID = []


def traverse(row, col) -> int:
  """
  traverse the pipes until there are no more pipes.
  keep track of the number of steps taken
  """
  global ROWS
  global COLS
  global GRID
  
  queue = [(row, col)]
  visited = set()
  steps = 0
  while queue:
    next_tiles = []
    for i in range(len(queue)):
      curr_row, curr_col = queue.pop(0)
      curr_tile = GRID[curr_row][curr_col]
      visited.add((curr_row, curr_col))
      GRID[curr_row][curr_col] = "#"
      if curr_tile == "S":
        d = [(0,-1), (-1,0), (0,1), (1,0)]
        dirs = []
        for d_row, d_col in d:
          n_row, n_col = curr_row + d_row, curr_col + d_col
          if (d_row, d_col) == (0,-1) and GRID[n_row][n_col] in ["-", "L", "F"]:
            dirs.append((d_row, d_col))
          elif (d_row, d_col) == (-1,0) and GRID[n_row][n_col] in ["|", "F", "7"]:
            dirs.append((d_row, d_col))
          elif (d_row, d_col) == (0,1) and GRID[n_row][n_col] in ["-", "7", "J"]:
            dirs.append((d_row, d_col))
          elif (d_row, d_col) == (1,0) and GRID[n_row][n_col] in ["|", "L", "J"]:
            dirs.append((d_row, d_col))
          else:
            pass
      elif curr_tile in ["|", "-", "L", "J", "7", "F"]:
        dirs = PIPES[curr_tile]
      for dir_row, dir_col in dirs:
        new_row = curr_row + dir_row
        new_col = curr_col + dir_col
        if (
          new_row in range(ROWS) and
          new_col in range(COLS) and
          GRID[new_row][new_col] in PIPES and
          (new_row, new_col) not in visited
        ):
          next_tiles.append((new_row, new_col))
    for i in next_tiles:
      queue.append(i)

    steps += 1

  return steps - 1


def part_1(data: list) -> int:
  """
  part 1
  """
  global ROWS
  global COLS
  global GRID

  for i in data:
    row = [j for j in i]
    GRID.append(row)
  ROWS = len(data)
  COLS = len(data[0])

  steps = 0

  for row in range(ROWS):
    for col in range(COLS):
      if GRID[row][col] == "S":
        steps = traverse(row, col)

  for i in GRID:
    print(i)

  return steps


def fill(row, col):
  if not row in range(ROWS) or not col in range(COLS):
    return

  if GRID[row][col] != ".":
    return

  GRID[row][col] = "0"
  dirs = [(0,-1), (-1,0), (0,1), (1,0)]
  for dir_row, dir_col in dirs:
    new_row, new_col = row + dir_row, col + dir_col
    fill(new_row, new_col)
  return


def part_2(data: list) -> int:
  """
  part 2
  """
  import sys
  sys.setrecursionlimit(1000000)

  global ROWS
  global COLS
  global GRID

  for i in data:
    row = [j for j in i]
    GRID.append(row)
  ROWS = len(data)
  COLS = len(data[0])

  steps = 0

  for row in range(ROWS):
    for col in range(COLS):
      if GRID[row][col] == "S":
        steps = traverse(row, col)

  for row in range(ROWS):
    for col in range(COLS):
      if GRID[row][col] != "#":
        GRID[row][col] = "."

  for row in range(ROWS):
    for col in range(COLS):
      if (
        ((
          row == 0 or
          row == ROWS - 1
        ) or
        (
          col == 0 or
          col == COLS - 1
        )) and
        (
          GRID[row][col] == "."
        )
      ):
        fill(row, col)

  dot_count = 0

  for row in range(ROWS):
    for col in range(COLS):
      if GRID[row][col] == ".":
        dot_count += 1
  
  # inside = False
  # for row in range(ROWS):
  #   for col in range(COLS):
  #     if GRID[row][col] in ["-", "F", "7"] and inside:
  #       GRID[row][col] = "I"
  #       dot_counts += 1
  #     if GRID[row][col] in ["|", "J", "L"]:
  #       if inside:
  #         inside = False
  #       else:
  #         inside = True
          
  # for row in range(ROWS):
  #   for col in range(COLS):
  #     if GRID[row][col] == "#":
  #       GRID[row][col] = " "

  for i in GRID:
    print("".join(i))

  return dot_count