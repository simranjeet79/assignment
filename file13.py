# 13.Write a program that asks the user for their birth year and calculates their age.
from datetime import datetime
Year1 =int(input("Enter your year of birth:"))
#Year2 = int(input("Enter the current year:"))
current_year = int(input("Enter the current year:"))

print("current age:", current_year - Year1)
