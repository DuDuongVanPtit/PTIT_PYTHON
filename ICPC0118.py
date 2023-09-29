for i in range(int(input())):
    x = input().split()
    t = [int(x[0]), int(x[1])]
    if(t[0] >= 20 and t[1] == 1 or t[0] <= 18 and t[1] == 2):
        print("Bao Binh")
    elif(t[0] > 18 and t[1] == 2 or t[0] <= 20 and t[1] == 3):
        print("Song Ngu")
    elif(t[0] > 20 and t[1] == 3 or t[0] < 20 and t[1] == 4):
        print("Bach Duong")
    elif(t[0] > 19 and t[1] == 4 or t[0] <= 20 and t[1] == 5):
        print("Kim Nguu")
    elif(t[0] > 20 and t[1] == 5 or t[0] <= 20 and t[1] == 6):
        print("Song Tu")
    elif(t[0] > 20 and t[1] == 6 or t[0] <= 22 and t[1] == 7):
        print("Cu Giai")
    elif(t[0] > 22 and t[1] == 7 or t[0] <= 22 and t[1] == 8):
        print("Su Tu")
    elif(t[0] > 22 and t[1] == 8 or t[0] <= 22 and t[1] == 9):
        print("Xu Nu")
    elif(t[0] > 22 and t[1] == 9 or t[0] <= 22 and t[1] == 10):
        print("Thien Binh")
    elif(t[0] > 22 and t[1] == 10 or t[0] <= 22 and t[1] == 11):
        print("Thien Yet")
    elif(t[0] > 22 and t[1] == 11 or t[0] <= 21 and t[1] == 12):
        print("Nhan Ma")
    elif(t[0] > 21 and t[1] == 12 or t[0] <= 19 and t[1] == 1):
        print("Ma Ket")
        