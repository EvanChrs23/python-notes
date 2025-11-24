class Matrix:
    def __init__(self,name = "Matrix"):
        self.name = name
        self.data = []
        self.rows = 0
        self.cols = 0
        self.input_matrix()

    def input_matrix(self):
        while True:
            try:
                self.rows = int(input(f"How many rows for matrix {self.name}?: "))
                self.cols = int(input(f"How many columns for matrix {self.name}?: "))
                break
            except ValueError:
                print("Must be an integer")

        for i in range(self.rows):
            while True:
                nums = input(f"Enter the values for row {i+1} in {self.name}, separated by space: ")
                if len(nums) != self.cols:
                    print(f"Please enter exactly {self.cols} values.")
                    continue
                try:
                    nums = list(map(int, nums))
                    self.data.append(nums)
                    break
                except ValueError:
                    print("Please enter numbers only.")

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])
    
