# os adds interactions with a users operating system, and time adds functions related to timing and delays
import os, time
#prints a string to the console by printing each letter individually in a loop that has a delay between runs
def slowText(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    return text
#puts  the player in the start screen by asking for a name and describing the initial situation
def start():
    global playerName
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("Welcome to the game! Please enter your name: ")
    playerName = input()
    slowText("Hello, {}! You find yourself in the living room of a mysterious house.".format(playerName))
    slowText("From here, you can go to the kitchen, the bedroom, or the garden.")
    # Further game logic would go here
    livingRoom()
#tells the player what is going on in the living rooms and gives them options on where they can go
def livingRoom():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Backpack: " + str(backpack))
    slowText("You are in the living room. There are doors to the kitchen, bedroom, and garden. You can also look for items.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "kitchen":
        kitchen()
    elif choice == "bedroom":
        bedroom()
    elif choice == "garden":
        garden()
    elif choice == "look for items":
        if searchPack(backpack, "oreos"):
            slowText("You decided to scan the room. You find nothing")
            time.sleep(2)
        else:
            slowText("You decided to scan the room. You find a half-eaten pack of oreos. Do you want to pick them up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("oreos")
            time.sleep(2)
        livingRoom()
    else:
        print("Invalid choice. Please try again.")
        livingRoom()

def kitchen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Backpack: " + str(backpack))
    slowText("You are in the kitchen. There is a door to the living room and a window to a knife shaped helicopter pad. You can also look for items.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room": #this variable is how the user picks which room to go to
        livingRoom()
    elif choice == "look for items":
        if searchPack(backpack, "paper clip"):
            slowText("You decided to scan the room. You find nothing")
        else:
            slowText("You decided to scan the room. You open up a junk drawer and find a paper clip. Do you want to pick it up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("paper clip")    
        time.sleep(2)
        kitchen()
    elif choice == "open window":
        openWindow()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1.5)
        kitchen()

def garden():
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the garden. There is a door to the living room")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room": #this variable is how the user picks which room to go to
        livingRoom()
    elif choice == "look for items":
        if searchPack(backpack, "Hammer"):
            slowText("You decided to scan the room. You find nothing")
        else:
            slowText("You decided to scan the room. You find a extremely large hammer. Do you want to pick it up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("Hammer")    
        time.sleep(2)
        garden()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1.5)
        garden()

def bedroom():
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the bedroom. There is a door to the living room. You can also look for items")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room": #this variable is how the user picks which room to go to
        livingRoom()
    elif choice == "look for items":
        if searchPack(backpack, "Play Station 5"):
            slowText("You decided to scan the room. You find nothing")
            time.sleep(2)
        else:
            slowText("You decided to scan the room. You find a play station 5 in the corner. Do you want to pick it up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("Play Station 5")
            time.sleep(2)
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1.5)
    bedroom()
def searchPack(pack, item):
    found = False
    for i in range(len(pack)):
        if pack[i] == item:
            found = True
    return found
def openWindow():
    slowText("You decided to try to open the window.")
    if searchPack(backpack, "paper clip") == True:
        slowText("you use the paper clip to unlock the lock on the window. Now it is open, but there is a wolf.")
        if searchPack(backpack, "oreos") == False:
            slowText("You use the oreos to distract the wolf.")
            slowText("Congradulations you made it out of the house alive!!!")
        else:
            slowText("You can't evade the wolf right now.")
    else:
        slowText("Unfortunately, you can't unlock the window.")





#keeps track of the players name
playerName = ""
backpack = []
start()