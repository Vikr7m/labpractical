n = int(input("How many values? "))
h = 0
a = []
for i in range(n):
    b = int(input("Enter the value %d: "%i))
    a.append(b)
for i in a:
    if i>h:
        h = i
print("The highest value:",h)
