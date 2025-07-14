#BMI Calculator
def calculate_BMI(weight, height):
    BMI = weight / (height ** 2)
    return BMI

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

BMI = calculate_BMI(weight, height)
print(f"Your BMI is {BMI:.2f}")

if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("You have a normal weight.")
elif 25 <= BMI < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")