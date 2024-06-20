

#intro
start = input("welcome adventurer are you ready to enter the world of the infinity acres")
if start == "yes":
    print("i hope you survive")
else:
    print("i pray for your death")

#explaining the game
print("during this adventure you will have to battle monsters and the environment in order to survive")
print("your goal is to make it to duras, the royal capital")
print("you have 20 hp to start find armor to increase it")

#start
print("you find yourself in a forest")

question = "what direction will you go"
a = "north"
b = "east"
c = "west"
answer = input("{}\nA.{} B.{} C.{}".format(question, a, b, c)).lower()

if answer == a or answer == "a":
    print("you spot a bear running towards you")
elif answer == "":
    print("you spot a bear running towards you")
elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer:
    print("you spot a bear running towards you")
else:
    print("you spot a bear running towards you")


#bear encounter
print("he is getting closer")
question = "what will you do"
a = "fight"
b = "run"
answer = input("{}\nA.{} B.{}".format(question, a, b)).lower()

while True:
    if answer == a or answer == "a":
        print("you land a clean right hook across the bears face, he is unfased.")
        print("the bear slashes your stomach, your guts spill out and you die")
        break
    elif answer == b or answer == "b":
        print("you are able to get away from the bear")
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer:
        print("")
    else:
        print("thats not an answer")
        
    # major crossroad north,east and west
        print("you find yourself further into the woods")

    question2 = "what direction will you go"
    a = "north"
    b = "east"
    c = "west"
    answer = input("{}\nA.{} B.{} C.{}".format(question, a, b, c)).lower()

    #----------------------------noth / main path---------------------------
    if answer == a or answer == "a":
        print("you find a cabin!")
        print("you see a small chest in the middle of the room")
        print("you open it an see a spell scroll that contains firebolt")
        

    #----------------------------east / short sidetrack---------------------
    elif answer == b or answer == "b":
        print("you find a bush of berries")
        
        question3 = "what would you like to do now "
        a = "gather berries"
        b = "go deeper into the woods"
        answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()
#----------------------------------answer a-------------------------------------
        if answer == a or answer == "a":
            print("you start picking up the berries but then hear a howling in the distance")
            question = "you quickly put all the berries into your bag and run away"
            a = "run north"
            b = "run west"
            answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()

            if answer == a or answer == "a":
                print("you run north untill you find a a cabin")
#-----------------------------------link to beach answer b-------------------------------                
            elif answer ==  b or answer == "b":
                print("you run west untill you stumble onto a deserted beach")
                
            elif answer != a and answer != "a" and answer != b and answer != "b" and answer:
                print("huh")
            else:
                print("that is not an answer")

#------------------------------------answer b go north-------------------------------------
        elif answer ==  b or answer == "b":
            print("you look around and see nothing but a small cabin in the distance")
        
        elif answer != a and answer != "a" and answer != b and answer != "b" and answer:
            print("huh")
        else:
            print("that is not an answer")


    #----------------------------west / big sidetrack ----------------------
    elif answer == c or answer == "c":
        print("you find a beach")


    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer:
        print("huh")
    else:
        print("thas is not an answer")

















print("gg")