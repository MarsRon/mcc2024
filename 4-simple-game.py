QUESTION_NAME = "4-simple-game"
QUESTION_START = 1
QUESTION_END = 11

def numbers2int(line: str, separator: str = ' ') -> list[int]:
  """Convert string of numbers to list[int]"""
  return [int(x) for x in line.split(separator)]

def solve(input_filename: str, output_filename: str) -> int:
  # Open and parse the input file
  with open(input_filename) as f:
    [n] = numbers2int(f.readline())
    cards: list[tuple[int,int]] = []
    for _ in range(n):
      [a, b] = numbers2int(f.readline())
      cards.append((a, b))

  # Process the data
  evirir = 0
  rhae = 0
  
  # Sort desc by importance
  # Importance here means how much it can affect the final results
  # e.g. the more a and b are, the more score Evirir/Rhae can score if they get that card
  # I tried a-b but didnt work, so somehow a+b works
  # Pure luck i guess
  cards.sort(key=lambda x: x[0] + x[1], reverse=True)

  evirir_turn = True
  for card in cards:
    if evirir_turn:
      # Use a
      evirir += card[0]
    else:
      # Use b
      rhae += card[1]
    evirir_turn = not evirir_turn
    # print(f"E {use[1][0]}" if evirir_turn else f"R {use[1][1]}", use[1])

  result = evirir - rhae

  # Output
  with open(output_filename, 'w') as f:
    f.write(str(result))

  return result

for i in range(QUESTION_START, QUESTION_END+1):
  input_filename = f"./{QUESTION_NAME}/input{i}.txt"
  output_filename = f"./{QUESTION_NAME}/output{i}.txt"
  
  answer = solve(input_filename, output_filename)
  
  print(f"{QUESTION_NAME} Q{i}: {answer}")
