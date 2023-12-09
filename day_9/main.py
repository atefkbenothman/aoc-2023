import logging
logger = logging.getLogger()


def predict_next_val(history: list, part_1: bool = True) -> int:
  """
  given a list of vals, calculate the next val.
  """
  # calculate next values
  steps = [history]
  while not all(h == 0 for h in history):
    diffs = []
    for i in range(1, len(history)):
      diff = history[i] - history[i - 1]
      diffs.append(diff)
    history = diffs
    steps.append(history)

  steps = steps[::-1]

  # extrapolate
  val_to_add = 0
  for i, step in enumerate(steps):
    logger.debug(step)

    if part_1:
      step.append(val_to_add)
    else:
      step.insert(0, val_to_add)

    if i == len(steps) - 1:
      break

    if part_1:
      val_to_add = val_to_add + steps[i + 1][-1]
    else:
      val_to_add = steps[i + 1][0] - val_to_add

  logger.debug("---")

  for step in steps:
    logger.debug(step)
  
  logger.debug("")

  if part_1:
    return steps[-1][-1]
  else:
    return steps[-1][0]


def part_1(data: list) -> int:
  """
  part 1
  """
  lines = [h.split() for h in data]
  histories = [[int(i) for i in l] for l in lines]
  total = 0
  for history in histories:
    total += predict_next_val(history, part_1=True)
  return total


def part_2(data: list) -> int:
  """
  part 2
  """
  lines = [h.split() for h in data]
  histories = [[int(i) for i in l] for l in lines]
  total = 0
  for history in histories:
    total += predict_next_val(history, part_1=False)
  return total