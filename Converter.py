while True:
    try:
        choice = input("What would you like to convert?\n1. Meters to Feet\n2. Feet to Meters\nChoose the number: ")

        if choice != "1" and choice != "2":
            print("Invalid choice. Please enter 1 or 2")
            continue

        number = float(input("Enter the value to convert: "))

        if choice == "1":
            answer = number / 0.3048
            print(f"{number} meters is {answer:.4f} feet")
        if choice == "2":
            answer = number * 0.3048
            print(f"{number} feet is {answer:.4f} meters")

        break

    except ValueError:
        print("Please enter a valid number.")
