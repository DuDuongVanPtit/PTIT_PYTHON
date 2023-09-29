from math import*
def check(s):
    if(s[0] != '5'):
        return False
    i = 1
    while i < len(s): 
        if(s[i] != '0'):
            return False
        i += 1
    return True
t = int(input())
while t :
    s = input()
    if(check(s)):
        print(s)
    elif(s[len(s) - 1] == '5'):
        print(int((int(s[0]) + 1) * pow(10, len(s) - 1)))
    else:
        if(int((int(s[0]) + 1) * pow(10, len(s) - 1)) - int(s) > int(s) - int((int(s[0])) * pow(10, len(s) - 1))):
            print(int((int(s[0])) * pow(10, len(s) - 1)))
        else:
            print(int((int(s[0]) + 1) * pow(10, len(s) - 1)))
    t -= 1