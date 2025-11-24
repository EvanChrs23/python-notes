#v1
numbers = [10,5,24,8,6]
count = 0

for number in numbers:
    if number%2 == 1:
        count += 1 #count the odd numbers

if count > 0:
    print(True)
else:
    print(False)

#v2
numbers = [10,5,24,8,6]
count = 0
for number in numbers:
    if number % 2 == 1:
        count += 1
print(count>0)

#v3
numbers = [10,5,24,8,6]
count = 0
for number in numbers:
    count += number % 2 == 1
print(count>0)

#v4
numbers = [10,5,24,8,6]
for number in numbers:
    if number % 2 == 1:
        print(True)
        break

#v5
def odd_detector():
    numbers = [10,5,24,8,6]
    for number in numbers:
        if number % 2 == 1:
            print(False)
            return()
    print(True)
odd_detector()

#v6
def num_detector():
    numbers = [10,5,24,8,6]
    count_odd = 0
    count_even = 0
    for number in numbers:
        if number % 2 == 1:
            count_odd += 1
        else:
            count_even += 1
        if count_odd == 3:
            return(False)
        if count_even == 3:
            return(True)
print(num_detector())