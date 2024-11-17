QUESTION_NAME = ""
QUESTION_START = 1
QUESTION_END = 1

def numbers2int(line: str, separator: str = ' ') -> list[int]:
  """Convert string of numbers to list[int]"""
  return [int(x) for x in line.split(separator)]

def solve(input_filename: str, output_filename: str) -> int:
  # Open and parse the input file
  with open(input_filename) as f:
    [n] = numbers2int(f.readline())
    numbers = numbers2int(f.readline())

  # Process the data
  total = sum(numbers)

  # Output
  with open(output_filename, 'w') as f:
    f.write(str(total))

  return total

for i in range(QUESTION_START, QUESTION_END+1):
  input_filename = f"./{QUESTION_NAME}/input{i}.txt"
  output_filename = f"./{QUESTION_NAME}/output{i}.txt"
  
  answer = solve(input_filename, output_filename)
  
  print(f"{QUESTION_NAME} Q{i}: {answer}")
