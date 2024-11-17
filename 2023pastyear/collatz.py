def numbers_in_text_to_int(line: str, separator: str = ' ') -> list[int]:
  """
  Convert string of numbers to list[int]
  """
  return list(map(int, line.split(separator)))

def solve(input_number: int) -> None:
  # Constants
  input_filename = f'./1-collatz/input{input_number}.txt'
  output_filename = f'./1-collatz/output{input_number}.txt'

  # Open and parse the input file
  with open(input_filename) as f:
    [n, k] = numbers_in_text_to_int(f.readline())
    numbers = numbers_in_text_to_int(f.readline())
    # print(f'n={n}')
    # print(f'k={k}')
    # print(f'numbers={numbers}')

  # Process the data
  for _ in range(k):
    for i in range(n):
      if numbers[i] % 2 == 0: # Even
        numbers[i] = numbers[i] / 2
      else: # Odd
        numbers[i] = 3*numbers[i] + 1
  
  final_sum = int(sum(numbers))

  # Output
  with open(output_filename) as f:
    [expected_solution] = numbers_in_text_to_int(f.readline())
  print(f"Expected solution: {expected_solution}", end='\t')
  print(f"My solution: {final_sum}", end='\t')
  print(f"Solutions match = {final_sum==expected_solution}")

for i in range(1,7+1):
  solve(i)