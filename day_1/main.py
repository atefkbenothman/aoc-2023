import logging
logger = logging.getLogger()


DIGITS = {
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}


def part_1(data: list) -> int:
  """
  part 1
  """
  total = 0
  for line in data:
    digits = []
    for char in line:
      if char.isnumeric():
        digits.append(char)
    total += int(digits[0] + digits[-1])
  return total


def part_2(data: list) -> int:
  """
  part 2
  """
  total = 0
  for line in data:
    occurrences = set()
    for digit in DIGITS.keys():
      start = 0
      while start < len(line):
        index = line.find(digit, start)
        if index != -1:
          occurrences.add((DIGITS[digit], index))
        start += 1
    sorted_occurrences = sorted(occurrences, key=lambda x:x[1])
    first_digit = str(sorted_occurrences[0][0])
    second_digit = str(sorted_occurrences[-1][0])
    total += int(first_digit + second_digit)
  return total