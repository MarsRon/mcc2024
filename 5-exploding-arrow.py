QUESTION_NAME = "5-exploding-arrow"
QUESTION_START = 1
QUESTION_END = 8

def numbers2int(line: str, separator: str = ' ') -> list[int]:
  """Convert string of numbers to list[int]"""
  return [int(x) for x in line.split(separator)]

def solve(input_filename: str, output_filename: str) -> int:
  # Open and parse the input file
  with open(input_filename) as f:
    [N, M, K] = numbers2int(f.readline())
    targets = numbers2int(f.readline())

  def calc_damage(X, i, j):
    """calculate the damage at target j given target i and X (power)"""
    return M * X - (j - i)*(j - i)

  def destroyed_all(X, N, K, array):
    """Returns True if the given X value can destroy all targets"""
    # Copy the targets array -> Doesn't affect the original array
    array = array[:]

    arrows_used = 0
    current_target = 0
    while current_target < N:
      # If current target is alive
      if array[current_target] > 0:
        arrows_used += 1
        if arrows_used > K: # already spent all arrows, not a feasible solution
          return False
        # Fire arrow at target i
        last_target = current_target
        while last_target < N and calc_damage(X, current_target, last_target) > 0:
          # tembak them i to j targets muahahahaha
          array[last_target] -= calc_damage(X, current_target, last_target)
          last_target += 1
      else:
        # kesian, current target died, we move onto next target and see if they still alive
        current_target += 1
    return True

  # Binary search the lowest X possible
  X, high = 1, max(targets)*2 # times 2 just to be safe idk
  while X < high:
    mid = (X + high) // 2
    # We check if can bomb every target... boom. (im not terorist pls no report)
    if destroyed_all(mid, N, K, targets):
      # still can be lower
      high = mid
    else:
      # still can be higher
      X = mid + 1
  result = X

  # Output
  with open(output_filename, 'w') as f:
    f.write(str(result))

  return result

for i in range(QUESTION_START, QUESTION_END+1):
  input_filename = f"./{QUESTION_NAME}/input{i}.txt"
  output_filename = f"./{QUESTION_NAME}/output{i}.txt"
  
  answer = solve(input_filename, output_filename)
  
  print(f"{QUESTION_NAME} Q{i}: {answer}")
