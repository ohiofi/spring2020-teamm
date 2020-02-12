import time
import random
from map import *

roomArray = []
itemArray = []
inventoryArray = []

for i in range(999):
  roomArray.append(False)
  itemArray.append(False)

roomArray[204] = "There is a long hallway to the East. The word START is written all over the walls in pen."
roomArray[304] = "There is a red door directly North and a hallway to the East"
roomArray[404] = "You are in the middle of the hallway with rooms to the East and West. There is a long hallway to the South." 
roomArray[502] = "You reached the end of this hallway. There are paintings on the walls."
roomArray[503] = "You are in the middle of this hallway with rooms to the North and South."
roomArray[504] = "There is a hallway to the North. The hallway you are in continues East."
roomArray[604] = "You reached a dead end. There are spikes on the ceiling."
roomArray[405] = "There are walls to your East and West. There is a faint light coming from the South."
roomArray[406] = "There are no lights in this room. However, there is a blue door to the West. A stronger light eluminates the floor from your East."
roomArray[506] = "The room is brightly lit. There are white walls blocking the North, East, and South." 
roomArray[407] = "There is a brown rug on the floor. The hallway continues South."
roomArray[408] = "The hallway continues South and has a branch leading West."
roomArray[409] = "The hallway reached it's end, but a hallway to the East is brightly lit"
roomArray[509] = "There is a bright light above you. The hallway gets darker toward the East."
roomArray[609] = "There is a small room to the North blocked by a green door."
roomArray[308] = "The long hallway is to the East. There are flashing stobe lights to the West."
roomArray[208] = "There is a room to the North. The strobe lights are very bright."
roomArray[207] = "There is a large mirror in the room. You see the strobe lights in the mirror."
itemArray[303] = "Blue Key"
itemArray[504] = "Red Key"
itemArray[306] = "Green Key"
itemArray[502] = "Coin"
itemArray[604] = "Coin"
itemArray[506] = "Coin"

def doesRoomExist(roomNumber):
  try:
    if roomArray[roomNumber] == False:
      print("You can't go there")
      return False
    else:
      return True   
  except:
    print("You can't go there")
    return False
      
def doesItemExist(roomNumber):
  try:
    if not itemArray[roomNumber] == False:
      print("Item: " + itemArray[roomNumber])
  except:
      return

def move(userInput, location):
    if userInput == "n" and doesRoomExist(location - 1) == True:
        location = location - 1
    elif userInput == "s" and doesRoomExist(location + 1) == True:
        location = location + 1
    elif userInput == "e" and doesRoomExist(location + 100) == True:
        location = location + 100
    elif userInput == "w" and doesRoomExist(location - 100) == True:
        location = location - 100
    return location
  
def randomSecretWord():
  list1 = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "brown", "black", "grey"]
  list2 = ["apple", "banana", "pear", "tomato", "grape", "watermelon", "cherry", "grapefruit", "pineapple", "mango"]
  list3 = ["america", "canada", "mexico", "brazil", "england", "egypt", "germany", "russia", "china", "japan"]
  combinedList = list1 + list2 + list3
  return random.choice(combinedList)

def matthewMain():
  randomWord = randomSecretWord()
  randomWord = randomWord.lower()
  print("There are words witten all over the wall: " "red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "brown", "black", "grey", "apple", "banana", "pear", "tomato", "grape", "watermelon", "cherry", "grapefruit", "pineapple", "mango", "america", "canada", "mexico", "brazil", "england", "egypt", "germany", "russia", "china", "japan")
  print("Take a guess on one of the words and I'll tell you if the secret word is before your word or after your word. Find the correct word to proceed.")
  while True:
    print("Guess a word")
    userInput = input()
    userInput = userInput.lower()
    if userInput < randomWord:
      print("The secret word is after " + str(userInput))
    if userInput > randomWord:
      print("The secret word is before " + str(userInput))
    if userInput == randomWord:
      print("You got it! You may now continue.")
      break
      
def lockCombo():
    return randint(0,12)

def validGuess(num):
    if int(num) >= 0 and int(num) <= 12:
        return True
    else:
        print("This number is not on the lock.")
        return False

def guessLock1():
    first = lockCombo()
    print("The lock should only need three numbers. Try guessing one number at a time from 0-12")
    while True:
        guess = input()
        if validGuess(guess) == True:
            if int(guess) == first:
                print("You got the first number!")
                break
            else:
                print("Try another number, 0-12:")

def guessLock2():
    second = lockCombo()
    print("Now try the second number.")
    while True:
        guess = input()
        if validGuess(guess) == True:
            if int(guess) == second:
                print("You got the second number!")
                break
            else:
                print("Wrong Number! You reset the lock...")
                time.sleep(1)
                print("and reenter the first number...")
                time.sleep(1)
                print("Try the second number again:")

def guessLock3():
    third = lockCombo()
    print("Now try the third number.")
    while True:
        guess = input()
        if validGuess(guess) == True:
            if int(guess) == third:
                print("You got the third number!")
                break
            else:
                print("Wrong Number! You reset the lock...")
                time.sleep(1)
                print("and reenter the first number and second number...")
                time.sleep(1)
                print("Try the third number again:")

def mainLock():
  guessLock1()
  guessLock2()
  guessLock3()
  print("You've cracked the lock! You may now continue.")
  
def pickItemUp(itemArray,location):
  inventoryArray.append(itemArray[location])
  print("You have picked up " + itemArray[location])
  itemArray[location] = False

def main():
  map = Map()
  matthew = 0
  brandon = 0
  location = 204
  print("   ____                _     _                     __   ____                     _        ")
  print("  / ___|___  _ __ _ __(_) __| | ___  _ __    ___  / _| / ___|  ___  ___ _ __ ___| |_ ___  ")
  print(" | |   / _ \| '__| '__| |/ _` |/ _ \| '__|  / _ \| |_  \___ \ / _ \/ __| '__/ _ \ __/ __| ")
  print(" | |__| (_) | |  | |  | | (_| | (_) | |    | (_) |  _|  ___) |  __/ (__| | |  __/ |_\__ \ ")
  print("  \____\___/|_|  |_|  |_|\__,_|\___/|_|     \___/|_|   |____/ \___|\___|_|  \___|\__|___/ ")
  print("                                                                                          ")
  print("By Matthew, Brandon, Eric")
  time.sleep(1)
  while True:
    map.draw(roomArray, itemArray, location)
    print(roomArray[location])
    print("Inventory: " + str(inventoryArray))
    doesItemExist(location)
    print("Please type: N (up), S (down), E (right), W (left), Q (quit), T (take item)")
    userInput = input()
    location = move(userInput, location)
    if userInput == "Q" or userInput == "q":
      print("Game Over")
      break
    if location == 405 and matthew == 0:
      matthewMain()
      matthew += 1
    if location == 405 and matthew == 1:
      print("You have already completed the secret word puzzle.")
    if location == 207 and brandon == 0:
      mainLock()
      brandon += 1
    if location == 207 and brandon == 1:
      print("You have already unlocked the safe.")
    if not itemArray[location] == False and userInput == "T" or userInput == "t":
      pickItemUp(itemArray, location)
    if "Red Key" in inventoryArray:
      roomArray[303] = "The red door was opened. The walls in this room are painted red. The only way out is the way you came in."
    if "Blue Key" in inventoryArray:
      roomArray[306] = "The room has black and white striped wallpaper. There is one dim light hanging from the ceiling. There are no other exits besides the one you entered through, from the East."
    if "Green Key" in inventoryArray:
      roomArray[608] = True
    if location == 608:
      print("You have escaped the corridor. You win!")
      break
