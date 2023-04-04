spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    get_names = []
    for i in range(len(spicy_foods)):
        get_names.append(spicy_foods[i]["name"])
    return get_names
  

def get_spiciest_foods(spicy_foods):
    get_spiciest_foods = []
    for i in range(len(spicy_foods)):
       if spicy_foods[i]["heat_level"] > 5:
        get_spiciest_foods.append(spicy_foods[i])
    return get_spiciest_foods
      
    

def print_spicy_foods(spicy_foods):
    for i in range(len(spicy_foods)):
        name = spicy_foods[i]["name"]
        cuisine = spicy_foods[i]["cuisine"]
        heat_level =  (spicy_foods[i]["heat_level"])
        heat_emoji = "🌶" * (heat_level)
        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
        
        


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in range(len(spicy_foods)):
        if cuisine == spicy_foods[i]["cuisine"]:
            return spicy_foods[i]

def print_spiciest_foods(spicy_foods):
    for i in range(len(spicy_foods)):
        name = spicy_foods[i]["name"]
        cuisine = spicy_foods[i]["cuisine"]
        heat_level =  (spicy_foods[i]["heat_level"])
        heat_emoji = "🌶" * (heat_level)
        if heat_level > 5:
            print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")

def get_average_heat_level(spicy_foods):
    heat_level_array = []
    for i in range(len(spicy_foods)):
        heat_level_array.append(spicy_foods[i]["heat_level"])
    average = sum(heat_level_array)/len(heat_level_array)
    return average
        

def create_spicy_food(spicy_foods, spicy_food):
    new_food = []
    for i in range (len(spicy_foods)):
        new_food.append(spicy_foods[i])
    new_food.append(spicy_food)
    return new_food

  
