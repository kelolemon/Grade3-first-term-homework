
MAX_NUMBER = 2147483647

x = 2600.0

for i in range(0, 199):
    x = x * 1.1
    if x > MAX_NUMBER:
        print(i)
        break

