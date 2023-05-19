def add_the_digits_in_a_2_digit_number(input_number):
    if len(input_number)!=2:
        return False
    return int(str(input_number)[0])+int(str(input_number)[1])

print(add_the_digits_in_a_2_digit_number(input("Type a two digit number: ")))


def bmi_calculator(weight,height):
    return weight*(height**2)
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
print(bmi_calculator(weight,height))