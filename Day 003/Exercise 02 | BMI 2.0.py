# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height = float(height)
weight = float(weight)

BMI = weight/(height ** 2)
BMI = round(BMI,0)
BMI = int(BMI)

if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI <= 25 and BMI > 18.5:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI <= 30 and BMI > 25:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI <= 35 and BMI > 30:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
