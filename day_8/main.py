import logging
logger = logging.getLogger()


def get_next_node(key: str, step_i: str, steps: list, nodes: dict) -> (str, int):
  """
  given a node key and step (L or R), get the next node's key
  """
  if step_i == len(steps):
    step_i = 0

  curr_node = nodes[key]
  curr_step = steps[step_i]

  if curr_step == "R":
    next_node_key = curr_node[1]
  elif curr_step == "L":
    next_node_key = curr_node[0]
  
  return next_node_key, step_i


def part_1(data: list) -> int:
  """
  part 1
  """
  steps = [s for s in data[0]]
  nodes = {}
  for line in data[2:]:
    name = line.split("=")[0].strip()
    next_nodes = line.split("=")[1].replace("(", "").replace(")", "").replace(" ", "").split(",")
    nodes[name] = next_nodes

  total_steps = 0

  curr = "AAA"
  step_i = 0
  while curr != "ZZZ":
    curr, step_i = get_next_node(curr, step_i, steps, nodes)
    step_i += 1
    total_steps += 1

  return total_steps


def traverse_nodes(key: str, steps: list, nodes: dict) -> int:
  """
  given a node key, count how many steps it takes to
  reach the first 'Z' char.
  """
  total_steps = 0
  step_i = 0
  while key[2] != "Z":
    key, step_i = get_next_node(key, step_i, steps, nodes)
    step_i += 1
    total_steps += 1

  return total_steps


def part_2(data: list) -> int:
  """
  part 2
  """
  from math import lcm
  
  steps = [s for s in data[0]]
  nodes = {}
  for line in data[2:]:
    name = line.split("=")[0].strip()
    next_nodes = line.split("=")[1].replace("(", "").replace(")", "").replace(" ", "").split(",")
    nodes[name] = next_nodes
  
  total_steps = 1

  steps_to_take = [n for n in nodes.keys() if n[2] == "A"]
  for key in steps_to_take:
    total_steps = lcm(total_steps, traverse_nodes(key, steps, nodes))

  return total_steps