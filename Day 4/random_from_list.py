# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_variable=random.randint(0,len(names)-1)
choosen_names = names[random_variable]
print(f"{choosen_names} is going to buy the meal today!")