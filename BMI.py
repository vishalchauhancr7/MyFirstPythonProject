import math
weight = 72
height = 1.73

bmi = (float(weight) / (math.pow(float(height), 2)))
print("bmi: ")
print(float(bmi))

if 25 < bmi < 30:
    print("Person is overweight")
elif 18 < bmi <= 25:
    print("Person is not overweight")
elif bmi > 30:
    print("Obesity")
else:
    print("Person is underweight")







