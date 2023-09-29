from math import*

def check(n):
    if n < 2: 
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0: 
            return False
    return True


t = int(input())
while t :
    n = int(input())
    k = int(0)
    for i in range(1, n):
        if gcd(i, n) == 1:
            k = k + 1
    if check(k):
        print("YES")
    else:
        print("NO")
    t = t - 1
    

