def add(a, b):
    print(f"Adding {a} + {b}")
    return a+b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a-b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a*b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a/b

print("Let's do math with some functions")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here's a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2)))) #-4391

print(f"That becomes {what}, Can you do it by hand?")