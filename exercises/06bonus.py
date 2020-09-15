# Create a python class that uses one of the functions 
# you write for these exercises.

food = {
  'Brian': 'pizza',
  'Lenny': 'ramen',
  'Daniel': 'bagels'
}

def favorite_food(food):
  for (key, value) in food.items():
    print(f"{key} likes to eat {value}")

favorite_food(food)

# Brian likes to eat pizza
# Lenny likes to eat ramen
# Daniel likes to eat bagels