from math import*
a = [0]*17
a[10] = 'A'
a[11] = 'B'
a[12] = 'C'
a[13] = 'D'
a[14] = 'E'
a[15] = 'F'
def thapphan(s):
    i = len(s) - 1
    ans = int(0)
    t = int(0)
    while i > -1:
        if(s[i] == '1'):
            ans += 2**t
        t += 1
        i -= 1
    return ans

def solve8(s, b):
    tp = thapphan(s)
    ans = ""
    while tp > 0:
        ans = str(tp % b) + ans
        tp = tp // b
    print(ans)
def solve16(s, b):
    i = len(s) - 1
    tmp = ""
    ans = ""
    while i > -1:
        tmp = s[i] + tmp
        if(len(tmp) == 4):
            if(thapphan(tmp) < 10):
                ans = str(thapphan(tmp)) + ans
            else:
                ans = a[thapphan(tmp)] + ans
            tmp = ""
        i -= 1
    if(len(tmp) > 0):
        ans = str(thapphan(tmp)) + ans
    print(ans)

for i in range(int(input())):
    b = int(input())
    s = input()
    if(b == 2):
        print(s)
    elif(b == 16):
        solve16(s, b)
    else:
        solve8(s, b)
