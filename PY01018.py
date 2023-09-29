tmp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    string = input()
    if string == "0":
        break
    x, s = string.split()
    k = int(x)
    res = ''
    for i in s:
        j = tmp.find(i)
        res += tmp[(j + k) % 28]
    print(res[::-1])