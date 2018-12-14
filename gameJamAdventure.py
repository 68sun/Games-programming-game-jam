##variables
action = "overview"
inventory = ["magnifying glass", "fingerprint kit"]
solved = False
fingerprint = False


##Background



##Beginning
#Ask for player name
print("PLEASE TYPE ALL COMMANDS IN LOWERCASE")
name = input("The young officer steps up to you and says 'Hi detective, can I ask what your name is?'")

#Name check
while name == "" or len(name)>20:
    name = input("'Sorry, what was that?'")
    continue

##Crime scene
#Crime scene introduction
print("'Hello detective %s, I'm officer Riley. Right this way please, the crime scene is in the front.'" % (name))
print("Officer Riley  lifts the police tape as you cross under it. You enter the house walk though until Riley brings you into the frontroom.")


while True:
    #Crime scene overview
    if action == "overview":
        print("The room itself looks like a reception or living room, with two sofas and a large arm chair positioned around a rug. Directly infront of the rug is an antique fireplace, the mantlepiece holding various trinkets and baubles.")
        print("Above the mantlepiece is a large flatscreen TV, mounted onto the wall and the screen cracked beyond repair. Lying lifeless on the rug is an elderly man, blood staining his clothes.")
        action = input("What would you like to do? Type inventory to check what items you have. Type 'go to' then what you want to investigate to look closer or to talk to a person. Type combine to combine items")

    #inventory
    elif action == "inventory":
        print(inventory)
        action = input("What would you like to do? Type inventory to check what items you have. Type 'go to' then what you want to investigate to look closer or to talk to a person. Type combine to combine items")

    #Fireplace
    elif action == "go to fireplace":
        print("You walk over to the fireplace. It seems recently used, with ash covering it. A fire poker is nestled in the back")
        print("As you pick up the poker, you see the end has a reddish tint under the soot. You decide to take the poker with you")
        inventory.append("fire poker")
        action = input("What would you like to do? Type overview to go back to a overview of the room. Type inventory to check what items you have. Type 'go to' then what you want to investigate to look closer or to talk to a person. Type combine to combine items")

    #Combine
    elif action == "combine":
        print(inventory)
        combineFirst = input("What is the first item you want to combine?")
        combineSecond = input("What is the second thing you want to combine?")
       
        
        
        if combineFirst == inventory[0] and combineSecond == inventory[2]:
            print("You use the magnifying glass on the poker and see some fingerprints, barely visible, on the handle")
            fingerprint = True
        elif combineFirst == inventory[1] and combineSecond == inventory[2] and fingerprint == True:
            print("You use the fingerprint kit on the poker and get some fingerprints to take to the lab. You should see Riley")
            solved = True
        else:
            print("That won't work, try again")

        action = input("What would you like to do? Type overview to go back to a overview of the room. Type inventory to check what items you have. Type 'go to' then what you want to investigate to look closer or to talk to a person. Type combine to combine items")

    #Riley
    elif action == "go to riley":
        if solved == True:
            print("Riley turns to you 'You did it detective %s! We can run these fingerprints through the system and find the killer!" % name)
            print("THE END")
            break
        else:
            print("We need to find the killer, detective. maybe look at the fireplace?")
            action = input("What would you like to do? Type overview to go back to a overview of the room. Type inventory to check what items you have. Type 'go to' then what you want to investigate to look closer or to talk to a person. Type combine to combine items")

    #Incorrect action
    else:
        print("That is an invalid action")
        action = input("What would you like to do? Type overview to go back to a overview of the room. Type inventory to check what items you have. Type 'go to' then what you want to investigate to look closer or to talk to a person. Type combine to combine items")


                 








    

