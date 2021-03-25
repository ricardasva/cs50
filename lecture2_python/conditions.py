import sys

number = input("Enter a number: ")
try:
    number = int(number)
except ValueError:
    print(f"{number} is not a number" )
    sys.exit(1)

if number > 0:
    print(f"{number} is bigger then 0")
elif number < 0:
    print(f"{number} is smaller then 0")
else:
    print(f"{number} is zero")