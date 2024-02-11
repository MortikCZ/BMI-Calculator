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
    
    per = 0
    
    print("Are you girl or boy? (girl/boy)")
    gender = input()

    percentiles_boy = [5, 10, 25, 50, 75, 85, 90, 95]
    percentiles_girl = [5, 10, 25, 50, 75, 85, 90, 95]

    if gender == "boy":
        percentiles = percentiles_boy
    elif gender == "girl":
        percentiles = percentiles_girl

    for age_percentiles in [
        [14.7, 15.1, 15.7, 16.6, 17.6, 18.2, 18.6],
        [14.3, 14.7, 15.3, 16, 16.8, 17.3, 17.7],
        [14, 14.3, 14.9, 15.6, 16.4, 16.9, 17.3],
        [13.8, 14.1, 14.7, 15.4, 16.3, 16.8, 17.3],
        [13.7, 14, 14.6, 15.4, 16.4, 17, 17.5],
        [13.7, 14, 14.7, 15.5, 16.6, 17.4, 18],
        [13.8, 14.1, 14.8, 15.8, 17.1, 18, 18.7],
        [14, 14.3, 15.1, 16.2, 17.6, 18.6, 19.5],
        [14.2, 14.6, 15.5, 16.6, 18.2, 19.4, 20.3],
        [14.6, 15, 15.9, 17.2, 18.9, 20.2, 21.2],
        [15, 15.5, 16.4, 17.8, 19.7, 21, 22.1],
        [15.5, 16, 17, 18.5, 20.4, 21.9, 23],
        [16, 16.5, 17.6, 19.2, 21.2, 22.7, 23.8],
        [16.6, 17.1, 18.3, 19.9, 22, 23.5, 24.6],
        [17.1, 17.7, 18.9, 20.6, 22.7, 24.2, 25.4],
        [17.7, 18.3, 19.6, 21.2, 23.4, 24.9, 26.1],
        [18.2, 18.9, 20.2, 21.9, 24.1, 25.7, 26.9],
        [18.7, 19.4, 20.7, 22.5, 24.8, 26.4, 27.6],
        [19.1, 19.8, 21.2, 23, 25.4, 27.1, 28.4],
    ][age - 2]:
        if bmi < age_percentiles:
            per = percentiles.pop(0)
            break


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


