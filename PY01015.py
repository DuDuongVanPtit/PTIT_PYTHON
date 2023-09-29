def check(s):
    tmp = s[0]
    i = 1
    while i < len(s):
        if(s[i] < tmp):
            print("NO")
            return
        tmp = s[i]
        i += 1
    print("YES")
    return
for i in range(int(input())):
    s = input()
    check(s)
        