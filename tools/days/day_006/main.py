# Day 6 - BMI Checker

from days.day_006.files.helpers import *

def day_006():
	title("BMI CHECKER")
	height = float(nli("How tall are you in cm?"))
	weight = float(nli("How much do you weigh in kg?"))
	# Calculation for bmi, rounded to 2 decimal places
	bmi = round(weight/(height/100)**2, 2)
	if bmi < 18.5:
		weight_class = 'underweight'
	elif bmi < 25:
		weight_class = 'normal weight'
	elif bmi < 30:
		weight_class = 'overweight'
	elif bmi < 35:
		weight_class = 'obese'
	else:
		weight_class = 'clinically obese'

	nls(f"Your BMI is {bmi}\nYou are {weight_class}")
	