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

roomArray[502] = "You are in a room with a shiny gold coin, to the south of you see a red key."
roomArray[503] = "In the current room there is a gold coin to the north of you and a red key to your south."
roomArray[504] = "There is a red key in the room with you, an a gold coin in the room to your right, and one in the distance to the north of you."
roomArray[604] = " A gold coin is sitting in front of you in the small room."

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
