#Phonebook
import os, pickle

def mainMenu():

    os.system('clear')
    print "Electronic Phone Book"
    print "=" * 21
    print "1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit"

    inp = raw_input("What do you want to do? (1-5): ")

    if inp == "1":
        lookup()
    elif inp == "2":
        sentry()
    elif inp == "3":
        dentry()
    elif inp == "4":
        lentry()
    elif inp == "5":
        quit()
    else:
        raw_input("Invalid input. Press enter")
        mainMenu()

def lookup():
    os.system('clear')
    print "Electronic Phone Book"
    print "Entry lookup"
    print "=" * 21

    name = raw_input("What name would you like to look up?")
    if db.get(name) == None:
        print (raw_input("Name does not exist, press enter to continue"))
        mainMenu()
    else:
        print db[name]
        raw_input("Press enter to continue.")
        mainMenu()

def sentry():
    os.system('clear')
    print "Electronic Phone Book"
    print "Set an Entry"
    print "=" * 21

    name = raw_input("What name would you like to add?: ")
    if db.get(name) != None:
        raw_input("Name already exists, press enter to continue")
        mainMenu()
    else:
        number = raw_input("Please enter the number: ")
        db[name] = number
        raw_input("Name and number entered. Press enter to continue")
        mainMenu()

def dentry():
    os.system('clear')
    print "Electronic Phone Book"
    print "Delete an Entry"
    print "=" * 21

    name = raw_input("What entry would you like to delete?: ")
    if db.get(name) == None:
        raw_input("Name does not exist! Press enter to continue")
        mainMenu()
    else:
        del db[name]
        raw_input(" Deleted. Press enter to continue ")
        mainMenu()

def lentry():
    os.system('clear')
    print "Electronic Phone Book"
    print "List all entries"
    print "=" * 21


    print db
    raw_input("Press enter to continue:  ")
    mainMenu()

def quit():
    t = raw_input("Are you sure? (y/n)")
    if  t != "y":
        mainMenu()




if os.path.exists("pb.pickle"):
    with open("pb.pickle") as f1:
        db = pickle.load(f1)
else:
    db = {}
mainMenu()
with open("pb.pickle", 'w') as f1:
    pickle.dump(db, f1)
