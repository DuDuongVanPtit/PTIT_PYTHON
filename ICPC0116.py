for i in range(int(input())):
    t = input()
    print((lambda x, y: "YES" if x == y else "NO")(t[0], t[len(t) - 1]))
# 2
# 12345
# 123451