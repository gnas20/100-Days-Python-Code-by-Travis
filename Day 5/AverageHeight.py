# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(",")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

average_height=round(sum(height for height in student_heights)/len(student_heights)) 
print(average_height)