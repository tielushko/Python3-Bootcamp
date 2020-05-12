# Given the provided dictionary of donations: donations = dict(sam=25.0, lena=88.99, chuck=13.0, 
# linus=99.5, stan=150.0, lisa=50.25, harrison=10.0) Use a loop to calculate the total value of the donations.  Save the result to a variable
# total_donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = 0

for value in donations.values():
    total_donations += value


# Exercise 2
# The food variable will store a randomly chosen food string like "gummy bear" or "morning bun".  Some of these items are in the
# bakery_stock   dictionary, and some are not.
# Your task is to simply print out a string depending on if food  
# is a value in bakery_stock. If food   is contained in bakery_stock   
# print out a string that states how many items are left: "3 left" if food is "toffee cookie" or "1 left" if food is "morning bun", etc.
# if food is not contained in bakery_stock (like "gummy bear"), print out we "we don't make that"

# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if (bakery_stock.get(food) != None):
    print(f"{bakery_stock.get(food)} left")
else:
    print("We don't make that")

# Exercise 3
# Imagine we're creating a video game and want to model the initial starting-state of our game. I've provided you with a list of 
# strings called game_properties. Use dict.fromkeys   to generate a new dictionary using the provided game_properties   list. 
# Initialize all values to 0  .  Save the result in a variable called  initial_game_state

game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state

initial_game_state = dict.fromkeys(game_properties, 0)

# Exercise 4
#I've provided you with a start dictionary called inventory.
# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Follow the instructions found in the comments:
# 1. Make a copy of inventory and save it to a variable called stock_list using a dictionary method we've covered
# 2. Add the value 18 to stock_list under the key "cookie"
# 3. Remove "cake" from stock_list using a method we learned 
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()

# add the value 18 to stock_list under the key "cookie"
stock_list["cookie"] = 18

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")