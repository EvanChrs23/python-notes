A = []
B = []

print("Welcome to the matrix calculator")

opcommand = input("Which operation are you going to execute? (+,-,*,transpose,det,inv): ")

def addition():
    matrix = []
    while True:
        try:
            rowA = int(input("How many rows for matrix A?: "))
            colA = int(input("How many columns for matrix A?: "))
            rowB = int(input("How many rows for matrix B?: "))
            colB = int(input("How many columns for matrix B?: "))
        except ValueError:
            print("lu goblok")
            continue
        break

    for i in range(rowA):
        while True:
            while True:
                nums = input(f"Enter the values for row {i+1} in matrix A, seperated by space: ").split()
                if len(nums) != colA:
                    print("lu goblok")
                else:
                    break

            try:
                for _ in range(len(nums)):
                    nums[_] = int(nums[_])
            except ValueError:
                print("lu goblok")
                continue
            
            break

        A.append(nums)

    for i in range(rowB):
        while True:
            while True:
                nums = input(f"Enter the values for row {i+1} in matrix B, seperated by space: ").split()
                if len(nums) != colB:
                    print("lu goblok")
                else:
                    break

            try:
                for _ in range(len(nums)):
                    nums[_] = int(nums[_])
            except ValueError:
                print("lu goblok")
                continue
            
            break

        B.append(nums)

    if (rowA == rowB and colA == colB):
        for i in range(rowA):
            row = []
            for j in range(colA):
                row.append(A[i][j]+B[i][j])
            matrix.append(row)
    else:
        matrix = "undefined"

    print(matrix)

addition()