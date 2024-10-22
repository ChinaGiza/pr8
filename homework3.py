n = 10
m = 10
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * m)
    else:
        print("*" + " " * (m - 2) + "*")
