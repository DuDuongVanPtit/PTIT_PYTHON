from math import*
def check(n):
    sum = (n[0]) - ord('0')
    for i in range(1, len(n)):
        sum += (ord(n[i]) - ord('0'))
        if abs(ord(n[i]) - ord(n[i - 1])) % 2 != 0: return False
    if sum % 10 == 0: return True
for i in range(int(input())):
    n = input()
    print(ord('0'))
    print((lambda y, n: y if check(n) == True else n)("YES", "NO"))
