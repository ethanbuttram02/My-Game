import math                                                                                        #imports math.
import random                                                                                      #imports random for RNG dungeon creation.
from random import randint          
amuletcount = 0                                                                                    #sets the amulet count to 0 for the Amulet of Health.
ringcount = 0                                                                                      #sets the ring count to 0 for the ring of shields.
swordcount = 0                                                                                     #sets the sword count to 0 for the ring of shields.
daggercount = 0                                                                                    #sets the dagger count to 0 for the ring of shields.
shieldcount = 0                                                                                    #sets the shield count to 0 for the ring of shields.
inventory = []                                                                                     #creates a blank inventory.
x = 1                                                                                              #sets the X coordinate of the player to 1.
y = 1                                                                                              #sets the Y coordinate of the player to 1.
items = ["Longsword", "Amulet of Health", "Ring of Shields", "Shield", "Dagger"]                   #this is every item in the game.
location = [x,y]                                                                                   #creates an ordered pair [x,y] of the players location.
health = 10                                                                                        #defines the base health stat.
while(1==1):                                                                                       #infinite loop for the game.
  x = 1                                                                                            #sets the X coordinate of the player to 1.
  y = 1                                                                                            #sets the Y coordinate of the player to 1.
  itemlocationX = []                                                                               #creates a list of X coordinates of items in the dungeon.
  itemlocationY = []                                                                               #creates a list of Y coordinates of items in the dungeon.
  itemlocation = []                                                                                #this is a list that will be used to combine X & Y coords into a list of ordered pairs [x,y].
  itemsleft = []                                                                                   #this is the list I will use to keep track of how many items are left using len().
  a = randint(3,10)                                                                                #this defines the X dimension of the dungeon room.
  b = randint(3,10)                                                                                #this defines the Y dimension of the dungeon room.
  c = randint(2,a)                                                                                 #the X coord of the exit.
  d = randint(2,b)                                                                                 #the Y coord of the exit.
  itemcount = math.floor(0.1*a*b)                                                                  #the item count/frequency is 10% rouded down of the multiple of the X & Y area of the room.
  while len(itemlocationX) < itemcount or len(itemlocationY) < itemcount:                          #this loop makes sure each item has a unique location ID and that items don't spawn in the exit
    e = randint(2,a)                                                                               #this makes random X & Y coords for each item.
    f = randint(2,b)
    itemlocationX.insert(0,e)
    itemlocationY.insert(0,f)
    e = randint(2,a)
    f = randint(2,b)
    if e in itemlocationX:                                                                         #removing duplicates for unique [x,y] locations.
      itemlocationX.remove(e)
    if f in itemlocationY:
      itemlocationY.remove(f)  
    if e == c and e in itemlocationX:                                                              #in case the item spawns on the exit, this removes it.
      itemlocationX.remove(e)
    if f == d and f in itemlocationY:
      itemlocationY.remove(f)
  k = 0
  while(k<itemcount):                                                                              #this creates the list of items left in the dungeon.
    itemsleft.insert(0,k)
    k = k + 1
  k = 0
  while(k<itemcount):                                                                              #this loop creates the list of ordered pairs previously mentioned.
    itemcoords = [itemlocationX[k],itemlocationY[k]]                                               #this list is called "itemlocation".
    itemlocation.insert(0, itemcoords)
    k = k + 1
  f1 = randint(0,len(items) - 1)                                                                   #this creates random loot per level.

  print("You are in a", a, "x", b, "grid with",len(itemlocation), "items. Find the exit to delve deeper into the dungeon!")
  print("type *help* for a list of commands")
  z = 0                                                                                            #this sets the completion variable to zero so the while loop will function as intended.
  while(z != 1):
    print("")
    print("Health:", health)                                                                       #this displays the health of the player.
    print("Location:", location)                                                                   #this shows the [x,y] location of the player.
    print("")                                                                  
    k = 0                                                                                          #this sets k = 0 for loops later on in the code.
    answer = ("")                                                                                  #this clears the variable answer for use later.
    answer2 = ("")                                                                                 #this clears the variable answer2 for use later.
    answer = str(input(""))                                                                        #command line input.
    exitcount = 0                                                                                  #this is for when the player discovers the exit, but does not want to leave.

    if answer == "devmode86-Character":                                                            #this gives dev mode information for debugging
      print("levelsize = ", a,b)
      print("exitlocation = ", c,d)
      print("itemlocations = ",itemlocation)
      
    if answer == "help":                                                                           #only I have the commands memorized so a player may need to know what to do.
      print("You are in a", a, "x", b, "grid with",len(itemlocation), "items. Find the exit to delve deeper into the dungeon!")
      print("Enchanted items bind to your character and cannot be removed")
      print("*north* - to move north")
      print("*south* - to move south")
      print("*east* - to move east")
      print("*west* - to move west")
      print("*inventory* - view your inventory")
      print("*search* - you search your feet for any items")
      print("*exit* - closes the game")

    if answer == "north" and y < b:                                                                #every if answer == "X" block is a command I have programmed into the game.
      y = y + 1                                                                                    #this changes the players Y position by 1.
      print("You move north")
      answer = ("")
      
    if answer == "north" and y == b:                                                               #every block like this is in case a player comes up against a wall, they cannot walk thru it.
      print("You cannot go this way")

    if answer == "south" and y > 1:
      y = y - 1                                                                                    #this changes the players Y position by -1.
      print("You move south")
      answer = ("")
  
    if answer == "south" and y == 1:
      print("You cannot go this way")

    if answer == "east" and x < a:
      x = x + 1                                                                                    #this changes the payers Y position by 1.
      print("You move east")
      answer = ("")
  
    if answer == "east" and x == a:
      print("You cannot go this way")

    if answer == "west" and x > 1:
      x = x - 1                                                                                    #this changes the payers Y position by -1.
      print("You move west")
      answer = ("")

    if answer == "west" and x == 1:
      print("You cannot go this way")

    if answer == "inventory" and len(inventory) > 0:                                               #this recalls the players inventory and tells the player if their inventory is empty if it is.
      k = 0
      print("")
      while(k<len(inventory)):
        print(inventory[k])
        k = k + 1
      print("")

    if answer == "inventory" and len(inventory) == 0:
      print("There is nothing in your inventory")
    
    if answer == "search" and location not in itemlocation:                                        #this is so if you want to grab something off the ground the player has just dropped.
      print("You examine the floor and find nothing of value ")

    if x == c and y == d and exitcount == 0:                                                       #this is the condition for finishing the level.
      print("You found the exit!")
      answer2 = str(input("Would you like to leave? "))
      
      if answer2 == "yes":                                                                         #if the player wants to exit the level, the next one will be randomly generated.
        print("")
        print("You climb deeper into the dungeon")
        z = z + 1
        
      if answer2 == "no":                                                                          #if the player wants to not exit the level and continue to loot, they may.
        exitcount = exitcount + 1
        print("")
        print("You ignore the ladder leading downward")

    location = [x,y]                                                                               #defines location[] as the players current position.
    if location in itemlocation:                                                                   #checks to see if the player is standing on a piece of loot.
      print("You've found",items[f1])                                                              #tells the player what they've found.
      answer2 = str(input("Would you like to pick it up? "))                                       #asks the player if they would like to pick up the item and add it to their inventory.
      if answer2 == "yes" and items[f1] in inventory:
        print("You may not carry more than one",items[f1])
      elif answer2 == "yes":                                                                         
        inventory.insert(0,items[f1])                                                              #adds the item to the player's inventory.
        itemlocation.remove([x,y])                                                                 #removes the item from the "ground".
        f1 = randint(0,len(items) - 1)                                                             #creates a new item for loot under the var f1.
      if answer2 == "no":
        print("You leave",items[f1],"on the ground.")                                              #leaves the item that the player found on the ground and does not put it into their inventory.
    
    if answer == "drop item":                                                                      #the player wants to drop an item from their inventory, this is where "search" comes in handy.
      k = 0                                                                                        #k = 0 for the loop.
      print("")
      while(k<len(inventory)):                                                                     #displays the inventory of the player in case they forgot what they had.
        print(inventory[k])
        k = k + 1
      print("")
      k = 0                                                                                         
      while(answer2 not in inventory):                                                             #once the player has declared to drop an item they cannot back out.
        answer2 = str(input("Which item would you like to drop? "))                                #asks the player which item they would like to drop.
        if answer2 == "Amulet of Health":                                                          #tbh, i was lazy and didnt wanna fix the majour health bug
          print("")                                                                                #that came with the amulet so I madeit irremoveable.
          print("The Amulet has bound itself to you and it is irremoveable.")
        if answer2 == "Ring of Shields":                                                           #tbh, i was lazy, similar reason for the amulet
          print("")                                                                                #that came with the amulet so I madeit irremoveable.
          print("The Ring has bound itself to you and it is irremoveable.")
        if answer2 == "Longsword":
          swordcount = 0
          print("")    
          print("You lay the Longsword down at your feet.")
        if answer2 == "Shield":
          shieldcount = 0
          print("")    
          print("You lay the Shield down at your feet.")
        if answer2 == "Dagger":
          daggercount = 0
          print("")    
          print("You lay the dagger down at your feet.")
        elif answer2 in inventory:                                                                 #if the item is in the inventory then it is dropped where the player is standing.
          itemlocation.insert(0,[x,y])
          k = k + 1
        else:                                                                                      #if the player types something that isnt in their inventory, the game tells them that its not.
          print("That's not in your inventory")
          k = k + 1
      inventory.remove(answer2)
    
    if "Amulet of Health" in inventory and amuletcount < 1:                                        #the amulet of health effect and acquisition notification.
      amuletcount = amuletcount + 1
      health = health + 10
      print("")
      print("As you feel it bind itself to you, the Amulet grants you a fortified constitution, and you gain 10 Health.")

    if "Ring of Shields" in inventory and ringcount < 1:                                           #the ring of shields effect and acquisition notification.
      ringcount = ringcount + 1
      print("")
      print("As you feel it bind itself to you, the Ring creates a glowing blue aura about you, granting greater resistance to attacks.")
    
    if "Longsword" in inventory and swordcount < 1:                                                #the longsword effect and acquisition notification.
      swordcount = swordcount + 1
      print("")
      print("Quite hefty, the sword's blade glimmers in the dim torchlight.")
    
    if "Dagger" in inventory and daggercount < 1:                                                  #The dagger acquisition notification.
      daggercount = daggercount + 1
      print("")
      print("Light and swift in your hand, the dagger's blade glimmers in the dim torchlight.")
    
    if "Shield" in inventory and shieldcount < 1:                                                  #the shield acquisition notification.
      shieldcount = shieldcount + 1
      print("")
      print("Big and heavy, the shield offers you greater protection against monsters.")
    
    if answer == "exit":
      answer2 = str(input("Are you sure? "))
      if answer2 == "yes":
        exit()
      if answer2 == "no":
        answer2 == ("")
