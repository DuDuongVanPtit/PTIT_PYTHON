def reTurn(s):
    for i in s:
        if i != '4' and i != '7':
            print("NO")
            return
    print("YES")
    return
for i in range(int(input())):
    s = str(input())
    reTurn(s)