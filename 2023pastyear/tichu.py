def numbers_in_text_to_int(line: str, separator: str = ' ') -> list[int]:
  """
  Convert string of numbers to list[int]
  """
  return list(map(int, line.split(separator)))

def solve(input_number: int) -> None:
  # Constants
  input_filename = f'./4-tichu/input{input_number}.txt'
  output_filename = f'./4-tichu/output{input_number}.txt'

  # Open and parse the input file
  with open(input_filename) as f:
    [N, K] = numbers_in_text_to_int(f.readline())
    print(f'N={N} K={K}')
    cards: list[int] = numbers_in_text_to_int(f.readline())

  # Process
  cards = list(set(cards)) # Remove duplicates
  cards.sort() # Sort ascending
  numbered_cards = len(cards) - K
  # print(cards)

  longest_run = 0
  for i in range(numbered_cards):
    run = 1
    wildcards_left = K

    j = 1
    k = 1
    while i+j<len(cards):
      if cards[i+j] == cards[i] + k:
        j += 1
      elif wildcards_left > 0:
        wildcards_left -= 1
      else:
        break
      # print(list(range(cards[i], cards[i]+k)))
      # print(j)
      run += 1
      k += 1
    longest_run = max(run, longest_run)

  longest_run += wildcards_left

  # Output
  with open(output_filename) as f:
    [expected_solution] = numbers_in_text_to_int(f.readline())
  print(f"Expected solution: {expected_solution}", end='\t')
  print(f"My solution: {longest_run}", end='\t')
  print(f"Solutions match = {longest_run==expected_solution}")

for i in range(1,6+1):
  print(f"Input {i}")
  solve(i)
  print()