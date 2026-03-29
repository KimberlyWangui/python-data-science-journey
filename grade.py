first_unit = float(input("Enter the first unit: "))
second_unit = float(input("Enter the second unit: ")) 
third_unit = float(input("Enter the third unit: "))
fourth_unit = float(input("Enter the fourth unit: "))
fifth_unit = float(input("Enter the fifth unit: "))
sixth_unit = float(input("Enter the sixth unit: "))

average = (first_unit + second_unit + third_unit + fourth_unit + fifth_unit + sixth_unit) / 6

if 70 <= average <= 100:
  print('Grade: A')
elif 60 <= average <= 69:
  print('Grade: B')
elif 50 <= average <= 59:
  print('Grade: C')
elif 40 <= average <= 49:
  print('Grade: D')
elif 0 <= average <= 39:
  print('Grade: F')
else:
  print('The entry is erroneous')