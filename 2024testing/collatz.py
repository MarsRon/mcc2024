def numbers_in_text_to_int(line: str, separator: str = ' ') -> list[int]:
  """
  Convert string of numbers to list[int]
  """
  return list(map(int, line.split(separator)))

def solve(input_number: int) -> None:
  # Constants
  input_filename = f'./collatz/input{input_number}.txt'
  output_filename = f'./collatz/output{input_number}.txt'

  # Open and parse the input file
  with open(input_filename) as f:
    [n, k] = numbers_in_text_to_int(f.readline())
    numbers = numbers_in_text_to_int(f.readline())

  # Process the data
  for _ in range(k):
    for i in range(n):
      if numbers[i] % 2 == 0: # Even
        numbers[i] = numbers[i] / 2
      else: # Odd
        numbers[i] = 3*numbers[i] + 1
  
  final_sum = int(sum(numbers))

  # Output
  print(f"{input_number}. My solution: {final_sum}")
  with open(output_filename, 'w') as f:
    f.write(str(final_sum))

for i in range(3,9+1):
  solve(i)