def calculate_bmi(height, weight, bmi):
    print("Height= " + str(height))
    print("Weight= " + str(weight))
    bmi = weight / (height * height)
    print("BMI= " + str(bmi))
    if bmi < 18.5:
        print("Underweight")
        return -1
    elif bmi >= 18.5 and bmi < 25:
        print("Normal Weight")
        return 0
    elif bmi >= 25 and bmi < 30:
        print("Overweight")
        return 1
    elif bmi >= 30:
        print("Obese")

calculate_bmi(weight=57,height = 1.3,bmi=0)
