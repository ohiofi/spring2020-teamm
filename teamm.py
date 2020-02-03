import time

roomArray = []
itemArray = ["Red Key", "Blue Key", "Green Key", "Coin", "Coin", "Coin"]

for i in range(999):
  roomArray.append(False)
  itemArray.append(False)

roomArray[204] = "There is a long hallway to the East. The word START is written all over the walls in pen."
roomArray[304] = "There is a red door directly North and a hallway to the East"
roomArray[404] = "You are in the middle of the hallway with rooms to the East and West. There is a hallway to the South." 
roomArray[303] = "The red door was opened. The walls in this room are painted red. The only way out is the way you came in."
roomArray[502] = "You reached the end of this hallway. There are paintings on the walls."
roomArray[503] = "You are in the middle of this hallway with rooms to the North and South."
roomArray[504] = "There is a hallway to the North. The hallway you are in continues East."
roomArray[604] = "You reached a dead end. There are spikes on the ceiling."
roomArray[306] = "The room has black and white striped wallpaper. There is one dim light hanging from the ceiling. There are no other exits besides the one you entered through, from the East."
roomArray[405] = "There are walls to your East and West. There is a faint light coming from the South."
roomArray[406] = "There are no lights in this room. However, a dim light eluminates the floor from your West. A stronger light eluminates the floor from your East."
roomArray[506] = "The room is brightly lit. There are white walls blocking the North, East, and South."


def doesRoomExist(roomNumber):
    if roomArray[roomNumber] == False:
        print("You can't go there")
        return False
    else:
        return True
    try:
        roomNumber
    except:
        print("You can't go there")
        return False

def move(userInput, location):
    if userInput == "n" and doesRoomExist(location - 1) == True:
        location = location - 1
    elif userInput == "s" and doesRoomExist(location + 1) == True:
        location = location + 1
    elif userInput == "e" and doesRoomExist(location + 100) == True:
        location = location + 100
    elif userInput == "w" and doesRoomExist(location - 100) == True:
        location = location - 100

def main():
  location = 204
  print("Corrdior of Secrets")
  print("By Matthew, Brandon, Eric")
  time.sleep(1)
  while True:
    print(roomArray[location])
    print("Please type: N, S, E, W, or quit")
    userInput = input()
    location = move(userInput, location)
