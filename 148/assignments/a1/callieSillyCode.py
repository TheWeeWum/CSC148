total = 0
n = 6 + 1
for i in range(1, n):
    total += i / (n - i)
    print(str(i) + " / " + str(n-i))

print(total)
