import time

roomArray = []
itemArray = ["Red Key", "Blue Key", "Green Key", "Coin", "Coin", "Coin"]

for i in range(999):
  roomArray.append(False)
  itemArray.append(False)

roomArray[204] = "There is a long hallway to the East. There are marks on the walls that look like the letter S."
roomArray[304] = "There is a red door directly North. There is a red object in the distance toward the East."
roomArray[404] = "There is a red key on the floor. There is another room to the East and a hallway to the North."
roomArray[303] = "The red door was opened. The walls in this room are painted red. There is a blue key in the room."
roomArray[502] = "You are in a room with a shiny gold coin, to the south of you see a red key."
roomArray[503] = "In the current room there is a gold coin to the north of you and a red key to your south."
roomArray[504] = "There is a red key in the room with you, an a gold coin in the room to your right, and one in the distance to the north of you."
roomArray[604] = " A gold coin is sitting in front of you in the small room."

roomArray[306] = "The room has black and white striped wallpaper. There is one dim light hanging from the ceiling. Towards the left corner you notice a small green key. There are no other exits besides the one you entered through, from the east."
roomArray[405] = "There are walls to your East and West. There is a faint light coming from the South."
roomArray[406] = "There are no lights in this room. However, a dim light eluminates the floor from your West. A stronger light eluminates the floor from your East."
roomArray[506] = "The room is brightly lit. There are white walls blocking the North, East, and South. A small gold coin sits on the floor next to a broken table."

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
  location = roomArray[204]
  print("Corrdior of Secrets")
  print("By Matthew, Brandon, Eric")
  time.sleep(1)
  while True:
    print(roomArray["location"])
    print("Please type: N, S, E, W, or quit")
    userInput = input()
    location = move(userInput, location)
