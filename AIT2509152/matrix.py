A = [
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"]
]

for m in range(len(A)):
    for n in range(len(A[m])):
        print(A[m][n],end=' ')
    print("\n")