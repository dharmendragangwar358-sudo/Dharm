import os
os.system('cls')
print("Welcome to the my new calculator which can do a lot of things! Please select one of the following options:")
print("1. Rent Split")
print("2. Tip Calculator")
print("3. BMI Calculator")
print("4. Age Calculator")
options = int(input("please select an option: "))
if options == 1:
    print ("rent split")
    rent = float(input("What is the total rent? "))
    number_of_people = int(input("How many people are splitting the rent? "))
    rent_per_person = rent / number_of_people
    print ("Each person should pay: " + str(rent_per_person))
    print("Thank you for using the rent split calculator!")
elif options == 2:    
    print ("tip calculator")
    bill_amount = float(input("What is the total bill amount? "))
    tip_percentage = float(input("What percentage would you like to tip? "))
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    print ("The tip amount is: " + str(tip_amount))
    print ("The total amount is: " + str(total_amount))
    print("Thank you for using the tip calculator!")
elif options == 3:
    print ("BMI calculator")
    weight = float(input("What is your weight in kilograms? "))
    height = float(input("What is your height in meters? "))
    bmi = weight / (height ** 2)
    print ("Your BMI is: " + str(bmi))
    print("Thank you for using the BMI calculator!")
elif options == 4:
    print ("age calculator")
    current_year = int(input("What is the current year? "))
    birth_year = int(input("What is your birth year? "))
    age = current_year - birth_year
    print ("Your age is: " + str(age))
    print("Thank you for using the age calculator!")
else:
    print ("Invalid option selected. Please try again.")
