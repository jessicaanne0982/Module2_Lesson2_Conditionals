# Task 1

current_year = int(input("What year is it? "))

if current_year % 4 == 0 and current_year % 100 != 0:
    print(f"{current_year} is a leap year.")
elif current_year % 4 == 0 and current_year % 400 == 0:
    print(f"{current_year} is a leap year.")
else:
    print(f"{current_year} is not a leap year.")

