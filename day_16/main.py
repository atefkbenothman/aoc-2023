import logging
logger = logging.getLogger()

import sys
sys.setrecursionlimit(100000)


def print_map(data: list[str]) -> None:
  for i, line in enumerate(data):
    logger.debug(f"{''.join(line)}")
  return


SPLITTERS = {
  "|": [(-1,0), (1,0)], # up, down
  "-": [(0,-1), (0,1)]  # left, right
}

MIRRORS = {
  "\\": [],
  "/": []
}

DIRECTIONS = {
  "up": (-1,0),
  "right": (0,1),
  "down": (1,0),
  "left": (0,-1)
}


def part_1(data: list) -> int:
  """
  part 1
  """
  data = [[i for i in row] for row in data]
  beam_map = [[i for i in row] for row in data]
  ROWS = len(data)
  COLS = len(data[0])

  print_map(data)
  print()

  visited = set()

  def dfs(coords: tuple[int, int], direction: str):
    nonlocal visited
    curr_row, curr_col = coords
    if curr_row not in range(ROWS) or curr_col not in range(COLS):
      return
    curr_tile = data[curr_row][curr_col]
    beam_map[curr_row][curr_col] = "#"
    # logger.debug(f"{coords} '{curr_tile}' {direction}")
    if (curr_row, curr_col, direction) in visited:
      return
    visited.add((curr_row, curr_col, direction))
    if curr_tile == ".":
      dir_row, dir_col = DIRECTIONS[direction]
      next_row, next_col = curr_row + dir_row, curr_col + dir_col
      dfs((next_row, next_col), direction)
    elif curr_tile in SPLITTERS:
      if curr_tile == "|":
        if direction == "right" or direction == "left":
          # go up
          dir_row_up, dir_col_up = DIRECTIONS["up"]
          next_row_up, next_col_up = curr_row + dir_row_up, curr_col + dir_col_up
          dfs((next_row_up, next_col_up), "up")
          # go down
          dir_row_down, dir_col_down = DIRECTIONS["down"]
          next_row_down, next_col_down = curr_row + dir_row_down, curr_col + dir_col_down
          dfs((next_row_down, next_col_down), "down")
        elif direction == "up" or direction == "down":
          dir_row, dir_col = DIRECTIONS[direction]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), direction)
        else:
          logger.debug("error 3")
          exit(0)
      elif curr_tile == "-":
        if direction == "up" or direction == "down":
          # go left
          dir_row_left, dir_col_left = DIRECTIONS["left"]
          next_row_left, next_col_left = curr_row + dir_row_left, curr_col + dir_col_left
          dfs((next_row_left, next_col_left), "left")
          # go right
          dir_row_right, dir_col_right = DIRECTIONS["right"]
          next_row_right, next_col_right = curr_row + dir_row_right, curr_col + dir_col_right
          dfs((next_row_right, next_col_right), "right")
        elif direction == "right" or "left":
          dir_row, dir_col = DIRECTIONS[direction]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), direction)
        else:
          logger.debug("error 4")
          exit(0)
      else:
        logger.debug("error 2")
        exit(0)
    elif curr_tile in MIRRORS:
      if curr_tile == "/":
        if direction == "right":
          # go up
          dir_row, dir_col = DIRECTIONS["up"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "up")
        elif direction == "left":
          # go down
          dir_row, dir_col = DIRECTIONS["down"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "down")
        elif direction == "up":
          # go right
          dir_row, dir_col = DIRECTIONS["right"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "right")
        elif direction == "down":
          # go left
          dir_row, dir_col = DIRECTIONS["left"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "left")
        else:
          logger.debug("error 6")
          exit(0)
      elif curr_tile == "\\":
        if direction == "right":
          # go down
          dir_row, dir_col = DIRECTIONS["down"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "down")
        elif direction == "left":
          # go up
          dir_row, dir_col = DIRECTIONS["up"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "up")
        elif direction == "up":
          # go left
          dir_row, dir_col = DIRECTIONS["left"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "left")
        elif direction == "down":
          # go right
          dir_row, dir_col = DIRECTIONS["right"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "right")
        else:
          logger.debug("error 7")
          exit(0)
      else:
        logger.debug("error 5")
        exit(0)
    else:
      logger.debug("error 1")
      exit(0)

  # start traversing by going east
  dfs((0,0), "right")

  print()
  print_map(beam_map)

  # traverse map, count number of "#'s"
  total = 0
  for row in range(ROWS):
    for col in range(COLS):
      if beam_map[row][col] == "#":
        total += 1

  return total


def part_2(data: list) -> int:
  """
  part 2
  """
  def dfs(coords: tuple[int, int], direction: str):
    nonlocal visited
    curr_row, curr_col = coords
    if curr_row not in range(ROWS) or curr_col not in range(COLS):
      return
    curr_tile = data[curr_row][curr_col]
    beam_map[curr_row][curr_col] = "#"
    # logger.debug(f"{coords} '{curr_tile}' {direction}")
    if (curr_row, curr_col, direction) in visited:
      return
    visited.add((curr_row, curr_col, direction))
    if curr_tile == ".":
      dir_row, dir_col = DIRECTIONS[direction]
      next_row, next_col = curr_row + dir_row, curr_col + dir_col
      dfs((next_row, next_col), direction)
    elif curr_tile in SPLITTERS:
      if curr_tile == "|":
        if direction == "right" or direction == "left":
          # go up
          dir_row_up, dir_col_up = DIRECTIONS["up"]
          next_row_up, next_col_up = curr_row + dir_row_up, curr_col + dir_col_up
          dfs((next_row_up, next_col_up), "up")
          # go down
          dir_row_down, dir_col_down = DIRECTIONS["down"]
          next_row_down, next_col_down = curr_row + dir_row_down, curr_col + dir_col_down
          dfs((next_row_down, next_col_down), "down")
        elif direction == "up" or direction == "down":
          dir_row, dir_col = DIRECTIONS[direction]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), direction)
        else:
          logger.debug("error 3")
          exit(0)
      elif curr_tile == "-":
        if direction == "up" or direction == "down":
          # go left
          dir_row_left, dir_col_left = DIRECTIONS["left"]
          next_row_left, next_col_left = curr_row + dir_row_left, curr_col + dir_col_left
          dfs((next_row_left, next_col_left), "left")
          # go right
          dir_row_right, dir_col_right = DIRECTIONS["right"]
          next_row_right, next_col_right = curr_row + dir_row_right, curr_col + dir_col_right
          dfs((next_row_right, next_col_right), "right")
        elif direction == "right" or "left":
          dir_row, dir_col = DIRECTIONS[direction]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), direction)
        else:
          logger.debug("error 4")
          exit(0)
      else:
        logger.debug("error 2")
        exit(0)
    elif curr_tile in MIRRORS:
      if curr_tile == "/":
        if direction == "right":
          # go up
          dir_row, dir_col = DIRECTIONS["up"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "up")
        elif direction == "left":
          # go down
          dir_row, dir_col = DIRECTIONS["down"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "down")
        elif direction == "up":
          # go right
          dir_row, dir_col = DIRECTIONS["right"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "right")
        elif direction == "down":
          # go left
          dir_row, dir_col = DIRECTIONS["left"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "left")
        else:
          logger.debug("error 6")
          exit(0)
      elif curr_tile == "\\":
        if direction == "right":
          # go down
          dir_row, dir_col = DIRECTIONS["down"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "down")
        elif direction == "left":
          # go up
          dir_row, dir_col = DIRECTIONS["up"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "up")
        elif direction == "up":
          # go left
          dir_row, dir_col = DIRECTIONS["left"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "left")
        elif direction == "down":
          # go right
          dir_row, dir_col = DIRECTIONS["right"]
          next_row, next_col = curr_row + dir_row, curr_col + dir_col
          dfs((next_row, next_col), "right")
        else:
          logger.debug("error 7")
          exit(0)
      else:
        logger.debug("error 5")
        exit(0)
    else:
      logger.debug("error 1")
      exit(0)

  data = [[i for i in row] for row in data]
  ROWS = len(data)
  COLS = len(data[0])

  top_row = []
  bottom_row = []
  left_cols = []
  right_cols = []

  for row in range(ROWS):
    for col in range(COLS):
      if row == 0:
        top_row.append((row, col))
      if col == 0:
        left_cols.append((row, col))
      if row == ROWS - 1:
        bottom_row.append((row, col))
      if col == COLS - 1:
        right_cols.append((row, col))

  max_total = 0

  for row, col in top_row:
    beam_map = [[i for i in row] for row in data]
    visited = set()
    dfs((row, col), "down")

    # traverse map, count number of "#'s"
    total = 0
    for row in range(ROWS):
      for col in range(COLS):
        if beam_map[row][col] == "#":
          total += 1

    max_total = max(max_total, total)

  for row, col in bottom_row:
    beam_map = [[i for i in row] for row in data]
    visited = set()
    dfs((row, col), "up")

    # traverse map, count number of "#'s"
    total = 0
    for row in range(ROWS):
      for col in range(COLS):
        if beam_map[row][col] == "#":
          total += 1

    max_total = max(max_total, total)

  for row, col in left_cols:
    beam_map = [[i for i in row] for row in data]
    visited = set()
    dfs((row, col), "right")

    # traverse map, count number of "#'s"
    total = 0
    for row in range(ROWS):
      for col in range(COLS):
        if beam_map[row][col] == "#":
          total += 1

    max_total = max(max_total, total)

  for row, col in right_cols:
    beam_map = [[i for i in row] for row in data]
    visited = set()
    dfs((row, col), "left")

    # traverse map, count number of "#'s"
    total = 0
    for row in range(ROWS):
      for col in range(COLS):
        if beam_map[row][col] == "#":
          total += 1

    max_total = max(max_total, total)

  return max_total