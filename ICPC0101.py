n = int(input())
a = []
l = list(input().split())

for i in l:
    x = int(i)
    if len(a) == 0:
        a.append(x)
    else:
        if (a[-1] + x) % 2 == 0:
            a.pop(-1)
        else:
            a.append(x)
print(len(a))
