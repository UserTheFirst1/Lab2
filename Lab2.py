def calculate_bmi(height, weight, bmi):
    print("Height= " + str(height))
    print("Weight= " + str(weight))
    bmi = weight / (height * height)
    print("BMI= " + str(bmi))
    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("Normal Weight")
    elif bmi >= 25 and bmi < 30:
        print("Overweight")




calculate_bmi(weight=57,height = 1.73,bmi=0)
