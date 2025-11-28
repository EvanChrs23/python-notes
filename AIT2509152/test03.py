from sys import argv

script, power, number = argv
n = int(power)
x = int(number)
total = 0

for i in range(int(n)):
    add = ((-1)**i)*(int(x)**(i+1))/(i+1)
    total += add

print(total)