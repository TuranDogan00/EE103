secret = 3  
guess = float(input("Guess the secret number: "))
if guess>secret:
    print("Too high")
elif guess<secret:
    print("Too low")
else:
    print("Correct!")            