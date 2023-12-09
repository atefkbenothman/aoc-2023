import logging
logger = logging.getLogger()


CARDS = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def get_hand_type(hand: str) -> int:
  """
  find out what the type is for the given hand.
  """
  # count how many of each card we have in our current hand
  card_counts = {}
  for card in hand:
    if card not in card_counts:
      card_counts[card] = 1
    else:
      card_counts[card] += 1

  # find out what type of hand we have
  hand_point = 0

  card_counts_vals = list(set(card_counts.values()))

  # check for joker card
  if "J" in card_counts:
    card_counts_sorted = sorted(card_counts.items(), key=lambda x:x[1], reverse=True)
    max_card = card_counts_sorted[0]
    if max_card[0] == "J":
      if len(card_counts_sorted) == 1:
        card_counts["A"] = 5
      else:
        card_counts[card_counts_sorted[1][0]] += card_counts["J"]
    else:
      card_counts[max_card[0]] += card_counts["J"]
    del card_counts["J"]

    card_counts_vals = list(set(card_counts.values()))

  # five of a kind
  if len(card_counts) == 1 and card_counts_vals[0] == 5:
    logging.debug(f"five of a kind: {hand}")
    hand_point = 7

  # four of a kind
  elif len(card_counts) == 2 and len(card_counts_vals) == 2 and 4 in card_counts_vals and 1 in card_counts_vals:
    logging.debug(f"four of a kind: {hand}")
    hand_point = 6

  # full house
  elif len(card_counts) == 2 and len(card_counts_vals) == 2 and 3 in card_counts_vals and 2 in card_counts_vals:
    logging.debug(f"full house: {hand}")
    hand_point = 5

  # three of a kind
  elif len(card_counts) == 3 and len(card_counts_vals) == 2 and 3 in card_counts_vals and 1 in card_counts_vals:
    logging.debug(f"three of a kind: {hand}")
    hand_point = 4

  # two pair
  elif len(card_counts) == 3 and len(card_counts_vals) == 2 and 2 in card_counts_vals and 1 in card_counts_vals:
    logging.debug(f"two of a pair: {hand}")
    hand_point = 3

  # one pair
  elif len(card_counts) == 4 and len(card_counts_vals) == 2 and 2 in card_counts_vals and 1 in card_counts_vals:
    logging.debug(f"one pair: {hand}")
    hand_point = 2

  # high card
  elif len(card_counts) == 5 and len(card_counts_vals) == 1 and 1 in card_counts_vals:
    logging.debug(f"high card: {hand}")
    hand_point = 1

  else:
    logging.debug("found no type: {card_counts}, {card_counts_vals}")
  
  return hand_point


def convert_hand(hand: str) -> list:
  """
  convert a hand to a list of card strenghs.
  """
  strengths = []
  for card in hand:
    strengths.append(CARDS.index(card))
  return strengths


def rank_cards_strength(hands: list) -> list:
  """
  rank two or more cards based on strength.
  """
  if not hands:
    return []

  updated_hands = []

  for hand in hands:
    converted_hand = convert_hand(hand[0])
    hand = hand + (tuple(converted_hand),)
    updated_hands.append(hand)

  sorted_hands = sorted(updated_hands, key=lambda x: list(x[3]))

  return sorted_hands


def rank_hands(hands: list) -> list:
  """
  given a set of hands, rank them based on their points.
  """
  hand_types = {1: [], 2:[], 3:[], 4: [], 5: [], 6:[], 7:[]}
  for hand in hands:
    cards, bid, point = hand[0], hand[1], hand[2]
    hand_types[point].append(hand)

  ranks = []
  for point, hands in hand_types.items():
    cards_ranked = rank_cards_strength(hands)
    if cards_ranked:
      for card in cards_ranked:
        ranks.append(card)

  return ranks


def part_1(data: list) -> int:
  """
  part 1
  """
  hands_bids_points = []
  for line in data:
    hand = line.split()[0]
    bid = int(line.split()[1])
    hand_type = get_hand_type(hand)
    hands_bids_points.append((hand, bid, hand_type))

  ranks = rank_hands(hands_bids_points)

  total_winnings = 0
  for i, rank in enumerate(ranks):
    bid = rank[1]
    winnings = bid * (i + 1)
    total_winnings += winnings

  return total_winnings


def part_2(data: list) -> int:
  """
  part 2
  """
  hands_bids_points = []
  for line in data:
    hand = line.split()[0]
    bid = int(line.split()[1])
    hand_type = get_hand_type(hand)
    hands_bids_points.append((hand, bid, hand_type))

  ranks = rank_hands(hands_bids_points)

  total_winnings = 0
  for i, rank in enumerate(ranks):
    bid = rank[1]
    winnings = bid * (i + 1)
    total_winnings += winnings

  return total_winnings
