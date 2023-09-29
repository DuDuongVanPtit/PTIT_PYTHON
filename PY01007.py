for i in range(int(input())):
    n, x, m = map(float, input().split())
    ans = 0
    while n < m:
        a = n * (x / 100)
        n = n + a
        ans += 1
    print(ans)