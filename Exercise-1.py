# 1. Replace "type here" with "Hello World!"
# print("type here")

print("Hello World!")

# 2. Assign "Hello World!" to the variable my_text
# my_text = <ADD CODE HERE>
# print(my_text)

my_text = "Hello World!"
print(my_text)

# 3. Type a couple of different values inside the print function.
# Make sure they are separated by commas.
# print(<ADD CODE HERE>)

print(3, 7, 12, 14, 21, 23, 34)

# 4. Assign a number to the variable glasses_of_water
# glasses_of_water = <ADD CODE HERE>
# print("I drank", glasses_of_water, "glasses of water today.")

glasses_of_water = 21
print("I drank", glasses_of_water, "glasses of water today.")

# 5. Increase the variable glasses_of_water by 2
# and fill the print function so it prints glass_of_water
#glasses_of_water = 3
# <ADD CODE HERE>
# print(<ADD CODE HERE>)

glasses_of_water = 3
glasses_of_water += 2
print(glasses_of_water)

# 6. Assign an integer to the variable, then print it.
# men_stepped_on_the_moon = <ADD CODE HERE>
# print(<ADD CODE HERE>)

men_stepped_on_the_moon = 2
print(men_stepped_on_the_moon)

# 7. Reassign the variable with a float.
# Hint: it was 0.1 cm in 1906 and as increased by 21.35 cm.
# global_mean_sea_level_2018 = 21
# global_mean_sea_level_2018 = <ADD CODE HERE >
# print(global_mean_sea_level_2018)

global_mean_sea_level_2018 = 21
global_mean_sea_level_2018 = global_mean_sea_level_2018 + 0.35
print(global_mean_sea_level_2018)

# or

global_mean_sea_level_2018 = 21
global_mean_sea_level_2018 = float(global_mean_sea_level_2018)
print(global_mean_sea_level_2018)

# correct

global_mean_sea_level_2018 = 21
global_mean_sea_level_2018 = 21.35
print(global_mean_sea_level_2018)

# 8. Assign True or False to the variable below then print it.
# staying_alive = <ADD CODE HERE >
# print(staying_alive)

staying_alive = True
print(staying_alive)

# 9. Use type() to assign the type of the first variable to answer
# men_stepped_on_the_moon = 12
# answer = <ADD CODE HERE >
# print(answer)

men_stepped_on_the_moon = 12
answer = type(men_stepped_on_the_moon)
print(answer)

# 10. Use type() to assign the type of the first variable to answer
# greeting = "Hello world!"
# answer = <ADD CODE HERE >
# print(answer)

greeting = "Hello world!"
answer = type(greeting)
print(answer)

# 11. Use type() to assign the type of the first variable to answer
# global_mean_sea_level_2018 = 21.36
# answer = <ADD CODE HERE >
# print(answer)

global_mean_sea_level_2018 = 21.36
answer = type(global_mean_sea_level_2018)
print(answer)

# 12. Use type() to assign the type of the first variable to answer
# staying_alive = True
# answer = <ADD CODE HERE >
# print(answer)

staying_alive = True
answer = type(staying_alive)
print(answer)

# 13. Convert number_of_items to an int and store it in answer
# number_of_items = "18"
# answer = <ADD CODE HERE >
# print(answer)

number_of_items = "18"
answer = int(number_of_items)
print(answer)

# 14. Convert random_value to an int and store it in answer
# random_value = 12.7
# answer = <ADD CODE HERE >
# print(answer)

random_value = 12.7
answer = int(random_value)
print(answer)

# 15. Convert measured_length to a float and store it in answer
# measured_length = "187.68"
# answer = <ADD CODE HERE >
# print(answer)

measured_length = "187.68"
answer = float(measured_length)
print(answer)

# 16. Convert shoe_price to a float and store it in answer
# measured_length = "69.99"
# answer = <ADD CODE HERE >
# print(answer)

shoe_price = "69.99"
answer = float(shoe_price)
print(answer)

# 17. Convert gwp_2018 to a string and store it in gwp_str
# gwp_2018 = 84.84
# gwp_str = <ADD CODE HERE >
# answer = "In 2018 gross product of the world (GWP) was " + \
#    gwp_str + " in trillion US dollars"
# print(answer)

gwp_2018 = 84.84
gwp_str = str(gwp_2018)
answer = "In 2018 gross product of the world (GWP) was " + \
    gwp_str + " in trillion US dollars"
print(answer)

# 18. Create an empty list and assign its type to answer
# gift_list = <ADD CODE HERE >
# answer = <ADD CODE HERE >
# print(answer)

gift_list = []
answer = gift_list
print(answer)

# 19. Create an empty dictionary and assign its type to answer
# grocery_items = <ADD CODE HERE >
# answer = <ADD CODE HERE >
# print(answer)

grocery_items = {}
answer = grocery_items
print(answer)

# 20. Create an empty tuple and assign its type to answer
# bucket_list = <ADD CODE HERE >
# answer = <ADD CODE HERE >
# print(answer)

bucket_list = ()
answer = bucket_list
print(answer)

# 21. Create and fill a list and print it out
# gift_list = <ADD CODE HERE >
# print(gift_list)

gift_list = ["laptop", "shoes", "balloons"]
print(gift_list)

# 22. Create and fill a dictionary and print it out.
# Use item as key and number to buy as value.
# grocery_items = <ADD CODE HERE>
# print(grocery_items)

grocery_items = {"bananas": 5, "milk": 2, "bread": "1"}
print(grocery_items)

# 23. Create and fill a tuple and print it out
# bucket_list = <ADD CODE HERE >
# print(bucket_list)

bucket_list = ("travel to Africa", "skydiving")
print(bucket_list)

# 24. Assign the first and second value from the list to answer_1 and answer_2 respectively.
# Assign the last value using a negative index to answer_3.
# number_list = [11, 100, 99, 1000, 999]
# answer_1 = <ADD CODE HERE >
# answer_2 = <ADD CODE HERE >
# answer_3 = <ADD CODE HERE >
# print(answer_1, answer_2, answer_3)

number_list = [11, 100, 99, 1000, 999]
answer_1 = number_list[0]
answer_2 = number_list[1]
answer_3 = number_list[-1]
print(answer_1, answer_2, answer_3)

# 25. Add an item to the end of gift_list
# gift_list = ['socks', '4K drone', 'wine', 'jam']
# <ADD CODE HERE >
# print(gift_list)

gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append("balloons")
print(gift_list)

# 26. Add the list ["socks", "tshirt", "pajamas"] to the end of gift_list
# gift_list = ['socks', '4K drone', 'wine', 'jam']
# <ADD CODE HERE>
# print(gift_list)

gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append(["socks", "tshirt", "pajamas"])
print(gift_list)

# 27. Insert "slippers" before "jam" in the gift_list
# gift_list = ['socks', '4K drone', 'wine', 'jam']
# <ADD CODE HERE>
# print(gift_list)

gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.insert(3, "slippers")
print(gift_list)

# 28. Assign when Plato was born to answer and print it out
# plato = {"name": "Plato", "country": "Ancient Greece",
# "born": -427, "teacher": "Socrates", "student": "Aristotle"}
# answer = <ADD CODE HERE>
# print(answer)

plato = {"name": "Plato", "country": "Ancient Greece",
         "born": -427, "teacher": "Socrates", "student": "Aristotle"}
answer = plato["born"]
print(answer)

# 29. Change Plato's birth year to 428 B.C.
# plato = {"name": "Plato", "country": "Ancient Greece",
#         "born": -428, "teacher": "Socrates", "student": "Aristotle"}
# <ADD CODE HERE >
# print(plato["born"])

plato = {"name": "Plato", "country": "Ancient Greece",
         "born": -428, "teacher": "Socrates", "student": "Aristotle"}
plato["born"] = -428
print(plato["born"])

# 30. Add an item with Plato's work to the dictionary with the key "work" with the items ["Apology", "Phaedo", "Republic", "Symposium"]
# plato = {"name": "Plato", "country": "Ancient Greece",
#         "born": -428, "teacher": "Socrates", "student": "Aristotle"}
# <ADD CODE HERE >
# print(plato)

plato = {"name": "Plato", "country": "Ancient Greece",
         "born": -428, "teacher": "Socrates", "student": "Aristotle"}
plato["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]
print(plato)

# 31. # Divide a by b and assign to the variable result
# a = 10
# b = 3
# result = <ADD CODE HERE >
# print(result)

a = 10
b = 3
result = a/b
print(result)

# 32. # Divide a by b using integer division (//)
# and assing to the variable result
# a = 10
# b = 3
# result = <ADD CODE HERE >
# print(result)

a = 10
b = 3
result = a//b
print(result)

# 33. Add 15 to the variable speed using +=
# speed = 75
# <ADD CODE HERE >
# print(speed)

speed = 75
speed += 15
print(speed)

# 34. Compare if a and b are equal
# a = 10
# b = 2*5
# answer = <ADD CODE HERE >
# print(answer)

a = 10
b = 2*5
answer = (a == b)
print(answer)

# 35. Write one million using exponentiation
# answer = 10**<ADD CODE HERE >
# print(answer)

answer = 10**6
print(answer)

# 36. Compare if both a and b are true
# a = True
# b = (10 == 2*5)
# answer = <ADD CODE HERE >
# print(answer)

a = True
b = (10 == 2*5)
answer = (a and b)
print(answer)

# 37. Compare if any value of the values in fruits is equal to "Melon" and print out the result
# fruits = ["Mango", "Kiwi", "Melon", "Cherry"]
# answer_1 = <ADD CODE HERE >
# answer_2 = <ADD CODE HERE >
# answer_3 = <ADD CODE HERE >
# answer_4 = <ADD CODE HERE >
# print(answer_1, answer_2, answer_3, answer_4)

fruits = ["Mango", "Kiwi", "Melon", "Cherry"]
answer_1 = (fruits[0] == "Melon")
answer_2 = (fruits[1] == "Melon")
answer_3 = (fruits[2] == "Melon")
answer_4 = (fruits[3] == "Melon")
print(answer_1, answer_2, answer_3, answer_4)
