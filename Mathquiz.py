import random
import operator
import time

op = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv
}

while True:
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    op_symbol = random.choice(list(op.keys()))
    op_func = op[op_symbol]

    print("Round it into 2 decimal places")
    user_answer = input(f"{num1} {op_symbol} {num2} = ")

    try:
        user_answer = float(user_answer)
    except ValueError:
        print("Bro??")

    real_answer = round(op_func(num1,num2),2)

    if user_answer == real_answer:
        print("Correct!!")
    else:
        print(f"Wrong! The answer is {real_answer}")

    time.sleep(1)

    while True:
        continue_game = input("Continue? (Y/N) : ").strip().lower()

        if continue_game == "y":
            print("Continuing...")
            time.sleep(1)
            break
        elif continue_game == "n":
            print("Goodbye!!")
            exit()
        else:
            print("Please insert Y or N")
            continue