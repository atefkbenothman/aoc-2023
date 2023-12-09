import logging
logger = logging.getLogger()


def extract_game_info(info: str) -> dict:
  """
  extract the game information into a dict.
  """
  id = info.split(":")[0].split(" ")[1]
  outcomes = info.split(":")[1]
  sets = outcomes.split(";")
  game_sets = []
  for s in sets:
    set_data = {}
    cubes = s.split(",")
    for cube in cubes:
      color = cube.strip().split()[1]
      count = cube.strip().split()[0]
      set_data[color] = int(count)
    game_sets.append(set_data)
  game_data = {
    "id": id,
    "sets": game_sets
  }
  return game_data


BAG = {
  "red": 12,
  "green": 13,
  "blue": 14
}


def part_1(data: list) -> int:
  """
  part 1
  """
  possible_games = []
  for game in data:
    game_info = extract_game_info(game)
    id = game_info["id"]
    sets = game_info["sets"]
    valid = True
    for s in sets:
      for color, count in s.items():
        if count > BAG[color]:
          valid = False
          break
      if not valid:
        break
    if valid:
      possible_games.append(int(id))
  return sum(possible_games)


def part_2(data: list) -> int:
  """
  part 2
  """
  power = 0
  for game in data:
    colors = {
      "red": 0,
      "green": 0,
      "blue": 0
    }
    game_info = extract_game_info(game)
    sets = game_info["sets"]
    for s in sets:
      for color, count in s.items():
        colors[color] = max(colors[color], count)
    total = 1
    for color, count in colors.items():
      total *= count
    power += total
  return power