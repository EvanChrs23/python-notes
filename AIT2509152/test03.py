print('Enter 5 numbers less than 32000, seperate it by hitting "Enter"')

highest = 0

for i in range(5):
    num = int(input(">> "))
    if num >= highest:
        highest = num

print(highest)