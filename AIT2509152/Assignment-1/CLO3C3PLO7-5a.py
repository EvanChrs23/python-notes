what_to_wear = {
    "sunny": "sunglasses and light clothes",
    "rainy": "an umbrella and waterproof shoes",
    "snowy": "a thick coat, gloves, and a scarf",
    "windy": "a windbreaker jacket",
    "cold": "a sweater and a jacket"
}

weather = input("What is the current weather?: ")
if weather in list(what_to_wear):
    print(what_to_wear[weather])
else:
    print("Sorry, I don't have advice for that weather.")