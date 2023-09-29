from math import*;
for i in range(int(input())):
    n = int(input())
    bf = n
    s = 0
    while(n > 0):
        s = s + factorial(n % 10)
        n = n // 10
    if(s == bf): print("Yes")
    else: print("No")