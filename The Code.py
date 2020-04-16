#----------------------------------------------------------------------------------------------------
#welcome to my text based dungeon crawler, ROGUE. The game will have you explore randomly generated dungeons and you must find the exit before you die. The loot, wnemies, and weapons are
#randomly generated, adding to a particular challenge. This game will run indefinitely, and the combat scenarios follow DND combat very closely.
#----------------------------------------------------------------------------------------------------

import math                                                                                        #imports math.
import random                                                                                      #imports random for RNG dungeon creation.
from random import randint

def showinventory():                                                                          #defines show inventory to display the inventory of the player
  k = 0
  print("")
  while(k<len(inventory)):
    print(inventory[k])
    k = k + 1
  print("")

def removeitem():                                                                              #removes an item from the player's inventory
  itemlocation.insert(0,location)                                                              #if the item is in the inventory then it is dropped where the player is standing.
  inventory.remove(answer2)
  locationanditem.insert(0,[location,answer2])

print("                   _                                       _           ")
print("                  | |                                     | |             _")
print("__      __   ___  | |   ___    ___    _ __ ___     ___    | |_    ___    (_)")
print("\ \ /\ / /  / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \   | __|  / _ \ ")
print(" \ V  V /  |  __/ | | | (__  | (_) | | | | | | | |  __/   | |_  | (_) |   _ ")
print("  \_/\_/    \___| |_|  \___|  \___/  |_| |_| |_|  \___|    \__|  \___/   (_)")
print("              _______  _______  _______           _______ ")
print("             (  ____ )(  ___  )(  ____ \|\     /|(  ____ \ ")    
print("             | (    )|| (   ) || (    \/| )   ( || (    \/")
print("             | (____)|| |   | || |      | |   | || (__    ")
print("             |     __)| |   | || | ____ | |   | ||  __)   ")
print("             | (\ (   | |   | || | \_  )| |   | || (      ")
print("             | ) \ \__| (___) || (___) || (___) || (____/\ ") 
print("             |/   \__/(_______)(_______)(_______)(_______/")

amuletcount = 0                                                                                    #sets the amulet count to 0 for the Amulet of Health.
ringcount = 0                                                                                      #sets the ring count to 0 for the ring of shields.
swordcount = 0                                                                                     #sets the sword count to 0 for the ring of shields.
daggercount = 0                                                                                    #sets the dagger count to 0 for the ring of shields.
shieldcount = 0                                                                                    #sets the shield count to 0 for the ring of shields.
shortswordcount = 0
j = 6
J = 20
inventory = []                                                                                     #creates a blank inventory.
x = 1                                                                                              #sets the X coordinate of the player to 1.
y = 1                                                                                              #sets the Y coordinate of the player to 1.
items = ["Potion of Healing","Potion of Majour Healing","Potion of Minour Healing","Dagger", "Shortsword", "Longsword", "Amulet of Minour Health", "Amulet of Majour Health", "Amulet of Health", "Ring of Minour Shields", "Ring of Majour Shields", "Ring of Shields", "Shield"]                   #this is every item in the game.
amulets = ["Amulet of Minour Health", "Amulet of Majour Health", "Amulet of Health"]               #these are the amulets
setamulets = set(amulets)                                                                          #makes sets so the intersect function works
rings = ["Ring of Minour Shields", "Ring of Majour Shields", "Ring of Shields"]                    #these are the rings
setrings = set(rings)
weapons = ["Dagger", "Shortsword", "Longsword"]                                                    #these are the weapons
setweapons = set(weapons)
enemies = ["Goblin", "Bandit" , "Skeleton"]                                                        #these are the enemies
potions = ["Potion of Healing","Potion of Majour Healing","Potion of Minour Healing"]              #these are the potions
setpotions = set(potions)
location = [x,y]                                                                                   #creates an ordered pair [x,y] of the players location.
maxhealth = 20                                                                                     #defines the base health stat.
health = 20                                                                                        #sets current health to 20
while(1==1):                                                                                       #infinite loop for the game.
  x = 1                                                                                            #sets the X coordinate of the player to 1.
  y = 1                                                                                            #sets the Y coordinate of the player to 1.                                                     
  itemlocation = []                                                                                #this is a list that will be used to combine X & Y coords into a list of ordered pairs [x,y].
  locationanditem = []                                                                             #this associates the location with the item in its place
  itemsleft = []                                                                                   #this is the list I will use to keep track of how many items are left using len().
  enemylocation = []                                                                               #X and Y coordinates of enemies
  locationandenemy = []                                                                            #associates the location with the enemy in that spot
  a = randint(3,10)                                                                                #this defines the X dimension of the dungeon room.
  b = randint(3,10)                                                                                #this defines the Y dimension of the dungeon room.
  c = randint(2,a)                                                                                 #the X coordinate of the exit.
  d = randint(2,b)                                                                                 #the Y coordninate of the exit.
  itemcount = math.ceil(0.05*a*b)                                                                  #the item frequency is 5% rounded up of the multiple of the X & Y area of the room.
  enemycount = math.floor(0.05*a*b)                                                                #sets the enemy frequency to 5% rounded down of the multiple of the X and Y area of the room
  k = 0
  while(k<itemcount):                                                                              #this creates the list of items left in the dungeon.
    itemsleft.insert(0,k)
    k = k + 1
  k = 0
  while(k<itemcount):                                                                              #this loop creates the list of ordered pairs previously mentioned.
    itemcoords = [randint(2,a),randint(2,b)]                                                       #this list is called "itemlocation".
    itemlocation.insert(0, itemcoords)
    k = k + 1
  k = 0
  while(k<enemycount):
    enemycoords = [randint(2,a),randint(2,b)]
    enemylocation.insert(0, enemycoords)
    k = k + 1
  k = 0
  while(k<len(itemlocation)):
    locationanditem.insert(len(locationanditem),[itemlocation[k],items[randint(0,len(items)-1)]])                     #this creates random loot per level.
    k = k + 1 
  k = 0                                                                
  while(k<len(enemylocation)):
    locationandenemy.insert(len(locationandenemy),[enemylocation[k],enemies[randint(0,len(enemies)-1)]])                #this creates random enemies per level.
    k = k + 1
   
  print("")
  print("You are in a", a, "x", b, "grid with",len(itemlocation), "items. Find the exit.")
  print("")
  print("type *help* for a list of commands")
  print("")
  print("Health:", health,"/",maxhealth)                                                                         #this displays the health of the player.
  print("Location:", location)                                                                     #this shows the [x,y] location of the player.
  print("") 
  z = 0                                                                                            #this sets the completion variable to zero so the while loop will function as intended.
  while(z != 1):
    setinventory = set(inventory)
    playerinitiative = 0
    enemyinitiative = 0
    g = 0                                                               
    k = 0                                                                                          #this sets k = 0 for loops later on in the code.
    answer = ("")                                                                                  #this clears the variable answer for use later.
    answer2 = ("")                                                                                 #this clears the variable answer2 for use later.
    answer = str(input(""))                                                                        #command line input.
    exitcount = 0                                                                                  #this is for when the player discovers the exit, but does not want to leave.

    if answer == "dev":                                                                            #this gives dev mode information for debugging
      print("levelsize = ", a,b)
      print("exitlocation = ", c,d)
      print("itemlocation =", itemlocation)
      print("locationanditem = ",locationanditem)
      print("enemylocation =", enemylocation)
      print("locationandenemy =", locationandenemy)

    elif answer == "help":                                                                           #only I have the commands memorized so a player may need to know what to do.
      print("You are in a", a, "x", b, "grid with",len(itemlocation), "items. Find the exit to delve deeper into the dungeon!")
      print("Enchanted items bind to your character and cannot be removed")
      print("*north* - to move north")
      print("*south* - to move south")
      print("*east* - to move east")
      print("*west* - to move west")
      print("*inventory* - view your inventory")
      print("*search* - you search the floor for any items")
      print("*drink potion* - you may drink a potion to regain your health")
      print("*exit* - closes the game")

    elif answer == "north" and y < b:                                                              #every if answer == "X" block is a command I have programmed into the game.
      y = y + 1                                                                                    #this changes the players Y position by 1.
      print("You move north")
      answer = ("")
      
    elif answer == "north" and y == b:                                                             #every block like this is in case a player comes up against a wall, they cannot walk thru it.
      print("You cannot go this way")

    elif answer == "south" and y > 1:
      y = y - 1                                                                                    #this changes the players Y position by -1.
      print("You move south")
      answer = ("")
  
    elif answer == "south" and y == 1:
      print("You cannot go this way")

    elif answer == "east" and x < a:
      x = x + 1                                                                                    #this changes the payers Y position by 1.
      print("You move east")
      answer = ("")
  
    elif answer == "east" and x == a:
      print("You cannot go this way")

    elif answer == "west" and x > 1:
      x = x - 1                                                                                    #this changes the payers Y position by -1.
      print("You move west")
      answer = ("")

    elif answer == "west" and x == 1:
      print("You cannot go this way")

    if answer == "inventory" and len(inventory) > 0:                                             #this recalls the players inventory and tells the player if their inventory is empty if it is.
      showinventory()

    elif answer == "inventory" and len(inventory) == 0:
      print("There is nothing in your inventory")
    
    if answer == "search" and location not in itemlocation and x != c and y != d:                #this is so if you want to grab something off the ground the player has just dropped.
      print("You examine the floor and find nothing of value ")
    
    if answer == "drink potion" and setinventory.intersection(setpotions):                       #This is for healing your character, by drinking potions of different magnitudes
      print("Potions:")
      while(k<len(inventory)):                                                                   #shows the potions in the player's inventory
        if inventory[k] in potions:
          print(inventory[k])
          k = k + 1
        else:
          k = k + 1
        print("")
      k = 0
      while(k < 1):
        answer2 = str(input("What potion would you like to drink? "))                             #asks which potion the player would like to drink
        if answer2 in inventory:
          k = k + 1
        else:
          k = k
      if answer2 == "Potion of Healing":
        prevhealth = health
        if health + 10 < maxhealth:
          health = health + 10
        else:
          health = maxhealth
        healthgain = maxhealth - prevhealth
        print("You drink the potion and gain",healthgain,"health")                                #by using the healthgain variable, I can show how much health the player gained from the potion
      if answer2 == "Potion of Minour Healing":
        prevhealth = health
        if health + 5 < maxhealth:
          health = health + 5
        else:
          health = maxhealth
        healthgain = maxhealth - prevhealth
        print("You drink the potion and gain",healthgain,"health")
      if answer2 == "Potion of Majour Healing":
        prevhealth = health
        if health + 15 < maxhealth:
          health = health + 15
        else:
          health = maxhealth
        healthgain = maxhealth - prevhealth
        print("You drink the potion and gain",healthgain,"health.")
      inventory.remove(answer2)
    elif answer == "drink potion":
      print("You do not have any potions.")                                                        #in case the player does not have any potions

    if x == c and y == d and exitcount == 0:                                                       #this is the condition for finishing the level.
      print("")
      print("You found the exit!")
      print("")
      g = 0
      while(g != 1):
        answer2 = str(input("Would you like to leave? "))
        if answer2 == "yes":                                                                       #if the player wants to exit the level, the next one will be randomly generated.
          print("")
          print("You climb deeper into the dungeon")
          z = z + 1
          x = 1                                                                                    #a bug occurred when the player found the exit and it would display they were spawned in
          y = 1                                                                                    #and it displayed their position in the new room as the position in the old room.
          g = g + 1
          
        if answer2 == "no":                                                                        #if the player wants to not exit the level and continue to loot, they may.
          exitcount = exitcount + 1
          print("")
          print("You ignore the ladder leading downward")
          g = g + 1

    location = [x,y]                                                                               #defines location[] as the players current position.
    if location in itemlocation:                                                                   #checks to see if the player is standing on a piece of loot.
      f = itemlocation.index(location)
      print("You've found",locationanditem[f][1])                                                  #tells the player what they've found.
      k = 0
      while(k == 0):
        answer2 = str(input("Would you like to pick it up? "))                                     #asks the player if they would like to pick up the item and add it to their inventory.
        if answer2 == "yes" and locationanditem[f][1] in inventory:
          print("")
          print("You may not carry more than one",locationanditem[f][1])
          k = k + 1
        elif answer2 == "yes" and setinventory.intersection(setamulets) and locationanditem[f][1] in amulets:
          print("")
          print("You may not carry more than one Amulet.")
          print("")
          k = k + 1
        elif answer2 == "yes" and setinventory.intersection(setrings) and locationanditem[f][1] in rings:
          print("")
          print("You may not carry more than one Ring.")
          print("")
          k = k + 1
        elif answer2 == "yes":                                                                         
          inventory.insert(0,locationanditem[f][1])                                                #adds the item to the player's inventory.
          itemlocation.remove(location)                                                            #removes the item from the "ground".
          locationanditem.remove(locationanditem[f])                                               #removes the item from the list that pairs items and coordinates.
          k = k + 1
        elif answer2 == "no":
          print("You leave",locationanditem[f][1],"on the ground.")                                #leaves the item that the player found on the ground and does not put it into their inventory.
          k = k + 1
        else:
          k = 0
    
    if answer == "drop item" and len(inventory) > 0:                                                                    #the player wants to drop an item from their inventory, this is where
      showinventory()                                                                                                     #"search" comes in handy.
      k = 0                                                                                         
      while(answer2 not in inventory):                                                             #once the player has declared to drop an item they cannot back out.
        answer2 = str(input("Which item would you like to drop? "))                                #asks the player which item they would like to drop.
        if answer2 in amulets and amuletcount > 0:                                                 #tbh, i was lazy and didnt wanna fix the majour health bug
          print("")                                                                                #that came with the amulet so I madeit irremoveable.
          print("The Amulet has bound itself to you and it is irremoveable.")
        elif answer2 in rings and ringcount > 0:                                                      #i was lazy, similar reason for the amulet
          print("")                                                                                #that came with the amulet so I madeit irremoveable.
          print("The Ring has bound itself to you and it is irremoveable.")
        elif answer2 == "Longsword" and location not in itemlocation:
          removeitem()
          swordcount = 0
          print("")    
          print("You lay the Longsword down at your feet.")
        elif answer2 == "Shortsword" and location not in itemlocation:                            #all of the items have their own dropped item text
          removeitem()
          shortswordcount = 0
          print("")    
          print("You lay the Shortsword down at your feet.")
        elif answer2 == "Shield" and location not in itemlocation:
          removeitem()
          shieldcount = 0
          print("")    
          print("You lay the Shield down at your feet.")
        elif answer2 == "Dagger" and location not in itemlocation:
          removeitem()
          daggercount = 0
          print("")    
          print("You lay the dagger down at your feet.")
        elif answer2 in potions and location not in itemlocation:
          removeitem()
          print("")    
          print("You lay the Potion down at your feet.")                                                                    
        else:                                                                                      #if the player types something that isnt in their inventory, the game tells them that its not.
          print("That's not in your inventory")
      k = k + 1
    elif answer == "drop item" and x == c and y == d:
      print("You may not drop that here.")
    elif answer == "drop item" and location in itemlocation:
      print("You may not drop that here.")
    elif answer == "drop item" and len(inventory) == 0:
      print("Your inventory is empty.")
  
    if "Amulet of Health" in inventory and amuletcount < 1:                                        #the amulet of health effect and acquisition notification.
      amuletcount = amuletcount + 1
      maxhealth = maxhealth + 10
      if health + 10 < maxhealth:
        health = health + 10
      else:
        health = maxhealth
      healthgain = maxhealth - health
      print("")
      print("As you feel it bind itself to you, the Amulet grants you a fortified constitution, and you gain",healthgain,"Health.")

    if "Amulet of Majour Health" in inventory and amuletcount < 1:                                        #the amulet of health effect and acquisition notification.
      amuletcount = amuletcount + 1
      maxhealth = maxhealth + 15
      if health + 15 < maxhealth:
        health = health + 15
      else:
        health = maxhealth
      healthgain = maxhealth - health
      print("")
      print("As you feel it bind itself to you, the Amulet grants you a fortified constitution, and you gain",healthgain,"Health.")

    if "Amulet of Minour Health" in inventory and amuletcount < 1:                                        #the amulet of health effect and acquisition notification.
      amuletcount = amuletcount + 1
      maxhealth = maxhealth + 5
      if health + 5 < maxhealth:
        health = health + 5
      else:
        health = maxhealth
      healthgain = maxhealth - health
      print("")
      print("As you feel it bind itself to you, the Amulet grants you a fortified constitution, and you gain",healthgain,"Health.")

    if "Ring of Shields" in inventory and ringcount < 1:                                           #the ring of shields effect and acquisition notification.
      ringcount = ringcount + 1
      j = j - 2
      print("")
      print("As you feel it bind itself to you, the Ring creates a glowing blue aura about you, granting minour resistance to attacks.")

    if "Ring of Minour Shields" in inventory and ringcount < 1:                                           #the ring of shields effect and acquisition notification.
      ringcount = ringcount + 1
      j = j - 1
      print("")
      print("As you feel it bind itself to you, the Ring creates a glowing blue aura about you, granting resistance to attacks.")

    if "Ring of Majour Shields" in inventory and ringcount < 1:                                           #the ring of shields effect and acquisition notification.
      ringcount = ringcount + 1
      j = j - 1
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
      J = J - 4
      print("")
      print("Big and heavy, the shield offers you greater protection against monsters.")
    
    if "Shortsword" in inventory and shortswordcount < 1:                                          #shortsword acquisition notification.
      shortswordcount = shortswordcount + 1
      print("")
      print("Quick and nimble, the shortsword's blade glimmers in the dim torchlight")

    if answer == "exit":      
      k = 0
      while(k == 0):
        answer2 = str(input("Are you sure? "))                                                    #in case the player doesnt want to leave
        if answer2 == "yes":
          exit()
          k = k + 1
        elif answer2 == "no":
          answer2 == ("")
          k = k + 1
        else:
          k = 0  
    print("")
    print("Health:", health,"/",maxhealth)                                                         #this displays the health of the player.
    print("Location:", [x,y])                                                                      #this shows the [x,y] location of the player.
    print("")

    location = [x,y]                                                                               #defines location[] as the players current position.
    if location in enemylocation:                                                                   #checks to see if the player found an enemy
      f = enemylocation.index(location)
      print("An enemy",locationandenemy[f][1],"stands in your path.")                              #tells the player what enemy they've found.
      if locationandenemy[f][1] == "Goblin":                                                       #this figures out which enemy the player found
        enemyhealth = 5
      elif locationandenemy[f][1] == "Skeleton":
        enemyhealth = 6
      elif locationandenemy[f][1] == "Bandit":
        enemyhealth = 8
      while(playerinitiative == enemyinitiative):                                                  #this is DND combat where both combatants roll 1d20 for initiative, seeing who attacks first
        playerinitiative = randint(1,j)
        enemyinitiative = randint(1,j)
      if playerinitiative > enemyinitiative:                                                       #checks if players initiative is higher than the enemy's and sees who attacks first
        print("Your initiative is higher than the enemy's.")
        while(enemyhealth > 0 and health > 0):                                                     #runs as long as the combatants are alive (health is more than zero)
          k = 0
          while(k<1):
            answer2 = str(input("Would you like to Attack or Run? "))                              #presents the player with options
            if answer2 == "Attack":
              k = k + 1
            elif answer2 == "Run":
              k = k + 1
          if answer2 == "Attack":
            k = 0
            print("")
            print("You may attack with:")                                                          #shows the weapons that the player has, a bug came early on where a player would have no
            print("Fists")                                                                         #weapons cuz they hadnt found any, I added the "Fists" to fix this issue
            while(k<len(inventory)):                                                               #shows the weapons
              if inventory[k] in weapons:
                print(inventory[k])
                k = k + 1
              else:
                k = k + 1
            k = 0
            while(k < 1):
              answer3 = str(input("What would you like to attack with? "))
              if answer3 == "Longsword" and "Longsword" in inventory:
                hitchance = randint(1,20)                                                                                #hit chance determines the chance of hitting the enemy, currently it
                if hitchance > 9:                                                                                        #is a 50% chance to hit hitchance > 9
                  damage = randint(1,8)
                  enemyhealth = enemyhealth - damage
                  print("You strike the",locationandenemy[f][1],"with the Longsword dealing",damage,"damage.")           #I used the damage variable to show how much damage was done to the enemy
                else:                                                                                                    #or to the player when the enemy attacks
                  print("You missed.")                                                                                   #the text displayed when the attack fails to hit
                k = k + 1 
              elif answer3 == "Longsword" and "Longsword" not in inventory:
                print("You do not have a Longsword")
              if answer3 == "Shortsword" and "Shortsword" in inventory:
                hitchance = randint(4,20)
                if hitchance > 9:
                  damage = randint(1,6)
                  enemyhealth = enemyhealth - damage
                  print("You strike the",locationandenemy[f][1],"with the Shortsword dealing",damage,"damage.")          #using locationandenemy[f][1] helped a butt ton in not worrying about
                else:                                                                                                    #scripting encounters
                  print("You missed.")
                k = k + 1
              elif answer3 == "Shortsword" and "Shortsword" not in inventory:
                print("You do not have a Shortsword")
              if answer3 == "Dagger" and "Dagger" in inventory:
                hitchance = randint(7,20)
                if hitchance > 9:
                  damage = randint(1,4)
                  enemyhealth = enemyhealth - damage
                  print("You strike the",locationandenemy[f][1],"with the Dagger dealing",damage,"damage.")
                else:
                  print("You missed.")
                k = k + 1
              elif answer3 == "Dagger" and "Dagger" not in inventory:
                print("You do not have a Dagger")
              if answer3 == "Fists":
                damage = 2
                enemyhealth = enemyhealth - damage
                print("You strike the",locationandenemy[f][1],"dealing",damage,"damage.")
                k = k + 1
              if answer3 not in inventory and answer3 != "Fists":                                         #doesnt let you attack with something not in your inventory
                print("That's not in your inventory.")
            hitchance = randint(1,J)                                                                      #variable J is for when the player has a shield which affects enemy hit chance
            if hitchance > 9 and enemyhealth > 0:
              damage = randint(2,j)                                                                       #variable j is for if the player has a ring of shields which affects enemy damage
              health = health - damage                                                                    #damage equation lets the player know how much damage was dealt
              print("The",locationandenemy[f][1],"strikes you, dealing",damage,"damage.")
            elif hitchance <= 9 and enemyhealth > 0:
              print("The",locationandenemy[f][1],"missed its attack.")                                    #if the enemy missed, the player knows
            print("")
            print("Health: ",health,"/",maxhealth)
            print(locationandenemy[f][1],"health: ",enemyhealth)
            print("")
          if answer2 == "Run" and playerinitiative - enemyinitiative >= 5:                                  #if your initiative is higher than the enemy's by 5, then you may flee from combat
            print("You have fled successfully")
            enemylocation.remove(location)                                                                  #randomly places the enemy
            locationandenemy.remove(locationandenemy[f][0])
            E = randint(2,a)
            F = randint(2,b)
            enemylocation.insert(F)
            locationandenemy.insert(locationandenemy[f][0],[E,F])
            if [E,F] == [x,y]:
              enemylocation.remove([E,F])
          elif answer2 == "Run" and playerinitiative - enemyinitiative <= 5:
            print("You may not flee from",locationandenemy[f][1])
        answer2 = ""
      if enemyhealth <= 0:                                                                                  #if the enemy died
          print("The enemy",locationandenemy[f][1],"has been slain.")
          enemylocation.remove(location)
          locationandenemy.remove(locationandenemy[f])
          print("")
          print("Health: ",health,"/",maxhealth)
          print("Location: ",location)
          print("")
      if health <= 0:                                                                                       #if you die, this is displayed
        print("You have been slain.")                                                                       
        k = 0
        while(k<1):
          answer2 = str(input("Would you like to try again? "))
          if answer2 == "yes":
            k = k + 1
            z = z + 1
          elif answer2 == "no":
            print("Game over")
            exit()
          else:
            k = k                                                                                         #--------------------------------------
      elif enemyinitiative > playerinitiative:                                                            #Literally just the same combat loop as before but the enemy 
        print("The enemy's initiative is higher than your's.")                                            #attacks first, no need to comment, imo
        while(enemyhealth > 0 and health > 0):                                                            #--------------------------------------
          hitchance = randint(1,20)
          if hitchance > 9 and enemyhealth > 0:
            damage = randint(2,j)
            health = health - damage
            print("The",locationandenemy[f][1],"strikes you, dealing",damage,"damage.")
          elif hitchance <= 9 and enemyhealth > 0:
            print("The",locationandenemy[f][1],"missed its attack.")
          print("")
          print("Health: ",health,"/",maxhealth)
          print(locationandenemy[f][1],"health: ",enemyhealth)
          print("")
          k = 0
          if health > 0:
            while(k<1):
              answer2 = str(input("Would you like to Attack or Run? "))
              if answer2 == "Attack":
                k = k + 1
              elif answer2 == "Run":
                k = k + 1
            if answer2 == "Attack":
              k = 0
              print("")
              print("You may attack with:")
              print("Fists")
              while(k<len(inventory)):
                if inventory[k] in weapons:
                  print(inventory[k])
                  k = k + 1
                else:
                  k = k + 1
              print("")
              k = 0
              while(k < 1):
                answer3 = str(input("What would you like to attack with? "))
                if answer3 == "Longsword" and "Longsword" in inventory:
                  hitchance = randint(1,20)
                  if hitchance > 9:
                    damage = randint(1,8)
                    enemyhealth = enemyhealth - damage
                    print("You strike the",locationandenemy[f][1],"with the Longsword dealing",damage,"damage.")
                  else:
                    print("You missed.")
                  k = k + 1
                elif answer3 == "Longsword" and "Longsword" not in inventory:
                  print("You do not have a Longsword")
                if answer3 == "Shortsword" and "Shortsword" in inventory:
                  hitchance = randint(4,20)
                  if hitchance > 9:
                    damage = randint(1,6)
                    enemyhealth = enemyhealth - damage
                    print("You strike the",locationandenemy[f][1],"with the Shortsword dealing",damage,"damage.")
                  else:
                    print("You missed.")
                  k = k + 1
                elif answer3 == "Shortsword" and "Shortsword" not in inventory:
                  print("You do not have a Shortsword")
                if answer3 == "Dagger" and "Dagger" in inventory:
                  hitchance = randint(7,20)
                  if hitchance > 9:
                    damage = randint(1,4)
                    enemyhealth = enemyhealth - damage
                    print("You strike the",locationandenemy[f][1],"with the Dagger dealing",damage,"damage.")
                  else:
                    print("You missed.")
                  k = k + 1
                if answer3 == "Fists":
                  damage = 2
                  enemyhealth = enemyhealth - damage
                  print("You strike the",locationandenemy[f][1],"dealing",damage,"damage.")
                  k = k + 1
                if answer3 not in inventory and answer3 != "Fists":
                  print("That's not in your inventory.")
            elif answer2 == "Run" and playerinitiative - enemyinitiative >= 5:
              print("You have fled successfully")
              enemylocation.remove(location)
              locationandenemy.remove(locationandenemy[f][0])
              E = randint(2,a)
              F = randint(2,b)
              enemylocation.insert(F)
              locationandenemy.insert(locationandenemy[f][0],[E,F])
              if [E,F] == [x,y]:
                enemylocation.remove([E,F])
            elif answer2 == "Run" and playerinitiative - enemyinitiative <= 5:
              print("You may not flee from",locationandenemy[f][1])
          answer2 = ""
        if health <= 0:
          print("You have been slain.")
          k = 0
          while(k<1):
            answer2 = str(input("Would you like to try again? "))
            if answer2 == "yes":
              k = k + 1
              z = z + 1
              inventory = []
              health = 20
              maxhealth = 20
            elif answer2 == "no":
              print("Game over")
              exit()
            else:
              k = k
        if enemyhealth <= 0:
          print("The enemy",locationandenemy[f][1],"has been slain.")
          enemylocation.remove(location)
          locationandenemy.remove(locationandenemy[f])
          print("")
          print("Health: ",health,"/",maxhealth)
          print("Location: ",location)
          print("")
