import logging
logger = logging.getLogger()


def extract_data(data: list) -> (list,dict):
  """
  extract the seeds, and mappings from the input data.
  """
  # get seeds
  seeds = data[0].split(":")[1].split()

  mappings = data[2:]

  # create a dict to store each mapping
  # for each source category
  source_to_destination = {}

  title = None
  for line in mappings:
    # check when each mapping section ends
    if line:
      # check if its the title
      if len(line.split()) == 2:
        title = line.split()[0]
        source_to_destination[title] = []
      else:
        if title:
          source_to_destination[title].append(line.split())
    else:
      title = None

  return seeds, source_to_destination


def look_up(category: str, num: int, categories: dict) -> int:
  """
  given a category and a number, calculate the cooresponding 
  source to destination number.
  """
  conversion = None
  for mapping in categories[category]:
    range_len, source_start = int(mapping[2]), int(mapping[1])

    if num in range(source_start, source_start + range_len):
      conversion = mapping

  if not conversion:
    return num

  diff = num - int(conversion[1])
  corresponding_num = int(conversion[0]) + diff

  return corresponding_num


def part_1(data: list) -> int:
  """
  part 1
  """
  seeds, source_to_destination = extract_data(data)

  # store all categories and its corresponding mappings to a dict.
  categories = {}

  for title, mappings in source_to_destination.items():
    m = []
    for mapping in mappings:
      m.append(mapping)

    categories[title] = m

  min_location_num = float("inf")
  for seed in seeds:
    key = int(seed)
    for title in categories:
      conversion = look_up(title, key, categories)
      key = conversion
    min_location_num = min(min_location_num, key)

  return min_location_num


def look_up_2(ranges: list, categories: dict):
  """
  given a list of seed ranges and a dictionary of categories
  with their mappings, calculate the corresponding destination 
  ranges after multiple conversions.
  """
  for title in categories:
    updated_ranges = []
    for (destination_start, src_start, range_len) in categories[title]:
      src_end = src_start + range_len
      next_ranges = []
      while ranges:
        (range_start, range_end) = ranges.pop()
        before = (range_start, min(range_end, src_start))
        inter = (max(range_start, src_start), min(src_end, range_end))
        after = (max(src_end, range_start), range_end)
        if before[1] > before[0]:
          next_ranges.append(before)
        if inter[1] > inter[0]:
          updated_ranges.append((inter[0] - src_start + destination_start, inter[1] - src_start + destination_start))
        if after[1] > after[0]:
          next_ranges.append(after)
      ranges = next_ranges
    ranges = ranges + updated_ranges
  return ranges


def part_2(data: list) -> int:
  """
  part 2
  """
  seeds, source_to_destination = extract_data(data)

  # store all categories and its corresponding mappings to a dict.
  categories = {}
  for title, mappings in source_to_destination.items():
    m = []
    for mapping in mappings:
      m.append([int(m) for m in mapping])
    categories[title] = m

  # split up seeds into pairs
  seed_pairs = []
  i = 0
  while i < len(seeds) - 1:
    seed_pairs.append((seeds[i], seeds[i+1]))
    i += 2

  min_location_num = float("inf")
  for pair in seed_pairs:
    start_range, end_range = int(pair[0]), int(pair[0]) + int(pair[1])
    ranges = [(start_range, end_range)]
    updated_ranges = look_up_2(ranges, categories)
    min_location_num = min(min_location_num, min(updated_ranges)[0])

  return min_location_num