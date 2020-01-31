import time

roomArray = []

for i in range(999):
  roomArray.append(False)

roomArray[204] = "There is a long hallway to the East. There are marks on the walls that look like the letter S."
roomArray[304] = "There is a red door directly North. There is a red object in the distance toward the East."
roomArray[404] = "There is a red key on the floor. There is another room to the East and a hallway to the North."
roomArray[303] = "The red door was opened. The walls in this room are painted red. There is a blue key in the room."

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
