# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print("Leap Year")
else:
    print("Not leap year")

    