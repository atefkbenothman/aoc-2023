import logging
logger = logging.getLogger()


SYMBOLS = ["*", "#", "+", "*", "!", "@", "$", "%", "^", "&", "?", "-", "/", "="]
DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]

def part_1(data: list) -> int:
  rows = len(data)
  cols = len(data[0])
  total = 0
  visited = set()
  for row in range(rows):
    for col in range(cols):
      if (row, col) in visited:
        continue
      if data[row][col].isnumeric():
        num = ""
        i = col
        symbol = None
        while i in range(cols) and data[row][i].isnumeric():
          num += data[row][i]
          visited.add((row,i))
          # check all neighbors for a sybmol
          for dir_row, dir_col in DIRECTIONS:
            new_row = row + dir_row
            new_col = i + dir_col
            if (
              new_row in range(rows) and
              new_col in range(cols) and
              data[new_row][new_col] in SYMBOLS
            ):
              symbol = data[new_row][new_col]
          i += 1
        if symbol:
          total += int(num)
  return total


def part_2(data: list) -> int:
  rows = len(data)
  cols = len(data[0])
  total = 0
  visited = set()
  for row in range(rows):
    for col in range(cols):
      if data[row][col] not in SYMBOLS:
        continue
      nums = []
      for dir_row, dir_col in DIRECTIONS:
        new_row = row + dir_row
        new_col = col + dir_col
        if (
          new_row in range(rows) and
          new_col in range(cols) and
          (new_row, new_col) not in visited and
          data[new_row][new_col].isnumeric()
        ):
          # found a num, find out what the whole value is 
          visited.add((new_row, new_col))
          num = data[new_row][new_col]
          start, end = new_col - 1, new_col + 1
          while (
            (
              new_row in range(rows) and
              start in range(cols) and
              data[new_row][start].isnumeric()
            ) or 
            (
              new_row in range(rows) and
              end in range(cols) and
              data[new_row][end].isnumeric()
            )
          ):
            if start in range(cols) and data[new_row][start].isnumeric():
              num = data[new_row][start] + num
              visited.add((new_row, start))
              start -= 1
            if end in range(cols) and data[new_row][end].isnumeric():
              num = num + data[new_row][end]
              visited.add((new_row, end))
              end += 1
          nums.append(num)
      if len(nums) == 2:
        total += int(nums[0]) * int(nums[1])
  return total