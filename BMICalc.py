import time
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("BMI Calculator")

while True:

    while True:

        display = input("Show BMI category list? (y/n): ").lower()
        if display == "y":
            print("""
            BMI Categories:
            - Underweight       : Less than 18.5
            - Normal weight     : 18.5 - 24.9
            - Overweight        : 25 - 29.9
            - Obese Class I     : 30 - 34.9
            - Obese Class II    : 35 - 39.9
            - Obese Class III   : 40 and above
            """)
            break
        elif display == "n":
            break
        else:
            print("Please choose y or no")
            time.sleep(1.5)

    while True:
        try:
            while True:
                height = float(input("\nEnter your height (cm): "))
                if height <= 0:
                    print("Height must be greater than zero.")
                else:
                    break

            while True:
                weight = float(input("Enter your weight (kg): "))
                if weight <= 0:
                    print("Weight must be greater than zero.")
                else:
                    break

            BMIval = weight / pow(height/100, 2)
            print(f"BMI : {BMIval:.2f}")

            if BMIval < 18.5:
                print("Category: Underweight")
            elif 18.5 <= BMIval < 25:
                print("Category: Normal weight")
            elif 25 <= BMIval < 30:
                print("Category: Overweight")
            elif 30 <= BMIval < 35:
                print("Category: Obese Class I")
            elif 35 <= BMIval < 40:
                print("Category: Obese Class II")
            else:
                print("Category: Obese Class III")

            while True:
                again = input("Check another BMI?(y/n): ").lower()
                if again == "y":
                    print("Continuing...")
                    time.sleep(1.5)
                    break
                elif again == "n":
                    print("Goodbye!")
                    time.sleep(1.5)
                    exit()
                else:
                    print("Please choose y or n")

        except ValueError:
            print("Please input a valid number")
            time.sleep(1.5)