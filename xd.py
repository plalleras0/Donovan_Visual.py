import random
 
options = ("papel", "piedra", "tijeras")
choices_of_pc=random.choice(options)
print(choices_of_pc)
user_ch= input("choose a world of this list : 'rock', 'paper', 'siccers': ")

def win(user_ch,choices_of_pc):
    if user_ch == choices_of_pc:
        print("tie")
                
    elif (user_ch == "rock" and choices_of_pc == "scissors") or (user_ch == "paper" and choices_of_pc == "rock") or (user_ch == "scissors" and choices_of_pc == "paper"):
        print("Won")

    else:
        print("you lose")


def user_opcions():
    while True : 
        global choices_of_pc
        global user_ch
        if user_ch == "quit":
            break

        if user_ch not in options:
            print("not allow")
            continue

user_opcions()
win(user_ch, choices_of_pc)


                
                