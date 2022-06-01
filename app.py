secret_number = 5
guess_count = 0
guess_limit = 5
print("""
Welcome to the guessing game!


Guess a number between 1-10...


If you guess right, you win a prize!


Also, remember to stay inbounds...


You have 5 tries, Good Luck!


""")
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("""

You guessed correctly! Here's your prize!


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



        """)
        break
    elif guess in range(10, 1000000):
        print("Your guess is out of range!")
    elif guess in range(1, 4):
        print("Your guess is cold...")
    elif guess in range(4, 5):
        print("Your guess is hot!!")
    elif guess in range(6, 7):
        print("Your guess is hot!!")
    elif guess in range(7, 10):
        print("Your guess is cold...")
else:
    print("Darn, better luck next time, GG's!")
