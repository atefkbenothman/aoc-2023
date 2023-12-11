import logging
logger = logging.getLogger()


# ------------------------- attempt 1 ------------------------- 


# ROWS = 0
# COLS = 0
# IMAGE = []


# def print_image(image: list) -> None:
#   """
#   print the entire grid
#   """
#   for i in image:
#     logger.debug("".join(i))

  
# def get_empty_rows_cols(image: list) -> (list,list):
#   rows = len(image)
#   cols = len(image[0])
#   # track which row indexes to add to image
#   rows_to_add = []
#   for row in range(rows):
#     if "#" not in image[row]:
#       rows_to_add.append(row)

#   # track which col indexes to add to image
#   cols_to_add = []
#   for col in range(cols):
#     no_galaxy = True
#     for row in range(rows):
#       if "#" == image[row][col]:
#         no_galaxy = False
#     if no_galaxy:
#       cols_to_add.append(col)

#   return rows_to_add, cols_to_add


# def expand_image(image: list, part_2: bool = False) -> None:
#   """
#   expand rows and cols that do not contain
#   any galaxies
#   """
#   rows = len(image)
#   cols = len(image[0])
#   # track which row indexes to add to image
#   rows_to_add = []
#   for row in range(rows):
#     if "#" not in image[row]:
#       rows_to_add.append(row)

#   # track which col indexes to add to image
#   cols_to_add = []
#   for col in range(cols):
#     no_galaxy = True
#     for row in range(rows):
#       if "#" == image[row][col]:
#         no_galaxy = False
#     if no_galaxy:
#       cols_to_add.append(col)

#   # logger.debug((len(rows_to_add), len(cols_to_add)))

#   row_offset = 0
#   for row in rows_to_add:
#     logging.debug(f"expanding row {row}")
#     if not part_2:
#       image.insert(row + row_offset, ["."] * cols)
#       row_offset += 1
#     if part_2:
#       for _ in range(999_999):
#         image.insert(row + row_offset, ["."] * cols)
#         row_offset += 1

#   rows = len(image)

#   col_offset = 0
#   for col in cols_to_add:
#     logging.debug(f"expanding col {col}")
#     if not part_2:
#       for row in range(rows):
#         image[row].insert(col + col_offset, ".")
#       col_offset += 1
#     if part_2:
#       for _ in range(999_999):
#         for row in range(rows):
#           image[row].insert(col + col_offset, ".")
#         col_offset += 1

#   cols = len(image[0])

#   # number each galaxy
#   galaxy_id = 1
#   for row in range(rows):
#     for col in range(cols):
#       if image[row][col] == "#":
#         # image[row][col] = str(galaxy_id)
#         galaxy_id += 1

#   return image, galaxy_id - 1


# def find_shortest_path(row: int, col: int, paths_found: set) -> None:
#   """
#   find the shortest path from one galaxy
#   to another
#   """
#   global ROWS, COLS, IMAGE

#   shortest_paths = set()

#   queue = [(row, col, 0)]
#   visited = set()
#   while queue:
#     next_coords = []
#     for _ in range(len(queue)):
#       curr_row, curr_col, steps = queue.pop(0)

#       if IMAGE[curr_row][curr_col] == "#":
#         if ((row, col, curr_row, curr_col) not in paths_found and (curr_row, curr_col, row, col) not in paths_found):
#           shortest_paths.add((curr_row, curr_col, steps))
#           paths_found.add((row, col, curr_row, curr_col))
#           paths_found.add((curr_row, curr_col, row, col))

#       for dir_row, dir_col in [(-1,0), (0,1), (1,0), (0,-1)]:
#         new_row, new_col = curr_row + dir_row, curr_col + dir_col
#         if (
#           new_row in range(ROWS) and
#           new_col in range(COLS) and
#           (new_row, new_col) not in visited
#         ):
#           visited.add((new_row, new_col))
#           next_coords.append((new_row, new_col, steps+1))
#     for coord in next_coords:
#       queue.append(coord)

#   length_of_all_paths = sum([i[-1] for i in shortest_paths])

#   return length_of_all_paths, paths_found


# def part_1(data: list) -> int:
#   """
#   part 1
#   """
#   global IMAGE, ROWS, COLS

#   image = []
#   for d in data:
#     image.append([i for i in d])

#   IMAGE, num_galaxies = expand_image(image)
#   ROWS = len(IMAGE)
#   COLS = len(IMAGE[0])

#   total = 0
#   count = 1
#   paths_found = set()
#   for row in range(ROWS):
#     for col in range(COLS):
#       if IMAGE[row][col] == "#":
#         logger.debug(f"finding shortest path: {count}/{num_galaxies}")
#         length, new_paths_found = find_shortest_path(row, col, paths_found)
#         for path in new_paths_found:
#           paths_found.add(path)
#         total += length
#         logger.debug(f"sum: {length}")
#         logger.debug(f"total: {total}")
#         count += 1
#         logger.debug("---")

#   return -1


# def part_2(data: list) -> int:
#   """
#   part 2
#   """
#   global IMAGE, ROWS, COLS

#   image = []
#   for d in data:
#     image.append([i for i in d])

#   IMAGE, num_galaxies = expand_image(image, part_2=True)
#   ROWS = len(IMAGE)
#   COLS = len(IMAGE[0])

#   total = 0
#   count = 1
#   paths_found = set()
#   for row in range(ROWS):
#     for col in range(COLS):
#       if IMAGE[row][col] == "#":
#         logger.debug(f"finding shortest path: {count}")
#         length, new_paths_found = find_shortest_path(row, col, paths_found)
#         for path in new_paths_found:
#           paths_found.add(path)
#         total += length
#         logger.debug(f"sum: {length}")
#         logger.debug(f"total: {total}")
#         count += 1
#         logger.debug("---")

#   return -1      


# ------------------------- attempt 2 ------------------------- 


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  rows = len(data)
  cols = len(data[0])

  # find all galaxies
  galaxies: list[tuple[int, int]] = []
  for row in range(rows):
    for col in range(cols):
      if data[row][col] == "#":
        galaxies.append((row, col))

  # find empty rows
  empty_rows: list[int] = []
  for row in range(rows):
    is_empty = True
    for g_row, g_col in galaxies:
      if row == g_row:
        is_empty = False
    if is_empty:
      empty_rows.append(row)

  # update galaxy coords based on number of empty rows
  for empty_row in sorted(empty_rows, reverse=True):
    adjusted_galaxies: list[tuple[int, int]] = []
    for g_row, g_col in galaxies:
      if g_row > empty_row:
        adjusted_galaxies.append((g_row + 1, g_col))
      else:
        adjusted_galaxies.append((g_row, g_col))
    galaxies = adjusted_galaxies

  # find empty cols
  empty_cols: list[int] = []
  for col in range(cols):
    is_empty = True
    for g_row, g_col in galaxies:
      if col == g_col:
        is_empty = False
    if is_empty:
      empty_cols.append(col)

  # update galaxy coords based on number of empty cols
  for empty_col in sorted(empty_cols, reverse=True):
    adjusted_galaxies: list[tuple[int, int]] = []
    for g_row, g_col in galaxies:
      if g_col > empty_col:
        adjusted_galaxies.append((g_row, g_col + 1))
      else:
        adjusted_galaxies.append((g_row, g_col))
    galaxies = adjusted_galaxies

  # logger.debug(galaxies)

  total_paths: int = 0

  # for each combination of galaxies, calculate the distance between them
  for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
      row1, col1 = galaxies[i]
      row2, col2 = galaxies[j]
      distance = abs(row1 - row2) + abs(col1 - col2)
      logger.debug(f"({row1},{col1}):({row2},{col2}) distance: {distance}")
      total_paths += distance

  return total_paths


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  rows = len(data)
  cols = len(data[0])

  # find all galaxies
  galaxies: list[tuple[int, int]] = []
  for row in range(rows):
    for col in range(cols):
      if data[row][col] == "#":
        galaxies.append((row, col))

  # find empty rows
  empty_rows: list[int] = []
  for row in range(rows):
    is_empty = True
    for g_row, g_col in galaxies:
      if row == g_row:
        is_empty = False
    if is_empty:
      empty_rows.append(row)

  # update galaxy coords based on number of empty rows
  for empty_row in sorted(empty_rows, reverse=True):
    adjusted_galaxies: list[tuple[int, int]] = []
    for g_row, g_col in galaxies:
      if g_row > empty_row:
        adjusted_galaxies.append((g_row + 999_999, g_col))
      else:
        adjusted_galaxies.append((g_row, g_col))
    galaxies = adjusted_galaxies

  # find empty cols
  empty_cols: list[int] = []
  for col in range(cols):
    is_empty = True
    for g_row, g_col in galaxies:
      if col == g_col:
        is_empty = False
    if is_empty:
      empty_cols.append(col)

  # update galaxy coords based on number of empty cols
  for empty_col in sorted(empty_cols, reverse=True):
    adjusted_galaxies: list[tuple[int, int]] = []
    for g_row, g_col in galaxies:
      if g_col > empty_col:
        adjusted_galaxies.append((g_row, g_col + 999_999))
      else:
        adjusted_galaxies.append((g_row, g_col))
    galaxies = adjusted_galaxies

  # logger.debug(galaxies)

  total_paths: int = 0

  # for each combination of galaxies, calculate the distance between them
  for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
      row1, col1 = galaxies[i]
      row2, col2 = galaxies[j]
      distance = abs(row1 - row2) + abs(col1 - col2)
      logger.debug(f"({row1},{col1}):({row2},{col2}) distance: {distance}")
      total_paths += distance

  return total_paths