def numbers_in_text_to_int(line: str, separator: str = ' ') -> list[int]:
  """
  Convert string of numbers to list[int]
  """
  return list(map(int, line.split(separator)))

def solve(input_number: int) -> None:
  # Constants
  input_filename = f'./3-innovation/input{input_number}.txt'
  output_filename = f'./3-innovation/output{input_number}.txt'

  # Open and parse the input file
  with open(input_filename) as f:
    [n, m] = numbers_in_text_to_int(f.readline())
    print(f'n={n} m={m}')
    cards: list[tuple[int]] = []
    for _ in range(n):
      [a, b, c, d] = numbers_in_text_to_int(f.readline())
      # Add them by default because we are only comparing a+b and c+d
      ab = a + b
      cd = c + d
      cards.append((ab, cd))
    # print(cards)

  # Process
  cards.sort(key=lambda x: x[0], reverse=True)
  max_ABs = [x[0] for x in cards[:m-1]]
  
  max_points = 0
  for i in range(n):
    if i <= m:
      max_points = max(max_points, cards[i][1] + sum(max_ABs))
    else:
      max_points = max(max_points, cards[i][0] + cards[i][1] + sum(max_ABs) - cards[m-1][0])

  # Output
  with open(output_filename) as f:
    [expected_solution] = numbers_in_text_to_int(f.readline())
  print(f"Expected solution: {expected_solution}", end='\t')
  print(f"My solution: {max_points}", end='\t')
  print(f"Solutions match = {max_points==expected_solution}")

for i in range(1,8+1):
  print(f"Input {i}")
  solve(i)
  print()