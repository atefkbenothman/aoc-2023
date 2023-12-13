import logging
logger = logging.getLogger()


def count_matches(pattern, size, splits):
  logger.debug(f"pattern: {pattern}, size: {size}, splits: {splits}")
  return


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  # records: list[str, list] = [[line.split()[0], [int(x) for x in line.split()[1].split(",")]] for line in data]
  for line in data:
    pattern, splits = line.split()
    pattern = "?".join((pattern,) * 1)
    splits = tuple(map(int, splits.split(","))) * 1
    count_matches(pattern, len(pattern), splits)
  return -1


def part_2(data: list) -> int:
  """
  part 2
  """
  return -1