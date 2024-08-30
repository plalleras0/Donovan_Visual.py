import random
my_num = random.randint(1, 11)
while True :
    Number = input("choose a number between 1 and 10:")
    if str(Number) == "quit":
        break
    else : 
        if int(Number) < my_num:
            print("you guessed too low.")
        elif int(Number) >my_num:
            print("you guessed too high")
        elif int(Number) ==my_num:
            print("you guessed the correct number") 
            break
        elif int(Number) > 12:
            print("you are putting the incorrect number")