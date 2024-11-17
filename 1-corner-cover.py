QUESTION_NAME = "1-corner-cover"
QUESTION_START = 1
QUESTION_END = 5

def numbers2int(line: str, separator: str = ' ') -> list[int]:
  """Convert string of numbers to list[int]"""
  return [int(x) for x in line.split(separator)]

def solve(input_filename: str, output_filename: str) -> int:
  test_cases = []

  # Open and parse the input file
  with open(input_filename) as f:
    [T] = numbers2int(f.readline())
    for _ in range(T):
      test_case = numbers2int(f.readline())
      test_cases.append(test_case)

  # Process the data
  results = []
  for [n, m, A, B] in test_cases:
    if (A == n and B <= m) or (B == n and A <= m) or (A == m and B <= n) or (B == m and A <= n):
      results.append("YES")
    else:
      results.append("NO")

  final_result = '\n'.join(results)

  # Output
  with open(output_filename, 'w') as f:
    f.write(final_result)

  return final_result

for i in range(QUESTION_START, QUESTION_END+1):
  input_filename = f"./{QUESTION_NAME}/input{i}.txt"
  output_filename = f"./{QUESTION_NAME}/output{i}.txt"
  
  answer = solve(input_filename, output_filename)
  
  print(f"{QUESTION_NAME} Q{i}: {answer}")
