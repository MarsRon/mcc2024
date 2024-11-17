def numbers_in_text_to_int(line: str, separator: str = ' ') -> list[int]:
  """
  Convert string of numbers to list[int]
  """
  return list(map(int, line.split(separator)))

def solve(input_number: int) -> None:
  # Constants
  input_filename = f'./5-rectangles/input{input_number}.txt'
  output_filename = f'./5-rectangles/output{input_number}.txt'

  # Open and parse the input file
  with open(input_filename) as f:
    [N, K] = numbers_in_text_to_int(f.readline())
    print(f'N={N} K={K}')
    rectangles: list[tuple[int,int]] = []
    for _ in range(N):
      (h, w) = numbers_in_text_to_int(f.readline())
      rectangles.append((h, w))
    print(rectangles)

  # Process
  1

  # Output
  # with open(output_filename) as f:
  #   [expected_solution] = numbers_in_text_to_int(f.readline())
  # print(f"Expected solution: {expected_solution}", end='\t')
  # print(f"My solution: {longest_run}", end='\t')
  # print(f"Solutions match = {longest_run==expected_solution}")

for i in range(1,1+1):
  print(f"Input {i}")
  solve(i)
  print()