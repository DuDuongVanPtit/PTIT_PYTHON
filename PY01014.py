l = list(map(int, input().split()))
a, k, n = l
i = k - (a % k)
b = []
n -= a
for j in range(i, n+1, k):
    b.append(j)

if len(b) == 0:
    print(-1)
else:
    for x in b:
        print(x, end=" ")
