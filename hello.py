import string
import time

lib = list(' ' + string.ascii_letters)
word = "Hello World"
result = ''

for x in word:
    for i in lib:
        print(result + i)
        time.sleep(0.03)
        if i == x:
            result += i
            break