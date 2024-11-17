from itertools import combinations

QUESTION_NAME = "6-xor-the-string"
QUESTION_START = 5
QUESTION_END = 5

def numbers2int(line: str, separator: str = ' ') -> list[int]:
  """Convert string of numbers to list[int]"""
  return [int(x) for x in line.split(separator)]

def solve(input_filename: str, output_filename: str) -> int:
  # Open and parse the input file
  with open(input_filename) as f:
    [n, k] = numbers2int(f.readline())
    s = f.readline()

  # Process the data
  def get_two_binary_digits(s: int, i: int) -> tuple[int, int]:
    """NOTE: INDEX IS FROM RIGHT TO LEFT"""
    # https://stackoverflow.com/a/49079722
    digit_1 = (s & (1 << i)) >> i
    digit_2 = (s & (1 << i+1)) >> i+1
    return [digit_1, digit_2]

  def interleave_strings(string1, string2):
    result = ""
    min_len = min(len(string1), len(string2))
    for i in range(min_len):
        result += string1[i] + string2[i]
    result += string1[min_len:] + string2[min_len:]
    return result

  def transform(s: str, n: int) -> tuple[int, int]:
    new_m = 2*n - 1
    xor = ''
    for i in range(n-1):
      # print(s, i,n, s[i])
      prev = 1 if s[i] == '1' else 0
      post = 1 if s[i+1] == '1' else 0
      xor += str(prev ^ post)
    # https://www.geeksforgeeks.org/python-interleaving-two-strings/
    transformed = interleave_strings(s, xor)
    # print(f'{xor=} {transformed=}')
    return (transformed, new_m)
  
    # transformed = '0'.join(s)
    # for i in range(1,new_m-1,2):
    #   # xor digit
    #   print(i)
    #   prev = 1 if s[i-1] == '1' else 0
    #   post = 1 if s[i+1] == '1' else 0
    #   num = prev ^ post
    #   transformed[i] = str(num)

    # transformed = 0
    # for i in range(n-1): # note: reading from right to left
    #   [digit_1, digit_2] = get_two_binary_digits(s, i)
    #   xor = digit_1 ^ digit_2
    #   new_3_digits = digit_1 | xor << 1 | digit_2 << 2
    #   # print(f'{new_3_digits:03b}')
    #   transformed = transformed | new_3_digits << i*2
    # new_m = n*2-1

    # (t, m)
    return (transformed, new_m)

  def get_beauty(t: str, m: int) -> int:
    beauty = 0
    for i in range(m-1):
      # print(i, i+1, m)
      if t[i] == t[i+1]:
        beauty += 1
    return beauty
  
  def g(t: str, m: int) -> int:
    t_prime = t
    m_prime = m
    for _ in range(k):
      # print(f'{t_prime=}')
      [t_prime, m_prime] = transform(t_prime, m_prime)
      print(m_prime)
    beauty = get_beauty(t_prime, m_prime)
    # print(f'{t=} \t {t_prime=} \t {beauty=}')
    return beauty
  
  total = 0
  for x, y in combinations(range(n+1), r=2):
    if y-x > 1:
      substr = s[x:y]
      total = (total + g(substr, len(substr))) % 998244353
  #total = g(s, n)

  # Output
  with open(output_filename, 'w') as f:
    f.write(str(total))

  return total

for i in range(QUESTION_START, QUESTION_END+1):
  input_filename = f"./6-xor-the-string/input{i}.txt"
  output_filename = f"./6-xor-the-string/output{i}.txt"
  
  answer = solve(input_filename, output_filename)
  
  print(f"{QUESTION_NAME} Q{i}: {answer}")