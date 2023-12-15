import logging
logger = logging.getLogger()


def calculate_hash(s: str) -> int:
  """
  calculate the hash of a string
  """
  value = 0
  # for each char, determine its value
  for c in s:
    c_ascii = ord(c)
    value += c_ascii
    value *= 17
    value = value % 256
  return value


def part_1(data: list) -> int:
  """
  part 1
  """
  data = data[0].split(",")
  total_val = 0
  for s in data:
    logger.debug(s)
    hash_val = calculate_hash(s)
    logger.debug(f"hash val: {hash_val}")
    total_val += hash_val
  return total_val


def part_2(data: list) -> int:
  """
  part 2
  """
  data = data[0].split(",")

  boxes = {}

  total_val = 0
  for s in data:
    logger.debug(s)

    # perform step
    if "=" in s:
      label, focal_length = s.split("=")
      label_hash = calculate_hash(label)
      if label_hash not in boxes:
        boxes[label_hash] = [(label, int(focal_length))]
      else:
        # check if there is another lens with the same label
        found = False
        for i, (lens_label, lens_focal_length) in enumerate(boxes[label_hash]):
          if label == lens_label:
            new_lens = (label, focal_length)
            boxes[label_hash][i] = new_lens
            found = True
            break
        if not found:
          boxes[label_hash].append((label, int(focal_length)))
      logger.debug(f"label:{label} hash:{label_hash}, focal_length:{focal_length}")
    elif "-" in s:
      label = s.split("-")[0]
      label_hash = calculate_hash(label)
      # remove the lens with the given label in the relevant boxes
      if label_hash in boxes:
        for i, (lens_label, lens_focal_length) in enumerate(boxes[label_hash]):
          if label == lens_label:
            boxes[label_hash].pop(i)
            if len(boxes[label_hash]) == 0:
              del boxes[label_hash]
      logger.debug(f"label:{label} hash:{label_hash}")
    else:
      logger.debug(f"found no = or - in string: {s}")
      exit(0)

    logger.debug(boxes)

  # calculate focusing power
  total_focusing_power = 0
  for label_hash, boxes in boxes.items():
    count = 1
    for label, focal_length in boxes:
      total_focusing_power += (int(label_hash) + 1) * count * int(focal_length)
      count += 1

  logger.debug("----")

  return total_focusing_power