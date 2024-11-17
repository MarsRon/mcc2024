from math import pow
from itertools import chain, combinations
from tqdm import tqdm

def numbers_in_text_to_int(line: str, separator: str = ' ') -> list[int]:
  """
  Convert string of numbers to list[int]
  """
  return list(map(int, line.split(separator)))

def powerset(s: list):
  "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
  return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

def solve(input_number: int) -> None:
  # Constants
  input_filename = f'./6-sumk/input{input_number}.txt'
  output_filename = f'./6-sumk/output{input_number}.txt'

  # Open and parse the input file
  with open(input_filename) as f:
    [N, K] = numbers_in_text_to_int(f.readline())
    print(f'N={N} K={K}')
    A = numbers_in_text_to_int(f.readline())

  # Process
  total_score = 0
  subsets = powerset(A)
  for subset in tqdm(subsets):
    score = pow(sum(subset), K)
    total_score += score
  total_score = total_score % 998244353

  # Output
  with open(output_filename) as f:
    [expected_solution] = numbers_in_text_to_int(f.readline())
  print(f"Expected solution: {expected_solution}", end='\t')
  print(f"My solution: {total_score}", end='\t')
  print(f"Solutions match = {total_score==expected_solution}")

for i in range(1,5+1):
  print(f"Input {i}")
  solve(i)
  print()