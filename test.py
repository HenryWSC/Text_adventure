question = ""
a = ""
b = ""
answer = input("{}\nA.{} B.{}".format(question, a, b, )).lower()

if answer == a or answer == "a":
    print("")
    
elif answer ==  b or answer == "b":
    print("")
    
elif answer != a and answer != "a" and answer != b and answer != "b" and answer:
    print("huh")
else:
    print("that is not an answer")