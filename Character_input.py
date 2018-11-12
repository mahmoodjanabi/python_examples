import datetime

#Get name
name = input("Please input name: ")
print("Hi " + name.title() + "!")

#Get age
age = input("Please input age: ")
print("Your age is " + age)

#Get current date
now = datetime.datetime.now()

year = int(now.year)
age_to_100 = 100-int(age)
predicted_year = age_to_100 + year
print("You're gonna be a 100 years old at " + str(predicted_year))