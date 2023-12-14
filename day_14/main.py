import logging
logger = logging.getLogger()


def print_map(data: list[list[str]]) -> int:
  for line in data:
    logger.debug("".join(line))


def tilt_north(data: list[list[str]]):
  rows = len(data)
  cols = len(data[0])
  for row in range(1, rows):
    for col in range(cols):
      if data[row][col] == "O":
        next_row = row - 1
        while next_row >= 0:
          if data[next_row][col] == ".":
            data[next_row][col] = "O"
            data[next_row + 1][col] = "."
            next_row -= 1
          else:
            break
  return


def tilt_west(data: list[list[str]]):
  rows = len(data)
  cols = len(data[0])
  for row in range(rows):
    for col in range(cols):
      if data[row][col] == "O":
        next_col = col - 1
        while next_col >= 0:
          if data[row][next_col] == ".":
            data[row][next_col] = "O"
            data[row][next_col + 1] = "."
            next_col -= 1
          else:
            break
  return


def tilt_east(data: list[list[str]]):
  rows = len(data)
  cols = len(data[0])
  for row in range(rows):
    for col in reversed(range(cols)):
      if data[row][col] == "O":
        next_col = col + 1
        while next_col < cols:
          if data[row][next_col] == ".":
            data[row][next_col] = "O"
            data[row][next_col - 1] = "."
            next_col += 1
          else:
            break
  return


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  data = [list(i) for i in data]
  rows = len(data)
  cols = len(data[0])

  print_map(data)
  tilt_north(data)
  logger.debug("")
  print_map(data)

  total_sum = 0
  for row in range(rows):
    for col in range(cols):
      if data[row][col] == "O":
        total_sum += (rows - row)

  return total_sum


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  data = [list(i) for i in data]
  rows = len(data)
  cols = len(data[0])

  print_map(data)
  logger.debug("")

  seen: dict[str, int] = {}
  fast_forward = False

  target = 1_000_000_000
  time = 0
  while time < target:
    time += 1
    # tilt
    tilt_north(data)
    tilt_west(data)
    tilt_north(data[::-1]) # south
    tilt_east(data)
    # if we've already seen this grid before,
    # calculate how many steps it took
    grid_hash = str(data)
    if not fast_forward and grid_hash in seen:
      period = time - seen[grid_hash]
      time += ((target - time) // period) * period
      fast_forward = True
    seen[grid_hash] = time

  print_map(data)
  logger.debug("")

  total_sum = 0
  for row in range(rows):
    for col in range(cols):
      if data[row][col] == "O":
        total_sum += (rows - row)

  return total_sum
