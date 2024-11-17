QUESTION_NAME = "2-gifts"
QUESTION_START = 1
QUESTION_END = 10

def numbers2int(line: str, separator: str = ' ') -> list[int]:
  """Convert string of numbers to list[int]"""
  return [int(x) for x in line.split(separator)]

def solve(input_filename: str, output_filename: str) -> int:
  # Open and parse the input file
  with open(input_filename) as f:
    [n, m] = numbers2int(f.readline())
    tiers = numbers2int(f.readline())

  # Process the data
  gifts = ['0'] * n # list of n zeros
  guests = list(enumerate(tiers)) # (index, tier)
  guests.sort(key=lambda x: (x[1], x[0])) # sort by tier, then index ascending
  # the above line basically sorts the guests in descending importance:
  # lower tier first, then first come first serve (lower index first)
  
  for (index, tier) in guests:
    if m > 0:
      # if we still have
      gifts[index] = '1'
      m -= 1
    else:
      break
    

  # current_tier = 1
  # while m > 0:
  #   for i, t in enumerate(tiers):
  #     if m <= 0:
  #       break
  #     if t == current_tier:
  #       gifts[i] = '1'
  #       m -= 1
  #   current_tier += 1

  gifts_str = ' '.join(gifts)

  # Output
  with open(output_filename, 'w') as f:
    f.write(gifts_str)

  return gifts_str

for i in range(QUESTION_START, QUESTION_END+1):
  input_filename = f"./{QUESTION_NAME}/input{i}.txt"
  output_filename = f"./{QUESTION_NAME}/output{i}.txt"
  
  answer = solve(input_filename, output_filename)
  
  print(f"{QUESTION_NAME} Q{i}: {answer}")
