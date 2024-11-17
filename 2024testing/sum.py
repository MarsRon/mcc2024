from math import sqrt

def numbers_in_text_to_int(line: str, separator: str = ' ') -> list[int]:
  """
  Convert string of numbers to list[int]
  """
  return list(map(int, line.split(separator)))

def solve() -> None:
  # Constants
  input_filename = f'./sum.txt'

  # Open and parse the input file
  with open(input_filename) as f:
    [n] = numbers_in_text_to_int(f.readline())
    numbers = numbers_in_text_to_int(f.readline())

  # Process the data
  total = sum(numbers)

  # Output
  print(f"My solution: {total}")

solve()