
###
# BMI Calculator
#
height = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')
height = int(height)
weight = int(weight)
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Your BMI is', bmi)
print('Check on the Internet if your BMI is ok!!')


###################################################

import random
print("Dice rolling simulator")
for i in range(5):
    dice_roll = random.randint(1,6)
    print(dice_roll, end=" ")

#################################################

wartoscp = 1

print(type(wartoscp))

########################################################
company = "ABC Data" # Name - Company    Value- ABC      Type - String #
phone = "555-123-009" # Name- phone     Value 555-123-009     Type -String #
employees = 25 #Name employees     Value  25   Type INT#
remote_work = True #Name remote_work     Value True     Type  bool#
big_company = employees > 100 #Name  big_company     Value NO    Type bool#
income = 4500000 #Name income      Value 4500000    Type int#
income_per_person = income / employees #Name  income_per_person     Value 180000    Type INT#


###############################################################

###
# A program that calculates the sum of two numbers.
# Modify the program to calculate the sum of three numbers.
#
number3 = 21
number1 = 71
number2 = 14
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)

######################################################################

x = 7
y = 34
Z =  0
print("Before swapping: x=", x, "y=", y)

Z = y
y= x
x = Z
print("After swapping: x=", x, "y=", y)

###########################################################################

def kmh_to_ms(speed_kmh):
    speed_ms = speed_kmh * 1000 / 3600
    return speed_ms

speed_kmh = float(input("Enter speed in km/h: "))

speed_ms = kmh_to_ms(speed_kmh)
print(f"The speed in m/s is: {speed_ms:.2f} m/s")

#############################################################################
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print(f"The length of the diagonal is: {diagonal:.2f}")
#################################################################################
import math
def distance_to_horizon(height):
    distance = 3.57 * math.sqrt(height)
    return distance
height = float(input("Enter the height above the ground in meters: "))
distance = distance_to_horizon(height)
print(f"The distance to the horizon is: {distance:.2f} kilometers")
beach_height = 1.7
beach_distance = distance_to_horizon(beach_height)
print(f"\nAt the beach (height {beach_height} m), the horizon is: {beach_distance:.2f} km away")
hotel_height = 20
hotel_distance = distance_to_horizon(hotel_height)
print(f"From a hotel window at 20 m, the horizon is: {hotel_distance:.2f} km away")
##############################################################################################

total_population = 8000000000  
northern_population = 7200000000  
southern_population = total_population - northern_population
northern_percentage = (northern_population / total_population) * 100
southern_percentage = (southern_population / total_population) * 100
print(f"Population in the Northern Hemisphere: {northern_population} people")
print(f"Percentage in the Northern Hemisphere: {northern_percentage:.2f}%")
print(f"Population in the Southern Hemisphere: {southern_population} people")
print(f"Percentage in the Southern Hemisphere: {southern_percentage:.2f}%")
###############################################################################################

mat = 5
Art = 4
muzic = 5
history = 3
average = mat + Art - muzic + history / 4
print("Average grade is", average)

####################################################################################################

name = "Adam"
age = 20  
height = 175 

print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In 6 years I will be {age + 6} years old.")

##################################################################################################

father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members
print(f"Total family income is {total_income}, and income per person is {income_per_person:.2f}")

#############################################################################################
a = 3
b = 5
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
##################################################################################################
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is full_name')
#################################################################
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
cube_volume = cube_side ** 3
cube_surface_area = 6 * (cube_side ** 2)
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')
##############################################################
a = int(input('Enter the length of side a: '))
b = int(input('Enter the length of side b: '))
c = int(input('Enter the length of side c: '))
cuboid_volume = a * b * c
cuboid_surface_area = 2 * (a * b + a * c + b * c)
print(f'The volume of a cuboid with sides {a}, {b}, and {c} is {cuboid_volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, and {c} is {cuboid_surface_area}')
##########################################################
name = input('Enter your name: ')
surname = input('Enter your surname: ')

characters_in_name = len(name)
characters_in_surname = len(surname)
characters_in_full_name = len(name + ' ' + surname)

print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_full_name} characters')
##############################################################
university = "Krakow University of Economics"

abbreviation = ''.join(word[0] for word in university.split())

print(f'The abbreviation of "{university}" is {abbreviation}')
##########################################################
employee = "Mr. John May, born on 1998-02-16"

name = employee[4:8]  
surname = employee[9:12]  
date_of_birth = employee[-10:]  

initials = name[0] + surname[0]

print(f'Name: {name}')
print(f'Surname: {surname}')
print(f'Born: {date_of_birth}')
print(f'Initials: {initials}')
##############################################################
phone = input('Enter a 9-digit phone number: ')

if len(phone) == 9 and phone.isdigit():
    formatted_phone = f'{phone[:3]}-{phone[3:6]}-{phone[6:]}'
    print(f'Formatted phone number: {formatted_phone}')
else:
    print('Please enter a valid 9-digit phone number.')
    #####################################################################
print(f'a: {ord("a")}')
print(f'b: {ord("b")}')
print(f'z: {ord("z")}')
print(f'A: {ord("A")}')
print(f'B: {ord("B")}')
print(f'Z: {ord("Z")}')
print(f'1: {ord("1")}')
print(f'=: {ord("=")}')
print(f'+: {ord("+")}')
print(f'€: {ord("€")}')
#####################################################################
name = input('name:')


print(f'The letter {name[0]} has a code {ord(name[0])}')
print(f'The letter {name[1]} has a code {ord(name[1])}')
print(f'The letter {name[2]} has a code {ord(name[2])}')
print(f'The letter {name[3]} has a code {ord(name[3])}')
#######################################################################

letter1 = input('Enter the first letter: ').upper()
letter2 = input('Enter the second letter: ').upper()
difference = abs(ord(letter1) - ord(letter2)) - 1
print(f'There are {difference} letters between {letter1} and {letter2}')
###########################################################
word = chr(67) + chr(111) + chr(111) + chr(108) + chr(33)
print(word)
########################################################
import random

dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)

total = dice_roll_1 + dice_roll_2 + dice_roll_3

print(f'Dice roll 1: {dice_roll_1}')
print(f'Dice roll 2: {dice_roll_2}')
print(f'Dice roll 3: {dice_roll_3}')
print(f'Total sum of dice rolled: {total}')
####################################################
Practice makes perfect:

###
celsius = float(input('Enter temperature in Celsius: '))
kelvin = celsius + 273.15
fahrenheit = (celsius * 9/5) + 32
print(f'Temperature in Kelvin: {kelvin:.2f} K')
print(f'Temperature in Fahrenheit: {fahrenheit:.2f} °F')
########################################
height_cm = int(input('Enter your height in cm: '))
cm_per_inch = 2.54
inches_per_foot = 12
total_inches = height_cm / cm_per_inch
feet = int(total_inches // inches_per_foot)
inches = int(total_inches % inches_per_foot)
print(f'Your height is {height_cm} cm.')    
print(f'That is approximately {feet} feet and {inches} inches.')    
######################################
swift_code = input('Enter the SWIFT code: ').upper()
bank_code = swift_code[:4]
country_code = swift_code[4:6]
print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')
###############################################
distance_km = float(input('Enter the distance in km: '))
fuel_price_per_liter = float(input('Enter the fuel price per liter: '))
fuel_consumption_per_100km = float(input('Enter the fuel consumption (liters per 100 km): '))
fuel_needed = (distance_km / 100) * fuel_consumption_per_100km
total_cost = fuel_needed * fuel_price_per_liter
print(f'Total fuel needed: {fuel_needed:.2f} liters')
print(f'Total cost of transportation: ${total_cost:.2f}')
#####################################################
