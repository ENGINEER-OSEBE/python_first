i = 1
while i <= 5:
    print(i)
    i += 1


print("End the programme.")


secret_word = "baby"
guesses = " "
guess_count = 0
guess_limit = 2
out_of_guesses = False
while guesses != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guesses = input("Enter the secret_word.")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("you lose")

else:
    print("you win.")

# example 2
a = int(input("Enter the first number."))
b = float(input("Enter the second number."))

product = a*b
answer = " "
attempt_count = 0
attempt_limit = 2
out_of_attempts = False
while answer != product and not out_of_attempts:
    if attempt_count < attempt_limit:
        answer = input("Enter the product of the two numbers.")
        product = input("Enter the product.")

        attempt_count += 1
    else:
        out_of_attempts = True
if out_of_attempts:
    print("you are wrong.")
else:
    print("you are correct.")
