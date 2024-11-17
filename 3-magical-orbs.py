QUESTION_NAME = "3-magical-orbs"
QUESTION_START = 1
QUESTION_END = 7

def numbers2int(line: str, separator: str = ' ') -> list[int]:
  """Convert string of numbers to list[int]"""
  return [int(x) for x in line.split(separator)]

def solve(input_filename: str, output_filename: str) -> int:
  # Open and parse the input file
  with open(input_filename) as f:
    [T] = numbers2int(f.readline())
    test_cases: list[tuple[int, list[int]]] = []
    for _ in range(T):
      [n] = numbers2int(f.readline())
      numbers = numbers2int(f.readline())
      test_cases.append((n, numbers))

  max_orbs: list[int] = []
  # Process the data
  for test in test_cases:
    [n, numbers] = test
    numbers.sort() # Ascending, aka max numbers at the end
    while len(numbers) > 1:
      y = numbers.pop(-1) # Remove max number
      x = numbers[-1] # 2nd max number
      power = x + 2*y
      numbers[-1] = power # Replace "2nd max number" with new power

    max_orb = numbers[0] % 1000000007 # CHECK OUTPUT FORMAT brah
    max_orbs.append(str(max_orb))

  max_orbs_str = '\n'.join(max_orbs)

  # Output
  with open(output_filename, 'w') as f:
    f.write(max_orbs_str)

  return max_orbs_str

for i in range(QUESTION_START, QUESTION_END+1):
  input_filename = f"./{QUESTION_NAME}/input{i}.txt"
  output_filename = f"./{QUESTION_NAME}/output{i}.txt"
  
  answer = solve(input_filename, output_filename)
  
  print(f"{QUESTION_NAME} Q{i}: {answer}")
