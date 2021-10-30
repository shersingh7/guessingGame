secret_number = 7

i = 0
while i < 3:
    guess = int(input("Guess the number: "))
    if(guess == secret_number):
        print("Right Guess")
        break
    else:
        print("Try Again!!!")
    i+1

