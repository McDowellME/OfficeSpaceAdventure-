#!/usr/bin/python3

import random
def main():

  def showInstructions():
    #print a main menu and the commands
    print('''
  Welcome to Initech, Peter!
  ========
  Commands:
    go [direction]
    take [item]
    inspect [item]
  ''')

  def showStatus():
    #print the player's current status
    print("---------------------------")
    # print the current room
    print("You are in " + currentRoom)
    # print the current inventory
    print("Inventory : " + str(inventory))
    # print an item if there is one
    if "item" in office[currentRoom]:
      print("You see a " + office[currentRoom]["item"])
      # print the person if there is one and choose a random phrase
    if "person" in office[currentRoom]:
      print("You see " + office[currentRoom]["person"]["name"] + ": " + random.choice(office[currentRoom]["person"]["phrase"]))
    # print scenario statement or blank if there isn't one 
    print(statement)
    print("---------------------------")

  # an inventory, which is initially empty
  inventory = []
  # statement blank unless reassigned  
  statement = ""

  #a dictionary linking a room to other rooms with directions, items, and people
  office = {
              "Reception" : {
                  "directions" : {
                      "south" : "The Hall",
                      "east" : "The Printer Room",
                      "west" : "Chotckie's"
                  },
                  "person" : {
                    "name" : "Nina",
                    "phrase" : ['"Corporate Accounts Payable, Nina speaking.  JUST a moment!"', '"Sounds like somebody\'s got a case of the Mondays."']
                  }
              },
              "The Hall" : {
                  "directions" : {
                      "north" : "Reception",
                      "east" : "The Cubicles",
                  },
                  "item" : "memo"
              },
              "The Cubicles" : {
                  "directions" : {
                      "north" : "The Printer Room",
                      "east" : "The Conference Room",
                      "west" : "The Hall"
                  },
                  "item" : "tps report"
              },
              "The Conference Room" : {
                  "directions" : {
                      "north" : "An Office",
                      "west" : "The Cubicles"
                  },
                  "item" : "new attitude",
                  "person" : {
                    "name" : "The Bobs",
                    "phrase" : ['"If you would, would you walk us through a typical day, for you?."', '"Looks like you\'ve been missing quite a bit of work lately."', '"We uh, we fixed the glitch. So he won\'t be receiving a paycheck anymore, so it will work itself out naturally."', '"We find it\'s always better to fire people on a Friday."']
                  }
              },
              "An Office" : {
                  "directions" : {
                      "south" : "The Conference Room",
                      "west" : "The Printer Room"
                  },
                  "item" : "stapler",                
                  "person" : {
                    "name" : "Lumbergh",
                    "phrase" : ['"Oh, and remember: Next Friday is Hawaiin Shirt Day..."', '"That would be great. MmmmmK?"', '"Hey Peter. Whaaat\'s happening?"']
                  }
              },
              "The Printer Room" : {
                  "directions" : {
                      "north" : "The Basement",
                      "south" : "The Cubicles",
                      "east" : "An Office",
                      "west" : "Reception"
                  },
                  "item" : "printer",
                  "person" : {
                    "name" : "Samir Nagheenanajar and Michael Bolton",
                    "phrase" : ['"PC Load Letter? What the fudge does that mean?"', '"Yeah, well, at least your name isn\'t Michael Bolton"', "If we get caught, we're not going to white-collar resort prison."]
                  }
              },
              "The Basement" : {
                  "directions" : {
                      "south" : "The Printer Room",
                  },
                  "person" : {
                    "name" : "Milton",
                    "phrase" : ['"Have you seen my stapler?"', '"I could set the building on fire."', '"I was told I could listen to the radio at a reasonable volume, from 9 to 11."']
                  }
              },
              "A Field" : {
                "item" : "bat",
                "person" : {
                    "name" : "Samir Nagheenanajar and Michael Bolton",
                    "phrase" : ['"Let\'s do this!"']
                  }
              },
              "Chotckie's" : {
                  "directions" : {
                      "east" : "Reception",
                  },
                  "item" : "flair",
                  "person" : {
                    "name" : "Joanna",
                    "phrase" : ['"I love Kung Fu!"', '"This is me, expressing myself!"']
                  }
              }

          }

  # separate dictionary to be able to grab description for anything in inventory even if deleted from office dict
  items = {
    "flair" : 'A pin that says: "We\'re not in Kansas anymore!".',
    "printer" : "A piece of equipment that constantly fails.",
    "stapler" : "A red swingline stapler. Maybe it's Milton's. Wonder what will happen if I forget to give it to him.",
    "new attitude" : "You're honest about how much you hate your job, and you seem much happier because of it.",
    "tps report" : "A document you constantly submit.  Requires a cover sheet",
    "memo" : "A document reminding you to put a cover sheet on your tps report."
  }

  # start the player in the first room in the office (dictionary)
  currentRoom = list(office.keys())[0]
  # define final room
  finalRoom = list(office.keys())[-1]

  showInstructions()

  #loop forever
  while True:

    showStatus()

    # reset statement
    statement = ""

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ""
    while move == "":
      move = input(">")

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)
    # define each
    command = move[0]
    thing = move[1]

    # if they type 'go' first
    if command == "go":
      #check that they are allowed wherever they want to go
      if thing in office[currentRoom]["directions"]:
        #set the current room to the new room
        currentRoom = office[currentRoom]["directions"][thing]
      #there is no door (link) to the new room
      else:
          print("You can\'t go that way!")

    # if they type 'get' first
    if command == "take" :
      # if the room contains an item, and the item is the one they want to get
      if "item" in office[currentRoom] and thing in office[currentRoom]["item"]:
        # add the item to their inventory
        inventory += [thing]
        # display a helpful message
        print(thing + " taken!")
        # delete the item from the room
        del office[currentRoom]["item"]
      # otherwise, if the item isn't there to get
      else:
        #tell them they can't get it
        print("Can\'t take " + thing + "!")

    # if they type inspect first
    if command == "inspect" :
      # if the item is in room or in inventory
      if ("item" in office[currentRoom] and thing in office[currentRoom]["item"]) or thing in inventory:
        # get description from items dict
        print(thing + ": " + items[thing])
        # can't inspect it
      else :
        print("Can\'t inspect " + thing + "!")

    # if user inputs wrong command
    if command != "inspect" and command != "take" and command != "go":
      print(f"{command} is not a proper command. Try again")

    # get transported
    if "printer" in inventory:
      currentRoom = "A Field"
      statement = "\nTaking the printer has transported you to a field.  You're only way back is to destroy the printer."

    # get transported back
    if "printer" in inventory and "bat" in inventory:
      statement = "\nYou're back. \nYou've destroyed the printer in a cathartic, epic, slow-mo scene. \nIt feels good."
      # remove the printer from inventory since destroyed
      inventory.remove("printer")
      currentRoom = "The Printer Room"

    # how to beat the boss
    if "person" in office[currentRoom] and "Lumbergh" in office[currentRoom]["person"]["name"] and "tps report" in inventory and "memo" in inventory:
      statement ="\nSince you read the memo, you put a cover sheet on your tps report. \nLumbergh will not ask you to work this weekend."

    ## Define how a player can win
    if currentRoom == finalRoom and 'stapler' in inventory and 'new attitude' in inventory:    
      statement = "\nYou have a new attitude and got the girl. \nYou forgot to give Milton his stapler, and he has now burned down Initech. \nYou don't have to go to work there anymore! You win!"
      showStatus()
      break  
      
    ## If a player enters a room with a monster
    elif "person" in office[currentRoom] and "Lumbergh" in office[currentRoom]["person"]["name"] and "tps report" not in inventory and "memo" not in inventory:    
      statement = '"\nYeah. You see, we\'re putting the cover sheets on all the tps reports now before they go out. Did you see that memo?" \nYou have to work this weekend.  You lose.'
      showStatus()
      break
main()
