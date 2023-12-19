import logging
logger = logging.getLogger()


class Rating:
  def __init__(self, rating_str: str):
    self.ratings: dict[str, int] = self.parse_rating_str(rating_str)

  def parse_rating_str(self, rating_str: str) -> dict[str, int]:
    ratings = {}
    rating_str = rating_str[1:-1].split(",")
    for i, r in enumerate(["x", "m", "a", "s"]):
      key = r
      val = int(rating_str[i].split("=")[1])
      ratings[key] = val
    return ratings
  
  def get(self, key: str) -> int:
    return self.ratings[key]

  @property
  def ratings_sum(self) -> int:
    return sum(self.ratings.values())


def check_valid(rule: str, rating: Rating) -> str:
  if rule == "A":
    return "accepted"
  elif rule == "R":
    return "rejected"
  elif ":" in rule:
    validation, next = rule.split(":")
    if "<" in rule:
      key,val = validation.split("<")
      if rating.get(key) < int(val):
        if next == "A":
          return "accepted"
        elif next == "R":
          return "rejected"
        return next
    elif ">" in rule:
      key,val = validation.split(">")
      if rating.get(key) > int(val):
        if next == "A":
          return "accepted"
        elif next == "R":
          return "rejected"
        return next
    return None
  else:
    return rule


def part_1(data: list) -> int:
  """
  part 1
  """
  empty_index = data.index("")
  workflows_list, ratings_list = data[:empty_index], data[empty_index+1:]
  workflows = {}
  total = 0
  for workflow in workflows_list:
    split_index = workflow.index("{")
    workflow_name, rules = workflow[:split_index], workflow[split_index+1:-1].split(",")
    workflows[workflow_name] = rules
  for i in range(len(ratings_list)):
    rating = Rating(ratings_list[i])
    rules = workflows["in"]
    res = None
    while res is None:
      for rule in rules:
        result = check_valid(rule, rating)
        if result is None:
          continue
        if result == "accepted":
          res = "accepted"
          total += rating.ratings_sum
          logger.debug((ratings_list[i], total))
          break
        elif result == "rejected":
          res = "rejected"
          break
        else:
          rules = workflows[result]
          break
  return total


def part_2(data: list) -> int:
  """
  part 2
  """
  return -1      