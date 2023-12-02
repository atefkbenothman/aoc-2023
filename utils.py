def read_input(file_name: str) -> list:
  """
  read the input file to a list.
  """
  data = []
  with open(file_name, "r") as f:
    lines = f.readlines()
    for line in lines:
      data.append(line.strip())
  return data