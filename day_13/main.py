import logging
logger = logging.getLogger()

PATTERNS = []

def print_pattern(pattern: list[str]) -> int:
  """
  pretty print a pattern
  """
  # logger.debug("   01234567890123456789")
  for i, row in enumerate(pattern):
    logger.debug(f"{i:02d} {row}")
  logger.debug("")
  return


def get_column_str(pattern: list[str], col_num: int) -> str:
  """
  given a pattern and a column number, construct a string
  of vals for that column
  """
  s = ""
  for row in range(len(pattern)):
    s += pattern[row][col_num]
  return s


def validate_horizontal_reflection(pattern: list[str], row1: int, row2: int) -> bool:
  """
  given two starting rows, expand outward to check to see if
  neighbor rows are equal
  """
  rows = len(pattern)
  is_valid = True
  first_row, last_row = row1, row2
  while first_row in range(rows) and last_row in range(rows):
    if pattern[first_row] != pattern[last_row]:
      is_valid = False
      break
    first_row -= 1
    last_row += 1
  return is_valid


def validate_vertical_reflection(pattern: list[str], col1: int, col2: int) -> bool:
  """
  given two starting cols, expand outward to check to see if
  neighbor cols are equal
  """
  cols = len(pattern[0])
  is_valid = True
  first_col, last_col = col1, col2
  while first_col in range(cols) and last_col in range(cols):
    first_col_str = get_column_str(pattern, first_col)
    last_col_str = get_column_str(pattern, last_col)
    if first_col_str != last_col_str:
      is_valid = False
      break
    first_col -= 1
    last_col += 1
  return is_valid


def part_1(data: list) -> int:
  """
  part 1
  """
  global PATTERNS
  # count num of columns to the left
  num_cols_to_left = 0

  # count num of rows above
  num_rows_above = 0

  # construct list of patterns
  patterns: list[list[str]] = []
  current_pattern = []
  for line in data:
    if len(line) == 0:
      patterns.append(current_pattern)
      current_pattern = []
    else:
      current_pattern.append(line)
  patterns.append(current_pattern)

  # for each pattern, find potential lines of reflections
  for i, pattern in enumerate(patterns):
    logger.debug("---")

    print_pattern(pattern)

    horizontal_potential_lines_of_reflection: list[tuple[int, int]] = []

    # check each row againt another to see
    # if they are equal
    start = 0
    end = len(pattern) - 1
    while start < end:
      first = start
      last = end
      while first < last:
        if pattern[first] == pattern[last]:
          if abs(last - first) == 1:
            horizontal_potential_lines_of_reflection.append((first, last))
        first += 1
      end -= 1

    vertical_potential_lines_of_reflection: list[tuple[int, int]] = []

    # check each column against another to see
    # if they are equal
    start = 0
    end = len(pattern[0]) - 1
    while start < end:
      first = start
      last = end
      while first < last:
        first_col_str = get_column_str(pattern, first)
        last_col_str = get_column_str(pattern, last)
        if first_col_str == last_col_str:
          if abs(last - first) == 1:
            vertical_potential_lines_of_reflection.append((first, last))
        first += 1
      end -= 1

    # validate each potential line of reflection

    valid_row_col: list[tuple[int, int, str]] = []

    if len(vertical_potential_lines_of_reflection) == 0 and len(horizontal_potential_lines_of_reflection) == 0:
      logger.debug("ERR")
      exit(0)

    elif len(horizontal_potential_lines_of_reflection) == 0:
      # for each potential line of reflection,
      # expand outward and check if all rows are equal
      for col1, col2 in vertical_potential_lines_of_reflection:
        if validate_vertical_reflection(pattern, col1, col2):
          valid_row_col.append((col1, col2, "vertical"))

    
    elif len(vertical_potential_lines_of_reflection) == 0:
      # for each potential line of reflection,
      # expand outward and check if all rows are equal
      for row1, row2 in horizontal_potential_lines_of_reflection:
        if validate_horizontal_reflection(pattern, row1, row2):
          valid_row_col.append((row1, row2, "horizontal"))

    else:
      # check both vertical and horizontal
      for row1, row2 in horizontal_potential_lines_of_reflection:
        if validate_horizontal_reflection(pattern, row1, row2):
          valid_row_col.append((row1, row2, "horizontal"))

      for col1, col2 in vertical_potential_lines_of_reflection:
        if validate_vertical_reflection(pattern, col1, col2):
          valid_row_col.append((col1, col2, "vertical"))

    assert len(valid_row_col) == 1

    PATTERNS.append(valid_row_col[0])

    # summarize pattern notes
    logger.debug(valid_row_col)
    val1, val2 = valid_row_col[0][0], valid_row_col[0][1]
    direction = valid_row_col[0][2]

    if direction == "horizontal":
      # count number of rows above horizontal line
      num_rows_above += val1 + 1

    if direction == "vertical":
      # count number of cols to the left of horizontal line
      num_cols_to_left += val1 + 1

    logger.debug("---")

  return num_cols_to_left + (num_rows_above * 100)


def part_2(data: list) -> int:
  """
  part 2
  """
  import copy
  global PATTERNS

  # we need to call part 1 so we can keep track of the original lines of reflection
  part_1(data)

  # count num of columns to the left
  num_cols_to_left = 0

  # count num of rows above
  num_rows_above = 0

  # construct list of patterns
  patterns: list[list[str]] = []
  current_pattern = []
  for line in data:
    if len(line) == 0:
      patterns.append(current_pattern)
      current_pattern = []
    else:
      current_pattern.append([i for i in line])
  patterns.append(current_pattern)

  # for each pattern, find potential lines of reflections
  for i, pattern in enumerate(patterns):
    logger.debug("---")
    print_pattern(pattern)

    valid_row_col: list[tuple[int, int, str]] = []

    for row in range(len(pattern)):
      for col in range(len(pattern[0])):
        pattern2 = copy.deepcopy(pattern)
        if pattern2[row][col] == ".":
          pattern2[row][col] = "#"
        elif pattern2[row][col] == "#":
          pattern2[row][col] = "."
        
        horizontal_potential_lines_of_reflection: list[tuple[int, int]] = []

        # check each row againt another to see
        # if they are equal
        start = 0
        end = len(pattern2) - 1
        while start < end:
          first = start
          last = end
          while first < last:
            if pattern2[first] == pattern2[last]:
              if abs(last - first) == 1:
                horizontal_potential_lines_of_reflection.append((first, last))
            first += 1
          end -= 1

        vertical_potential_lines_of_reflection: list[tuple[int, int]] = []

        # check each column against another to see
        # if they are equal
        start = 0
        end = len(pattern2[0]) - 1
        while start < end:
          first = start
          last = end
          while first < last:
            first_col_str = get_column_str(pattern2, first)
            last_col_str = get_column_str(pattern2, last)
            if first_col_str == last_col_str:
              if abs(last - first) == 1:
                vertical_potential_lines_of_reflection.append((first, last))
            first += 1
          end -= 1

        # validate each potential line of reflection

        if len(vertical_potential_lines_of_reflection) == 0 and len(horizontal_potential_lines_of_reflection) == 0:
          continue

        if len(horizontal_potential_lines_of_reflection) == 0:
          # for each potential line of reflection,
          # expand outward and check if all rows are equal
          for col1, col2 in vertical_potential_lines_of_reflection:
            if validate_vertical_reflection(pattern2, col1, col2):
              if (col1, col2, "vertical") not in valid_row_col and (col1, col2, "vertical") != PATTERNS[i]:
                valid_row_col.append((col1, col2, "vertical"))

        
        elif len(vertical_potential_lines_of_reflection) == 0:
          # for each potential line of reflection,
          # expand outward and check if all rows are equal
          for row1, row2 in horizontal_potential_lines_of_reflection:
            if validate_horizontal_reflection(pattern2, row1, row2):
              if (row1, row2, "horizontal") not in valid_row_col and (row1, row2, "horizontal") != PATTERNS[i]:
                valid_row_col.append((row1, row2, "horizontal"))

        else:
          # check both vertical and horizontal
          for row1, row2 in horizontal_potential_lines_of_reflection:
            if validate_horizontal_reflection(pattern2, row1, row2):
              if (row1, row2, "horizontal") not in valid_row_col and (row1, row2, "horizontal") != PATTERNS[i]:
                valid_row_col.append((row1, row2, "horizontal"))

          for col1, col2 in vertical_potential_lines_of_reflection:
            if validate_vertical_reflection(pattern2, col1, col2):
              if (col1, col2, "vertical") not in valid_row_col and (col1, col2, "vertical") != PATTERNS[i]:
                valid_row_col.append((col1, col2, "vertical"))

    # summarize pattern notes
    logger.debug(valid_row_col)
    val1, val2 = valid_row_col[0][0], valid_row_col[0][1]
    direction = valid_row_col[0][2]

    if direction == "horizontal":
      # count number of rows above horizontal line
      num_rows_above += val1 + 1

    if direction == "vertical":
      # count number of cols to the left of horizontal line
      num_cols_to_left += val1 + 1

    logger.debug("---")

  return num_cols_to_left + (num_rows_above * 100)