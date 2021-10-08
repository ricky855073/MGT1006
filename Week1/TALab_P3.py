height = int(input("Please enter your height (cm):"))
weight = int(input("Please enter your weight (kg):"))

BMI = weight / ((height/100) ** 2)
print(f'Your BMI is {BMI:.5f}')