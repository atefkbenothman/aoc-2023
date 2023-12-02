import sys
sys.dont_write_bytecode = True

import os
import argparse
from importlib import import_module
from utils import read_input


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Advent of Code", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
    "--day",
    type=int,
    help="choose a day",
    required=True
  )
  parser.add_argument(
    "--part",
    type=int,
    help="choose which part to run",
    required=True
  )
  parser.add_argument(
    "--example",
    action="store_true",
    default=False,
    help="run the example"
  )
  args = parser.parse_args()

  # day
  day = args.day
  day_dir = f"day_{day}"
  if not os.path.exists(day_dir) and not os.path.isdir(day_dir):
    print(f"day {day} has not been implemented yet!")
    exit(0)

  # part
  part = args.part
  if part < 1 or part > 2:
    print(f"part {part} does not exist!")
    exit(0)

  input_file = f"{day_dir}/input.txt"

  # example
  example = args.example
  if example:
    input_file = f"{day_dir}/example_{part}.txt"

  data = read_input(input_file)

  # import main module dynamically
  main_module = import_module(f"{day_dir}.main")

  # call the part function from the module
  part_function = getattr(main_module, f"part_{part}")
  answer = part_function(data)

  if example:
    print(f"Day {day} Part {part} answer (example): {answer}")
  else:
    print(f"Day {day} Part {part} answer: {answer}")