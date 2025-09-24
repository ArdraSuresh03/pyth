import random
secret_number=random.randint(1,9)
guess_user=int(input("Guess a number between 1 and 9 : "))
if guess_user < secret_number:
    print("too low try again")
elif guess_user > secret_number:
    print("too high try again")
else :
    print("You are Right")
    print(f"The secret number is {secret_number}")    