Number = input("choose a number between 1 and 10:")
if int(Number) < 3:
    print("you guessed too low.")
    Number = input("choose a number between 1 and 10:")
elif int(Number) >3:
    print("you guessed too high")
elif int(Number) ==3:
    print("you guessed the correct number")
if int(Number) >10:
    print("you are putting the incorrect number")
    