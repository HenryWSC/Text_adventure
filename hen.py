#starting beach
print("you run throught the woods and see a break in the trees, as you break throught the tree lines you see a beach and hear crashes of waves. you seem safe.")

print("as you walk along the beach you come across a light house it seems old and abandoned")
question = "what will you do?"
a = "enter the light house"
b = "continue walking along the beach"

answer = input("{}\nA.{} B.{}".format(question, a, b)).lower()

if answer == a or answer == "a":
    print("you enter a lighthouse the floor boards creek under your step and you find a small letter")
    print("as your open the letter it says to come to Duras as soon as possible")
elif answer == "b":
    print("you walk along the beach the sound of waves crash in the background and you find a small wrecked boat")
elif answer != a and answer != "a" and answer != b and answer != "b":
    print("")

