for i in range(int(input())):
    t = input().split()
    arr = input().split()
    arr[len(arr):] = arr[:int(t[1])]
    arr[:int(t[1])] = []
    for x in arr:
        print(x, end = " ")
    print()