t = int(input())
while t > 0: 
    s = input()
    i = 1
    while i < len(s):
        for x in range(ord(s[i]) - ord('0')):
            print(s[i - 1], end="")
        i += 2
    print()
    t -= 1