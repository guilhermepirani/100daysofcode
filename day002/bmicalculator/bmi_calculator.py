'''Write a program that calculates the Body Mass Index (BMI) from a user.
The BMI is a measure of some's weight taking into account their height.
e.g. If a tall person and a short person both weigh the same amount, 
the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg)
by the square of their height (in m).
Warning: you should convert the result to a whole number.'''

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(f'Your BMI is {round(float(weight)/float(height)**2)}.')