import logging
logger = logging.getLogger()


def part_1(data: list) -> int:
  """
  part 1
  """
  # convert input data to list of times and distances
  times = [int(t) for t in data[0].split(":")[1].strip().split()]
  distances = [int(d) for d in data[1].split(":")[1].strip().split()]

  margin_of_error = 1

  # for the length of the race, calculate possible distances you can travel
  for i in range(len(times)):
      race_duration = times[i]
      longest_distance = distances[i]
      distances_possible = []
      # try holding for 0..race_duration
      for hold_time in range(race_duration + 1):
          distance = hold_time * (race_duration - hold_time)
          distances_possible.append(distance)

      # count how many possible ways to win from a list of possible distances
      ways_to_win = len([d for d in distances_possible if d > longest_distance])

      margin_of_error *= ways_to_win

  return margin_of_error


def calculate_ways_to_win(race_duration_start: int, race_duration_end: int, total_race_duration: int, longest_distance):
  """
  calculate total ways to win for a given race.
  """
  ways_to_win = 0
  for hold_time in range(race_duration_start, race_duration_end):
    distance_traveled = hold_time * (total_race_duration - hold_time)
    if distance_traveled > longest_distance:
      ways_to_win += 1
  return ways_to_win


def part_2(data: list) -> int:
  """
  part 2
  """
  import concurrent.futures
  import time

  start = time.perf_counter()

  race_duration = int(data[0].split(":")[1].strip().replace(" ", ""))
  longest_distance = int(data[1].split(":")[1].strip().replace(" ", ""))

  # split up race duration: 100 // 2 = 50 -> [0,50) + [50..101)
  middle = race_duration // 2
  first_half, second_half = [0, middle], [middle, race_duration+1]
  
  ways_to_win = 0

  USE_MULTI_PROCESSING = True

  """
  normal
  """
  if not USE_MULTI_PROCESSING:
    ways_to_win += calculate_ways_to_win(first_half[0], first_half[1], race_duration, longest_distance)
    ways_to_win += calculate_ways_to_win(second_half[0], second_half[1], race_duration, longest_distance)

  """
  multi-processing
  """
  if USE_MULTI_PROCESSING:
    with concurrent.futures.ProcessPoolExecutor() as executor:
      f1 = executor.submit(calculate_ways_to_win, first_half[0], first_half[1], race_duration, longest_distance)
      f2 = executor.submit(calculate_ways_to_win, second_half[0], second_half[1], race_duration, longest_distance)

      ways_to_win = f1.result() + f2.result()

  finish = time.perf_counter()

  logging.debug(f"finished in {round(finish - start, 2)} seconds")

  return ways_to_win