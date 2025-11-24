pi = 0
for i in range(99999999):
    pi += (-1)**i / (2*i+1)

print(pi*4)