s = input()
four = 0
sevent = 0
for i in s: 
    if i == '4':
        four = four + 1
    elif i == '7':
        sevent = sevent + 1
if(four + sevent == 4 or four + sevent == 7):
    print("YES")
else:
    print("NO")