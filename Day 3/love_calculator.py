# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name=name1.lower()+name2.lower()

count_in_word_true=combined_name.count('t')+combined_name.count('r')+combined_name.count('u')+combined_name.count('e')

count_in_word_love=combined_name.count('l')+combined_name.count('o')+combined_name.count('v')+combined_name.count('e')

love_score = int(str(count_in_word_true)+str(count_in_word_love))

if love_score <10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >=40 and love_score <=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")