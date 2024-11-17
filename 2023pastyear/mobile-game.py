def numbers_in_text_to_int(line: str, separator: str = ' ') -> list[int]:
  """
  Convert string of numbers to list[int]
  """
  return list(map(int, line.split(separator)))


def solve(input_number: int) -> None:
  # Constants
  input_filename = f'./2-mobile-game/input{input_number}.txt'
  output_filename = f'./2-mobile-game/output{input_number}.txt'

  # Open and parse the input file
  with open(input_filename) as f:
    [T] = numbers_in_text_to_int(f.readline())
    # print(f'T={T}')
    test_cases: list[list[int|list[int]]] = []
    for _ in range(T):
      [N, A, B] = numbers_in_text_to_int(f.readline())
      enemies = numbers_in_text_to_int(f.readline())
      test_cases.append([N, A, B, enemies])
    #   print(f'N={N}')
    #   print(f'A={A}')
    #   print(f'B={B}')
    #   print(f'enemies={enemies}')
    # print(test_cases)

  # Process
  for test_case in test_cases:
    [N, A, B, enemies] = test_case
    enemies_killed = 0

    # Repeat until Alice power level reaches B
    while A < B:
      enemies_weaker_than_alice = list(filter(lambda x: x < A, enemies))
      if len(enemies_weaker_than_alice) == 0:
        # Alice cannot kill, aka cannot increase power level
        enemies_killed = -1
        break
      
      largest_enemy = max(enemies_weaker_than_alice)

      # Kill
      A += largest_enemy
      enemies.remove(largest_enemy)
      enemies_killed += 1
      # print(largest_enemy)
      # print(f"A: {A}")
  
    # if enemies_killed == -1:
    #   print("NO SOLUTION: -1")
    # else:
    #   print("Enemies killed", enemies_killed)
    
    test_case.append(enemies_killed)

  # Output
  with open(output_filename) as f:
    expected_solutions = [numbers_in_text_to_int(x)[0] for x in f.readlines()]
  for t in range(T):
    enemies_killed = test_cases[t][4]
    print(f"Expected solution: {expected_solutions[t]}", end='\t')
    print(f"My solution: {enemies_killed}", end='\t')
    print(f"Solutions match = {enemies_killed==expected_solutions[t]}")

for i in range(1,10+1):
  print(f"Input {i}")
  solve(i)
  print()