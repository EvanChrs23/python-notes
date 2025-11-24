def oddsum():
    s = 0
    for i in range(1,1000,2):
        s += i
    return s

def oddharmonicsum():
    h = float(0)
    for i in range(1,1000,2):
         h += 1/i
    return h

print(oddsum())
print(oddharmonicsum())