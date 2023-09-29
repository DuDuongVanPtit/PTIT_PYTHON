s = input()
thuong = 0
hoa = 0
for i in s:
    if ord(i) < ord('a') : 
        hoa += 1
    else: 
        thuong += 1
if(thuong >= hoa):
    print(s.lower())
else:
    print(s.upper())