x = int(input("Enter how many rows you want: "))
y = int(input("Enter how many columns you want: "))

a = [[0 for x in range(y)] for x in range(x)]
print(a)

x = int(input("Enter the x-coordinate you want to modify: "))
y = int(input("Enter the y-coordinate you want to modify: "))
m = int(input("Enter new value: "))

a[x][y] = m

for x in range(len(a)):
    for y in range(len(a[x])):
        print(a[x][y])
