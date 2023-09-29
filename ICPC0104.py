from math import*
for i in range(int(input())):
    s = input()
    s += 'e'
    Min = 0
    ans = ""
    for x in s:
        if(x.isnumeric()):
            ans += x
        else:
            if len(ans) > 0:
                Min = max(int(ans), Min)
                ans = ""
    print(Min)
