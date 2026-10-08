x, k, y = map(int, input().split())
multiples = []

for i in range(1, x + 1):
    multiples.append(i * k)

if y in multiples:
    print("YES")
else:
    print("NO")
