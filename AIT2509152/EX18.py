import random
import string

while True:
    try:
        age = int(input("How old are you?: "))
        if age > 90:
            print("Bro... just move on already")
        elif age > 21:
            print("Boomer ahh")
        else:
            print("Minor ahh")

        print("Get a job")

        if (age%2 == 0 or age%3 == 0) and not age%6==0:
            print("okay!")
        break

    except ValueError:
        print("you suck")

print(random.randint(1,10))

print("hello\n"*(age%5))