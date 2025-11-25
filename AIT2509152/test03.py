from sys import argv

script, n, x = argv
total = 0

for i in range(n):
    add = ((-1)**i)*(x**(i+1))/(i+1)
    total += add

print(total)