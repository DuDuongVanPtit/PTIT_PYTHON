t = int(input())
while t:
    s = input()
    cnt = [0]*256
    for i in range(len(s)):
        cnt[ord(s[i])] += 1
        if(i == len(s) - 1):
            print(cnt[ord(s[i])], s[i], sep = "", end = "")
        else:
            if(s[i + 1] != s[i]):
                print(cnt[ord(s[i])], s[i],sep = "", end="")
                cnt[ord(s[i])] = 0  
    print()
    t -= 1