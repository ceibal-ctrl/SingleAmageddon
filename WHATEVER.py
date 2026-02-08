from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year

birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print(f"You are {age} years old.")

def calculate_age_2050(birth_year):
    target_year = 2050
    return target_year - birth_year
age_2050 = calculate_age_2050(birth_year)
print(f"In the year 2050, you will be {age_2050} years old.")