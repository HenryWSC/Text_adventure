

light_house = False
        #starting beach
print("you run throught the woods and see a break in the trees, as you break throught the tree lines you see a beach and hear crashes of waves. you seem safe.")

print("as you walk along the beach you come across a light house it seems old and abandoned")

H_question = "what will you do"
a = "Go into the light house"
b = "continue walking along the beach"
answer = input("{}\nA.{} B.{}".format(H_question, a, b,)).lower()

#setting light_house true/false start
if answer == a or answer == "a":
        light_house = True
if light_house == False:
#setting light_house true/false end
                if answer == b or answer == "b":
                                print("you continue walking along the beach until you find a wrecked rowboat")
                        
                #wrecked boat
                H_question2 = "what will you do"
                a = "Investigate the boat"
                answer = input("{}\nA.{}".format(H_question, a,)).lower()

                if answer == a or answer == "a":
                        print("you investigate the row boat and find string, a stick, a sharp flint and wood kindle")
                        #Investigate row boat
                H_question3 = "what will you do"
                a = "make a spear"
                b = "make a torch"
                answer = input("{}\nA.{} B.{}".format(H_question, a, b,)).lower()
                        #Investigate row boat ends

                        #making spear and torch
                if answer == b or answer == "b":
                                has_torch = True
                                print("you make a torch by wrapping string around a stick and lighting it with a flint, but the sun starts to set")
                answer == b or answer == "b"
                has_spear = True
                print("you make a spear out of the flint and sticks but the sun starts to set")

                H_question3 = "what will you do"
                a = "make a fire"
                b = "go look for berries"
                answer = input("{}\nA.{} B.{}".format(H_question, a, b,)).lower()
                        #making spear ends
                        
                if answer == b or answer == "b":
                        has_spear = True
                        print("")

                        #making fire
                if answer == a or answer == "a":
                        print("you make a fire smoke plums up and may attract predetors")
                        print("what do you do?")
                                
                        a = "put out the fire"
                        b = "leave the fire going"
                elif answer == b or answer == "b":
                        #jacksons berries
                        print("you find a bush of berries")
                                
                        a = ""
                        b = ""
                        answer = input("{}\nA.{} B.{}".format(H_question, a, b, )).lower()
                        #making fire ends

                        #wolves encounter
                while True:
                        if answer == a or answer == "a":
                                question = "3 wolves appear behind you from the forest"
                        a = "run away"
                        b = "fight"
                        answer = input("{}\nA.{} B.{}".format(question, a, b)).lower()

                        if answer == a or answer == "a":
                                print("you run away into the woods until you find a cabin")
                                #go into jacksons
                                
                        elif answer ==  b or answer == "b":
                                print("as you fight the wolfes they outnumber and overwhelm you and you die")
                                break
                        
                        else:
                                print("that is not an answer")

                                #going for berries
                        if answer == a or answer == "a":
                                print("you find a bush of berries")

                        question3 = "what would you like to do now "
                        a = "gather berries"
                        b = "you go into the cabin"
                        answer = input("{}\nA.{} B.{}".format(H_question, a, b, )).lower()
                                #berries go to jackson
else:  
                        print("you walk into the lighthouse and find a chest you open it and you find a letter telling you to go to duras")
                        print("you feel compelled to go to duras and when you do you find 3 golblins blocking your path")
                        #lighthouse ends      
        #go to golbin encounter





























































































































#starting beach real
#STORY = [["you travel to duras","you find a small wrecked boat, you investigat the boat and find string, a stick, a sharp stone and some wood kindle",
#              "do you make a torch, spear or fire", "you make a fire",
 #             "smoke plums from the fire and could attract animals, do you put it out?",
  #            "you keep the fire going and after a while you hear wolves howling and you hear shuffling behind you. You look behind and see 5 wolves coming out the forest",
   ##          "you die from the wolves"]
     #         [#lighthouse 
      #        "you enter the lighthouse and find a letter telling you to get to the kingdom of duras ASAP", 
       ####     "you go into the forest to look for food and you find a bush of berries"
           #    #smoke plums
            #   "you put out the fire and it starts to get cold since its now midnight do you go get food or go to sleep", 
             #  "you die from hyperthermia",
               #wolf attack 
              # "you run from the wolf attacking you and enter the woods you survive on 3 HP" ]]

#OPTIONS = [["enter the lighthouse", "go along the beach"],
 #          ["go to duras", "go to the forest to look for food"],
  #         ["continue along the beach", "enter the lighthouse"],
   #        ["go back to the light house","investigate the boat"],
    #        ["make a fire", "make a spear", "make a torch"],
     #       ["look for food", "make fire"],
      #      ["put out the fire", "keep the fire going"],
       #    ["run", "fight"]]
#SHORT_OPTIONS =["a", "b", "c"]
#ANSWERS = []





























































































































































































































































































































































































































































































































































































































