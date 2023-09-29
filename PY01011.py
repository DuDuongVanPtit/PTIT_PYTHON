def check(n):
    if str(n) != str(n)[::-1]:
        return False
    for c in str(n):
        if (ord(c) - ord('0')) % 2 == 1:
            return False
    if len(str(n)) % 2 == 1:
        return False
    return True


for t in range(int(input())):
    n = int(input())
    for i in range(1, n):
        if check(i):
            print(i, end=" ")
    print()
