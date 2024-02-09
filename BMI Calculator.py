print("Type your weight in kilograms:")
kg = float(input())

print("Type your height in meters:")
m = float(input())

print("Type your age:")
age = int(input())

bmi = kg / (m ** 2)

bmiprint = ""

if age > 20:

    if bmi < 18.5:
        bmiprint = "underweight"
    elif bmi < 25:
        bmiprint = "normal weight"
    elif bmi < 30:
        bmiprint = "overweight"
    else:
        bmiprint = "obesity"
        
    bmiround = round(bmi, 2)
    print(f"Your BMI is: {bmiround} and it is {bmiprint}.")

elif age <= 20:
    
    per = ""
    
    print("Are you girl or boy? (girl/boy)")
    response1 = input()

    if response1 == "boy":
        if age == 2:
            if bmi < 14.7:
                per = 5
            elif bmi < 15.1:
                per = 10
            elif bmi < 15.7:
                per = 25
            elif bmi < 16.6:
                per = 50
            elif bmi < 17.6:
                per = 75
            elif bmi < 18.2:
                per = 85
            elif bmi < 18.6:
                per = 90
            else:
                per = 95
        if age == 3:
            if bmi < 14.3:
                per = 5
            elif bmi < 14.7:
                per = 10
            elif bmi < 15.3:
                per = 25
            elif bmi < 16:
                per = 50
            elif bmi < 16.8:
                per = 75
            elif bmi < 17.3:
                per = 85
            elif bmi < 17.7:
                per = 90
            else:
                per = 95
        if age == 4:
            if bmi < 14:
                per = 5
            elif bmi < 14.3:
                per = 10
            elif bmi < 14.9:
                per = 25
            elif bmi < 15.6:
                per = 50
            elif bmi < 16.4:
                per = 75
            elif bmi < 16.9:
                per = 85
            elif bmi < 17.3:
                per = 90
            else:
                per = 95
        if age == 5:
            if bmi < 13.8:
                per = 5
            elif bmi < 14.1:
                per = 10
            elif bmi < 14.7:
                per = 25
            elif bmi < 15.4:
                per = 50
            elif bmi < 16.3:
                per = 75
            elif bmi < 16.8:
                per = 85
            elif bmi < 17.3:
                per = 90
            else:
                per = 95
        if age == 6:
            if bmi < 13.7:
                per = 5
            elif bmi < 14:
                per = 10
            elif bmi < 14.6:
                per = 25
            elif bmi < 15.4:
                per = 50
            elif bmi < 16.4:
                per = 75
            elif bmi < 17:
                per = 85
            elif bmi < 17.5:
                per = 90
            else:
                per = 95
        if age == 7:
            if bmi < 13.7:
                per = 5
            elif bmi < 14:
                per = 10
            elif bmi < 14.7:
                per = 25
            elif bmi < 15.5:
                per = 50
            elif bmi < 16.6:
                per = 75
            elif bmi < 17.4:
                per = 85
            elif bmi < 18:
                per = 90
            else:
                per = 95
        if age == 8:
            if bmi < 13.8:
                per = 5
            elif bmi < 14.1:
                per = 10
            elif bmi < 14.8:
                per = 25
            elif bmi < 15.8:
                per = 50
            elif bmi < 17.1:
                per = 75
            elif bmi < 18:
                per = 85
            elif bmi < 18.7:
                per = 90
            else:
                per = 95
        if age == 9:
            if bmi < 14:
                per = 5
            elif bmi < 14.3:
                per = 10
            elif bmi < 15.1:
                per = 25
            elif bmi < 16.2:
                per = 50
            elif bmi < 17.6:
                per = 75
            elif bmi < 18.6:
                per = 85
            elif bmi < 19.5:
                per = 90
            else:
                per = 95
        if age == 10:
            if bmi < 14.2:
                per = 5
            elif bmi < 14.6:
                per = 10
            elif bmi < 15.5:
                per = 25
            elif bmi < 16.6:
                per = 50
            elif bmi < 18.2:
                per = 75
            elif bmi < 19.4:
                per = 85
            elif bmi < 20.3:
                per = 90
            else:
                per = 95
        if age == 11:
            if bmi < 14.6:
                per = 5
            elif bmi < 15:
                per = 10
            elif bmi < 15.9:
                per = 25
            elif bmi < 17.2:
                per = 50
            elif bmi < 18.9:
                per = 75
            elif bmi < 20.2:
                per = 85
            elif bmi < 21.2:
                per = 90
            else:
                per = 95
        if age == 12:
            if bmi < 15:
                per = 5
            elif bmi < 15.5:
                per = 10
            elif bmi < 16.4:
                per = 25
            elif bmi < 17.8:
                per = 50
            elif bmi < 19.7:
                per = 75
            elif bmi < 21:
                per = 85
            elif bmi < 22.1:
                per = 90
            else:
                per = 95
        if age == 13:
            if bmi < 15.5:
                per = 5
            elif bmi < 16:
                per = 10
            elif bmi < 17:
                per = 25
            elif bmi < 18.5:
                per = 50
            elif bmi < 20.4:
                per = 75
            elif bmi < 21.9:
                per = 85
            elif bmi < 23:
                per = 90
            else:
                per = 95
        if age == 14:
            if bmi < 16:
                per = 5
            elif bmi < 16.5:
                per = 10
            elif bmi < 17.6:
                per = 25
            elif bmi < 19.2:
                per = 50
            elif bmi < 21.2:
                per = 75
            elif bmi < 22.7:
                per = 85
            elif bmi < 23.8:
                per = 90
            else:
                per = 95
        if age == 15:
            if bmi < 16.6:
                per = 5
            elif bmi < 17.1:
                per = 10
            elif bmi < 18.3:
                per = 25
            elif bmi < 19.9:
                per = 50
            elif bmi < 22:
                per = 75
            elif bmi < 23.5:
                per = 85
            elif bmi < 24.6:
                per = 90
            else:
                per = 95
        if age == 16:
            if bmi < 17.1:
                per = 5
            elif bmi < 17.7:
                per = 10
            elif bmi < 18.9:
                per = 25
            elif bmi < 20.6:
                per = 50
            elif bmi < 22.7:
                per = 75
            elif bmi < 24.2:
                per = 85
            elif bmi < 25.4:
                per = 90
            else:
                per = 95
        if age == 17:
            if bmi < 17.7:
                per = 5
            elif bmi < 18.3:
                per = 10
            elif bmi < 19.6:
                per = 25
            elif bmi < 21.2:
                per = 50
            elif bmi < 23.4:
                per = 75
            elif bmi < 24.9:
                per = 85
            elif bmi < 26.1:
                per = 90
            else:
                per = 95
        if age == 18:
            if bmi < 18.2:
                per = 5
            elif bmi < 18.9:
                per = 10
            elif bmi < 20.2:
                per = 25
            elif bmi < 21.9:
                per = 50
            elif bmi < 24.1:
                per = 75
            elif bmi < 25.7:
                per = 85
            elif bmi < 26.9:
                per = 90
            else:
                per = 95
        if age == 19:
            if bmi < 18.7:
                per = 5
            elif bmi < 19.4:
                per = 10
            elif bmi < 20.7:
                per = 25
            elif bmi < 22.5:
                per = 50
            elif bmi < 24.8:
                per = 75
            elif bmi < 26.4:
                per = 85
            elif bmi < 27.6:
                per = 90
            else:
                per = 95
        if age == 20:
            if bmi < 19.1:
                per = 5
            elif bmi < 19.8:
                per = 10
            elif bmi < 21.2:
                per = 25
            elif bmi < 23:
                per = 50
            elif bmi < 25.4:
                per = 75
            elif bmi < 27.1:
                per = 85
            elif bmi < 28.4:
                per = 90
            else:
                per = 95

    if response1 == "girl":
        if age == 2:
            if bmi < 14.4:
                per = 5
            elif bmi < 14.8:
                per = 10
            elif bmi < 15.5:
                per = 25
            elif bmi < 16.4:
                per = 50
            elif bmi < 17.4:
                per = 75
            elif bmi < 18:
                per = 85
            elif bmi < 18.4:
                per = 90
            else:
                per = 95
        if age == 3:
            if bmi < 14:
                per = 5
            elif bmi < 14.3:
                per = 10
            elif bmi < 14.9:
                per = 25
            elif bmi < 15.7:
                per = 50
            elif bmi < 16.6:
                per = 75
            elif bmi < 17.2:
                per = 85
            elif bmi < 17.6:
                per = 90
            else:
                per = 95
        if age == 4:
            if bmi < 13.7:
                per = 5
            elif bmi < 14:
                per = 10
            elif bmi < 14.6:
                per = 25
            elif bmi < 15.3:
                per = 50
            elif bmi < 16.2:
                per = 75
            elif bmi < 16.8:
                per = 85
            elif bmi < 17.3:
                per = 90
            else:
                per = 95
        if age == 5:
            if bmi < 13.5:
                per = 5
            elif bmi < 13.8:
                per = 10
            elif bmi < 14.4:
                per = 25
            elif bmi < 15.2:
                per = 50
            elif bmi < 16.1:
                per = 75
            elif bmi < 16.8:
                per = 85
            elif bmi < 17.3:
                per = 90
            else:
                per = 95
        if age == 6:
            if bmi < 13.4:
                per = 5
            elif bmi < 13.7:
                per = 10
            elif bmi < 14.4:
                per = 25
            elif bmi < 15.2:
                per = 50
            elif bmi < 16.3:
                per = 75
            elif bmi < 17.1:
                per = 85
            elif bmi < 17.7:
                per = 90
            else:
                per = 95
        if age == 7:
            if bmi < 13.4:
                per = 5
            elif bmi < 13.8:
                per = 10
            elif bmi < 14.5:
                per = 25
            elif bmi < 15.5:
                per = 50
            elif bmi < 16.7:
                per = 75
            elif bmi < 17.6:
                per = 85
            elif bmi < 18.3:
                per = 90
            else:
                per = 95
        if age == 8:
            if bmi < 13.5:
                per = 5
            elif bmi < 13.9:
                per = 10
            elif bmi < 14.7:
                per = 25
            elif bmi < 15.8:
                per = 50
            elif bmi < 17.3:
                per = 75
            elif bmi < 18.3:
                per = 85
            elif bmi < 19.2:
                per = 90
            else:
                per = 95
        if age == 9:
            if bmi < 13.7:
                per = 5
            elif bmi < 14.2:
                per = 10
            elif bmi < 15.1:
                per = 25
            elif bmi < 16.3:
                per = 50
            elif bmi < 18:
                per = 75
            elif bmi < 19.1:
                per = 85
            elif bmi < 20.1:
                per = 90
            else:
                per = 95
        if age == 10:
            if bmi < 14:
                per = 5
            elif bmi < 14.5:
                per = 10
            elif bmi < 15.5:
                per = 25
            elif bmi < 16.9:
                per = 50
            elif bmi < 18.7:
                per = 75
            elif bmi < 20:
                per = 85
            elif bmi < 21:
                per = 90
            else:
                per = 95
        if age == 11:
            if bmi < 14.4:
                per = 5
            elif bmi < 14.9:
                per = 10
            elif bmi < 16:
                per = 25
            elif bmi < 17.5:
                per = 50
            elif bmi < 19.5:
                per = 75
            elif bmi < 20.9:
                per = 85
            elif bmi < 22:
                per = 90
            else:
                per = 95
        if age == 12:
            if bmi < 14.8:
                per = 5
            elif bmi < 15.4:
                per = 10
            elif bmi < 16.5:
                per = 25
            elif bmi < 18.1:
                per = 50
            elif bmi < 20.2:
                per = 75
            elif bmi < 21.7:
                per = 85
            elif bmi < 23:
                per = 90
            else:
                per = 95
        if age == 13:
            if bmi < 15.3:
                per = 5
            elif bmi < 15.9:
                per = 10
            elif bmi < 17.1:
                per = 25
            elif bmi < 18.7:
                per = 50
            elif bmi < 21:
                per = 75
            elif bmi < 22.6:
                per = 85
            elif bmi < 23.9:
                per = 90
            else:
                per = 95
        if age == 14:
            if bmi < 15.8:
                per = 5
            elif bmi < 16.4:
                per = 10
            elif bmi < 17.6:
                per = 25
            elif bmi < 19.4:
                per = 50
            elif bmi < 21.7:
                per = 75
            elif bmi < 23.3:
                per = 85
            elif bmi < 24.7:
                per = 90
            else:
                per = 95
        if age == 15:
            if bmi < 16.3:
                per = 5
            elif bmi < 16.9:
                per = 10
            elif bmi < 18.2:
                per = 25
            elif bmi < 19.9:
                per = 50
            elif bmi < 22.3:
                per = 75
            elif bmi < 24:
                per = 85
            elif bmi < 25.5:
                per = 90
            else:
                per = 95
        if age == 16:
            if bmi < 16.8:
                per = 5
            elif bmi < 17.4:
                per = 10
            elif bmi < 18.7:
                per = 25
            elif bmi < 20.5:
                per = 50
            elif bmi < 22.9:
                per = 75
            elif bmi < 24.7:
                per = 85
            elif bmi < 26.1:
                per = 90
            else:
                per = 95
        if age == 17:
            if bmi < 17.2:
                per = 5
            elif bmi < 17.8:
                per = 10
            elif bmi < 19.1:
                per = 25
            elif bmi < 20.9:
                per = 50
            elif bmi < 23.4:
                per = 75
            elif bmi < 25.2:
                per = 85
            elif bmi < 26.7:
                per = 90
            else:
                per = 95
        if age == 18:
            if bmi < 17.6:
                per = 5
            elif bmi < 18.2:
                per = 10
            elif bmi < 19.5:
                per = 25
            elif bmi < 21.3:
                per = 50
            elif bmi < 23.8:
                per = 75
            elif bmi < 25.7:
                per = 85
            elif bmi < 27.3:
                per = 90
            else:
                per = 95
        if age == 19:
            if bmi < 17.8:
                per = 5
            elif bmi < 18.4:
                per = 10
            elif bmi < 19.7:
                per = 25
            elif bmi < 21.6:
                per = 50
            elif bmi < 24.2:
                per = 75
            elif bmi < 26.1:
                per = 85
            elif bmi < 27.8:
                per = 90
            else:
                per = 95
        if age == 20:
            if bmi < 17.8:
                per = 5
            elif bmi < 18.5:
                per = 10
            elif bmi < 19.8:
                per = 25
            elif bmi < 21.7:
                per = 50
            elif bmi < 24.5:
                per = 75
            elif bmi < 26.5:
                per = 85
            elif bmi < 28.3:
                per = 90
            else:
                per = 95

    if per < 5:
        bmiprint = "underweight"
    elif per < 85:
        bmiprint = "normal weight"
    elif bmi < 95:
        bmiprint = "overweight"
    else:
        bmiprint = "obesity"
        
    bmiround = round(bmi, 2)
    print(f"Your BMI is: {bmiround} and it is {bmiprint}.")


