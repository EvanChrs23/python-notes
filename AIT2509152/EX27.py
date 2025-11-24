def cheese_and_crackers(cheese_count, boxes_of_crackers): #this is the main
    print(f"You have {cheese_count} cheese(s)!")
    print(f"You have {boxes_of_crackers} box(es) of crackers!")
    print("Man that's enough for a party")
    print("Get a blanket\n")

print("We can just give the function numbers directly")
cheese_and_crackers(20, 30) #inputs cheese_count = 20 and boxes_of_crackers = 30

print("Pr we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers) #inputs cheese_count = 10 and boxes_of_crackers = 50

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) #inputs cheese_count = 30 and boxes_of_crackers = 11

print("And we can combine the two. variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #inputs cheese_count = 110 and boxes_of_crackers = 1050