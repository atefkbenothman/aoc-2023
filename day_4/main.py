import logging
logger = logging.getLogger()


def extract_card_info(info: str) -> dict:
  """
  extract contents of card info to a dict.
  """
  id = info.split(":")[0].split()[1]
  numbers = info.split(":")[1]
  winning_numbers = numbers.split("|")[0].strip().split()
  your_numbers = numbers.split("|")[1].strip().split()
  data = {
    "id": id,
    "winning": winning_numbers,
    "have": your_numbers
  } 
  return data


def calculate_card_matching_numbers(card: dict) -> int:
  """
  calculate the number of matching numbers on a card.
  """
  your_nums = set(card["have"])
  count = 0
  for num in card["winning"]:
    if num in your_nums:
      count += 1
  return count


def calculate_card_points(card: dict) -> int:
  """
  calculate the total points for a card.
  """
  count = calculate_card_matching_numbers(card)
  if count == 0:
    return 0
  total = 0
  points = 1
  for _ in range(1, count):
    points = 2 * points
  total += points
  return total


def part_1(data: list) -> int:
  """
  part 1
  """
  total = 0
  for card_info in data:
    card = extract_card_info(card_info)
    points = calculate_card_points(card)
    total += points
  return total


def part_2(data: list) -> int:
  """
  part 2
  """
  # store card IDs and their corresponding match counts.
  card_count_mapping = {}
  for card_info in data:
    card = extract_card_info(card_info)
    card_match_count = calculate_card_matching_numbers(card)
    card_count_mapping[card["id"]] = card_match_count

  # initialize a list to store the count of each card.
  # initiallly, we have 1 count of each card.
  card_counts = [1] * len(data)

  # for each card
  for card_i in range(len(card_counts)):
    # get the number of copies to add to subsequent cards
    num_copies_to_add = card_count_mapping[str(card_i+1)]
    # for each card copy, add the count of the original card to the target card's count
    for j in range(num_copies_to_add):
      card_index_to_add_to = card_i + 1 + j
      card_counts[card_index_to_add_to] += card_counts[card_i]
  return sum(card_counts)