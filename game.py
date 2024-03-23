import random
while True:
    try:
        user_input = int(input("enter the level"))
        break
        while user_input < 0:
            user_input = input("enter level(hint: enter a positive number")
    except ValueError:
        print("enter a valid integer")
        break

n = random.randint(1, user_input)



while True:
    guess = int(input("put in your guess"))
    if guess < n:
        print("your number is too low")

    elif guess > n:
        print("Too large")

    else:
        print("JUST RIGHT!")
        break
