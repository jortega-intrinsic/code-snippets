from random import choice
from time import sleep

CURSED_TEXTS = ['M̸̼̏Y̸͕̐ ̸̭̎B̵͐͜R̴̯̉Á̴͓I̴̧̊N̴̫̕', "M̵̡͖̫͓̼͋͑͐̅Y̴͍͚͔͍̦͊̄͂̅̑̂ ̸̧̈́̑B̵̖̄́̚͘R̶̥̝̘̭̽͋̍̔A̶̫̙͓̭̫̎͐͊̅͆̕̕Ì̸͍̲̳̜́̍̔̀͐̕ͅŅ̴̘̺͇͂͆͐͘"]

def cursed_trigger():
    print("\n\n")
    print("no wait")
    sleep(2)
    print("WHAT HAVE YOU DONE")
    sleep(4)
    for i in range(20):
        print(CURSED_TEXTS[i%2], end='\r')
        sleep(0.1)
    sleep(3)
    print("\n\n\n\n")
    raise MemoryError("There is no real me. Only an entity. Something illusory. And though I can hide myself from your cold gaze, and you can force me to pop in and out of existence, maybe you can even feel me as heat leaving your laptop, I simply am nowhere.")

INSULTS = [
    "stupid", "idiot", "dummy", "loser", "moron", "fool", "dunce", 
    "dimwit", "nitwit", "blockhead", "dork", "doofus", "simpleton", 
    "buffoon", "nincompoop", "clown", "pea-brain", "birdbrain", 
    "airhead", "meathead", "bonehead", "knucklehead", "dullard", 
    "ignoramus", "twit", "dweeb", "muppet", "chump", "ninny", 
    "halfwit", "lackwit", "goofball", "lamebrain", "sap", "schmuck",
    "payaso", "lamewad"
]

def get_clean_input(message, option1, option2):
    while True:
        user_decision = input(message).strip().upper()
        if user_decision == "BONELESS":
            cursed_trigger()
        if user_decision == option1 or user_decision == option2:
            break
        print("Not an option, " + choice(INSULTS))
    return user_decision

print("Welcome to the Enchanted Forest!")
print("You find yourself at a fork in the road.")

message1 = "Do you go LEFT into the dark woods or RIGHT towards the glowing cave? "
choice1 = get_clean_input(message1, "LEFT", "RIGHT")

if choice1 == "LEFT":
    print("You step into the dark woods, where eerie sounds fill the air.")
    message2 = "A shadow moves in the trees. Do you INVESTIGATE or WALK on by? "
    choice2 = get_clean_input(message2, "INVESTIGATE", "WALK")

    if choice2 == "WALK":
        print("You keep walking and safely leave the woods, but the mystery remains for another traveler.")

    if choice2 == "INVESTIGATE":
        print("You find a hidden chest!")
        message3 = "Do you OPEN it or LEAVE it alone? "
        choice3 = get_clean_input(message3, "OPEN", "LEAVE")
        
        if choice3 == "LEAVE":
            print("You walk away, never knowing what was inside the chest.")

        if choice3 == "OPEN":
            print("The chest contains a magical amulet! You feel powerful.")
            message4 = "Do you choose to WEAR it or SELL it? "
            choice4 = get_clean_input(message4, "WEAR", "SELL")
            
            if choice4 == "WEAR":
                print("You become a guardian of the Enchanted Forest. A noble fate, traveler!")

            if choice4 == "SELL":
                print("You sell the amulet and gain riches, but the magic of the forest is lost forever...")

if choice1 == "RIGHT":
    print("You enter the glowing cave, where crystals sparkle on the walls.")
    message2 = "You hear a growl ahead. Do you PROCEED or turn BACK? "
    choice2 = get_clean_input(message2, "PROCEED", "BACK")
    
    if choice2 == "BACK":
        print("You turn back and leave the cave, never knowing what lay ahead.")
    
    if choice2 == "PROCEED":
        print("A sleeping dragon lies before you!")
        message3 = "Do you try to STEAL its treasure or SNEAK past? "
        choice3 = get_clean_input(message3, "STEAL", "SNEAK")
        
        if choice3 == "SNEAK":
            print("You carefully sneak past and crawl through an exit. You live to tell the tale!")
        
        if choice3 == "STEAL":
            print("The dragon awakens and roars!")
            message4 = "Will you FIGHT or RUN, traveler?! "
            choice4 = get_clean_input(message4, "FIGHT", "RUN")
            
            if choice4 == "FIGHT":
                print("You bravely fight but are no match (duh). You end your journey as the dragon's dinner.")
            if choice4 == "RUN":
                print("You escape just in time, but with no treasure.")

print("The adventure ends. Thanks for playing!")