i = 0
numbers = []
increment = int(input("How much increment?: "))

while i < 6:
    print(f"At the top oof i is {i}")
    numbers.append(i)

    i = i + increment
    print("Numbers now: ",numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")
for num in numbers:
    print(num)