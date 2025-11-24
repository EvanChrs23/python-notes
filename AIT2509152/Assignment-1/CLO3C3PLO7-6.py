n = 4

for i in range(n + 1): #for the top half
    print(" " * (n - i), end='') #the spaces at front
    print("*", end='') #prints "*""

    for j in range(2 * i - 1):
        print(" ", end='') #the spaces in the middle
    
    if i != 0:
        print("*") #if the position is not in the first
    else:
        print() #at the first position

for i in range(n - 1, -1, -1): #for the second helf
    print(" " * (n - i), end='') #the spaces at front
    print("*", end='') #prints "*"

    for j in range(2 * i - 1):
        print(" ", end='') #the spaces in the middle

    if i != 0:
        print("*") #if the position is not in the last
    else:
        print() #at the last position