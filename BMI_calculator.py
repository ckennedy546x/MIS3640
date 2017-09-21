import math

weight = input('What is your weight in lbs? ')
weight = float(weight)

height = input('What is your height in inches? ')
height = float(height)

bmi = 703 * weight / (height * height)

if bmi <=18.5:
    print('Your BMI is {}.'.format(bmi))
    print('Underweight')

elif bmi <= 24.9:
    print('Your BMI is {}.'.format(bmi))
    print('Normal Weight')

elif bmi <= 29.9:
    print('Your BMI is {}.'.format(bmi))
    print('Overweight')

else:
    print('Your BMI is {}.'.format(bmi))
    print('Obesity')

 
