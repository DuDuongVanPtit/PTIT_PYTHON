def solve(ab, x, y):
    minx = ""
    maxx = ""
    miny = ""
    maxy = ""
    for i in range(len(x)):
        if(x[i] == (ab[1])):
            minx += ((ab[0]))
        else:
            minx += x[i]
        if(x[i] == (ab[0])):
            maxx += (ab[1])
        else:
            maxx += x[i]
    for i in range(len(y)):
        if(y[i] == (ab[1])):
            miny += (ab[0])
        else:
            miny += y[i]
        if(y[i] == (ab[0])):
            maxy += (ab[1])
        else:
            maxy += y[i]
    print(int(minx) + int(miny), int(maxx) + int(maxy), sep=" ", end="\n")

for i in range(int(input())):
    ab = input().split()
    ab.sort()
    s = input().split()
    if(len(s) > 1):
        x, y = s[0], s[1]
    else:
        x = s[0]
        y = input()
    solve(ab, x, y)