from itertools import permutations

word1 = "SEND"
word2 = "MORE"
result = "MONEY"

letters = set(word1 + word2 + result)

for values in permutations(range(10), len(letters)):
    mapping = dict(zip(letters, values))

    if mapping["S"] == 0 or mapping["M"] == 0:
        continue

    send = int("".join(str(mapping[c]) for c in word1))
    more = int("".join(str(mapping[c]) for c in word2))
    money = int("".join(str(mapping[c]) for c in result))

    if send + more == money:
        print("Solution found:")
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        break
