arcana = 0
MAX_ARCANA = 30
hp = 20
has_firebolt = False
has_leather_armour = False 
has_spear = False 
has_torch = False

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
        has_firebolt = True
        print("you look around the cabin and see a beadroom with studded leather armor on a stand in the corner")
        
        question = "what will you do"
        a = "put on the armor"
        b = "go to sleep"
        answer = input("{}\nA.{} B.{}".format(question, a, b,)).lower()

        if answer == a or answer == "a":
            print("you put the armor on and now you have 10 more hp")
            has_leather_armor = True
            print("you explore the house and find a bed on fall down and go to sleep")
            print("misterious creature visits you while you are asleep telling you to go to duras")
            print("when you wake up you feel compelled to go to duras")
            print("along the way you see 3 goblins gurading the gate to duras")
            print("the notice you and draw their daggers")
            while True:
                question = "what will you do"
                a = "run"
                b = "fight"
                answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()

                if answer == a or answer == "a":
                    print("you try to run from the goblins but they throw a dagger at you")
                    print("the dagger hits you a the back of the leg you fall over and the goblins pounce")
                    print("you are stabbed and die")
                    
                elif answer ==  b or answer == "b":
                    print("the goblins start running towards you")
                    #-------------------------------------------------------------attack 1-----------------------------------------------------
                    question = "how will you attack"
                    a = "melee"
                    b = "spell"
                    answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()

                    if answer == a or answer == "a":
                        print("you hit one of the goblins in the face he takes 5 damage")
                        if has_spear == True:
                            print("you also hit them with your spear you deal 10 damage total")
                            print("you have killed a goblin 2 left")
                            print("the goblins both stab you and you take 5 damage per goblin 10 damage total")
                        else:
                            print("the goblins each hit you for 5 damage 15 total")
                    
                    elif answer ==  b or answer == "b":
                        print("you try to cast firebolt")
                        if has_firebolt == True:
                            print("the cast is succsesful you hit a goblin for 10 damage and he dies 2 goblins left")
                            print("the goblins each hit you for 5 damage 10 total")
                        else:
                            print("the spell fails you hit yourself for 15 damage")
                            print("the goblins all hit you for 5 damage each you die")
                            break
                            #--------------------------------------------attack 2----------------------------------------------------------
                question = "how will you attack"
                a = "melee"
                b = "spell"
                answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()

                if answer == a or answer == "a":
                    print("you hit one of the goblins in the face he takes 5 damage and he dies ")
                    if has_spear == True:
                        print("you also hit them with your spear you deal 10 damage total")
                        print("you have killed a goblin 1 left")
                        print("the goblin stabs you and you take 5 damage per goblin 5 damage total")

                    else:
                        print("the goblins each hit you for 5 damage 10 total")

                
                elif answer ==  b or answer == "b":
                    print("you try to cast firebolt")
                    if has_firebolt == True:
                        print("the cast is succsesful you hit a goblin for 10 damage and he dies 1 goblins left")
                    else:
                        print("the spell fails you hit yourself for 15 damage")
                        print("the goblins all hit you for 5 damage each you die")
                        break
                
                
                #------------------------------------------attack 3-------------------------
                question = "how will you attack"
                a = "melee"
                b = "spell"
                answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()

                if answer == a or answer == "a":
                    print("you hit one of the goblins in the face he takes 5 damage")
                    if has_spear == True:
                        print("you also hit them with your spear you deal 10 damage total")
                        print("you have killed a goblin 0 left")
                        print("you have killed all the goblins nice")

                    else:
                        print("the goblins each hit you for 5 damage 10 total")
                        print("you die")
                        break
                
                
                
                elif answer ==  b or answer == "b":
                    print("you try to cast firebolt")
                    if has_firebolt == True:
                        print("the cast is succsesful you hit a goblin for 10 damage and he dies 0 goblins left")
                        print("you have killed all the goblins nice")
                    else:
                        print("the spell fails you hit yourself for 15 damage")
                        print("the goblins all hit you for 5 damage each you die")
                        break
                
                
                print("you may now enter duras")
                print("this is the end of your travels adventurer")
                print("you win")
                break
            

#-----------------------------------path to gobbs answer b---------------------------------
        elif answer ==  b or answer == "b":
            print("misterious creature visits you while you are asleep telling you to go to duras")
            print("when you wake up you feel compelled to go to duras")
            print("along the way you see 3 goblins gurading the gate to duras")
            print("the notice you and draw their daggers")
            while True:
                question = "what will you do"
                a = "run"
                b = "fight"
                answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()

                if answer == a or answer == "a":
                    print("you try to run from the goblins but they throw a dagger at you")
                    print("the dagger hits you a the back of the leg you fall over and the goblins pounce")
                    print("you are stabbed and die")
                    
                elif answer ==  b or answer == "b":
                    print("the goblins start running towards you")
                    #-------------------------------------------------------------attack 1-----------------------------------------------------
                    question = "how will you attack"
                    a = "melee"
                    b = "spell"
                    answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()

                    if answer == a or answer == "a":
                        print("you hit one of the goblins in the face he takes 5 damage")
                        if has_spear == True:
                            print("you also hit them with your spear you deal 10 damage total")
                            print("you have killed a goblin 2 left")
                            print("the goblins both stab you and you take 5 damage per goblin 10 damage total")
                        else:
                            print("the goblins each hit you for 5 damage 15 total")
                    
                    elif answer ==  b or answer == "b":
                        print("you try to cast firebolt")
                        if has_firebolt == True:
                            print("the cast is succsesful you hit a goblin for 10 damage and he dies 2 goblins left")
                            print("the goblins each hit you for 5 damage 10 total")
                        else:
                            print("the spell fails you hit yourself for 15 damage")
                            print("the goblins all hit you for 5 damage each you die")
                            break
                            #--------------------------------------------attack 2----------------------------------------------------------
                question = "how will you attack"
                a = "melee"
                b = "spell"
                answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()

                if answer == a or answer == "a":
                    print("you hit one of the goblins in the face he takes 5 damage and he dies ")
                    if has_spear == True:
                        print("you also hit them with your spear you deal 10 damage total")
                        print("you have killed a goblin 1 left")
                        print("the goblin stabs you and you take 5 damage per goblin 5 damage total")

                    else:
                        print("the goblins each hit you for 5 damage 10 total")

                
                elif answer ==  b or answer == "b":
                    print("you try to cast firebolt")
                    if has_firebolt == True:
                        print("the cast is succsesful you hit a goblin for 10 damage and he dies 1 goblins left")
                    else:
                        print("the spell fails you hit yourself for 15 damage")
                        print("the goblins all hit you for 5 damage each you die")
                        break
                
                
                #------------------------------------------attack 3-------------------------
                question = "how will you attack"
                a = "melee"
                b = "spell"
                answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()

                if answer == a or answer == "a":
                    print("you hit one of the goblins in the face he takes 5 damage")
                    if has_spear == True:
                        print("you also hit them with your spear you deal 10 damage total")
                        print("you have killed a goblin 0 left")
                        print("you have killed all the goblins nice")

                    else:
                        print("the goblins each hit you for 5 damage 10 total")
                        print("you die")
                        break
                
                
                
                elif answer ==  b or answer == "b":
                    print("you try to cast firebolt")
                    if has_firebolt == True:
                        print("the cast is succsesful you hit a goblin for 10 damage and he dies 0 goblins left")
                        print("you have killed all the goblins nice")
                    else:
                        print("the spell fails you hit yourself for 15 damage")
                        print("the goblins all hit you for 5 damage each you die")
                        break
                
                
                print("you may now enter duras")
                print("this is the end of your travels adventurer")
                print("you win")
                break


                    

                    
                

        

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
                
            else:
                print("that is not an answer")

#------------------------------------answer b go north-------------------------------------
        elif answer ==  b or answer == "b":
            print("you look around and see nothing but a small cabin in the distance")
        else:
            print("that is not an answer")


    #----------------------------west / big sidetrack ----------------------
    elif answer == c or answer == "c":
        print("you find a beach")

    else:
        print("thas is not an answer")


    break

print("gg")