# example 2
a = int(input("Enter the first number."))
b = float(input("Enter the second number.")

product = a*b
answer = " "
attempt_count = 0
attempt_limit = 2
out_of_attempts = False
while answer != product and not out_of_attempts:
    if attempt_count < attempt_limit:
        answer = input("Enter the product of the two numbers.")
        attempt_count += 1
    else:
        out_of_attempts = True
if out_of_attempts:
    print("you are wrong.")
else:
    print("you are correct.")