import random
my_world = random.choice(['python', 'java', 'javascript', 'ruby', 'html', 'css'])
print (my_world)
while True :
    world= input("choose a world of this list : 'python', 'java', 'javascript', 'ruby', 'html', 'css' : ")
    if (world) == "quit":
        break
    else : 
        if (world) ==my_world:
            print("you guessed the correct world") 
            break
        elif (world) == ("choose a world of this list : 'python', 'java', 'javascript', 'ruby', 'html', 'css'") :
            print("")
        else :
            print("your world is not in the list or is not correct")