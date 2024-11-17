# Put your input in input.txt in the working directory (or modify the path)
input_file_path = "input.txt"
file = open(input_file_path, encoding='utf-8')

n, m = [int(x) for x in file.readline().split()]

cards = []
for i in range(n):
    card = [int(x) for x in file.readline().split()]
    card = [card[0] + card[1], card[2] + card[3]]
    cards.append(card)

cards.sort(reverse=True)  # This sorts by descending order of cards[0] first, which is a+b

ans = 0
xsum_m1 = sum([card[0] for card in cards[:m-1]])
xsum_m = xsum_m1 + cards[m - 1][0]
for i in range(m):
    ans = max(ans, xsum_m + cards[i][1])
for i in range(m, n):
    ans = max(ans, xsum_m1 + cards[i][0] + cards[i][1])

print(ans)

file.close()