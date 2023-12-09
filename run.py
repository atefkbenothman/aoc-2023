#!/usr/bin/env python3

import sys
sys.dont_write_bytecode = True

import os
import argparse
import logging

from importlib import import_module
from utils import read_input


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Advent of Code", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
    "--day",
    type=int,
    help="choose a day",
    required=False
  )
  parser.add_argument(
    "--part",
    type=int,
    help="choose which part to run",
    required=False
  )
  parser.add_argument(
    "--example",
    action="store_true",
    default=False,
    help="run the example"
  )
  parser.add_argument(
    "--new",
    type=int,
    help="create a new directory for the day",
    required = False
  )
  parser.add_argument(
    "--debug",
    action="store_true",
    default=False,
    help="show print statements",
    required=False
  )
  args = parser.parse_args()

  # logging
  if args.debug:
    red_color_code = '\033[91m'
    reset_color_code = '\033[0m'
    logging.basicConfig(level=logging.DEBUG, format=f"{red_color_code}%(message)s{reset_color_code}")

  # new
  if args.new:
    day_dir_name = f"day_{args.new}"

    if not os.path.exists(day_dir_name):
      os.makedirs(day_dir_name)

      files = [
        "input.txt",
        "example_1.txt",
        "example_2.txt",
        "main.py"
      ]

      for file in files:
        open(f"{day_dir_name}/{file}", "w")

    exit(0)

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

  if not os.path.exists(input_file):
    print(f"{input_file} does not exist!")
    exit(0)

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
