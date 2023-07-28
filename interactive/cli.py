from random import randint

min_number = int(input("Enter the minimum number: "))
max_number = int(input("Enter the maximum number: "))

random_number = randint(min_number, max_number)

print(f"Your random number is {random_number}")