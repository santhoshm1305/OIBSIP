def bmi_cal(height,weight):
    weight_ = int(weight)
    height_ = float(height)
    bmi = int(((weight_) / (height_ ** 2)))
    if bmi < 18.5:
        print(f"\nYour BMI is: {bmi} \nYou are Underweight.")
    elif bmi >= 18.5 and bmi < 25:
        print(f"\nYour BMI is:{bmi} \nNormal weight, you are healthy.")
    elif bmi >= 25 and bmi < 30:
        print(f"\nYour BMI is:{bmi} \nYou are Overweight, Exercise daily.")
    elif bmi >= 30:
        print(f"\nYour BMI is:{bmi} \nYou are obese, Eat Healthy and hit the Gym.")
    else:
        print(f"\nYour BMI is:{bmi} \nThe Weight Must Be An Integer And Height In Decimal.")

weight = input("Enter your weight in Kgs :")
height = input("Enter you height in Meters: ")
bmi_cal(height,weight)