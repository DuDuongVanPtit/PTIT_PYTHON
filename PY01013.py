from math import*

def nt(n): 
    if n < 2: 
        print("NO")
        return
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            print("NO")
            return
    print("YES")
    return

# main--------------------

t = int(input())
while t > 0:
    a, b = map(int, input().split())
    x = gcd(a, b)
    sum = 0
    while(x > 0):
        sum += x % 10
        x //= 10
    nt(sum)
    t -= 1
    