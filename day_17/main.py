import logging
logger = logging.getLogger()


def print_map(data: list[str]) -> None:
  for line in data:
    logger.debug("".join(line))
  return


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  import time
  dirs = [(0,1), (0,-1), (-1,0), (1,0)]

  def bfs():
    pass

  data = [[i for i in row] for row in data]
  heat_loss_map = [[i for i in row] for row in data]
  ROWS = len(data)
  COLS = len(data[0])

  # print_map(data)

  START = (0,0)
  END = (ROWS - 1, COLS - 1)

  return -1


def part_2(data: list) -> int:
  """
  part 2
  """
  return -1