 # -*- coding: cp1252 -*-
#exercise 9.1
#The exercise in the 9th chapter focuses on one of the most powerful tools in the Python language, the datatype list,
# and the first assignment is a simple exercise to create. Define a list which has four items, strings "Blue","Red","Yellow" and "Green". 
# After this, make a slice from the list which contains only the first item of the list (list place 0), and print out all of the items with one for-structure. 
# When the code works properly, the program prints the following:
mylist = ["Blue", "Red", "Yellow", "Green"]
firstElement = mylist[0]
print("The first item in the list is:", firstElement)
print("The entire list printed one item a time:")

for i in mylist :
    print(i); 

#exercise 9.2
#In the second exercise the idea is to create a small grocery shopping list with the list datastructure. In short, create a program that allows the user to
# (1) add products to the list, (2) remove items and (3) print the list and quit. 
#If the user adds something to the list, the program asks "What will be added?: " and saves it as the last item in the list. 
#If the user decides to remove something, the program informs the user about how many items there are on the list (There are [number] items in the list.") 
#and prompts the user for the removed item ("Which item is deleted?: "). If the user selects 0, the first item is removed. When the user quits, the final list is
# printed for the user "The following items remain in the list:" followed by the remaining items one per line. If the user selects anything outside the options, 
# including when deleting items, the program responds "Incorrect selection.". When the program works correctly it prints out the following: 
groceryList = []
decision = True

while(decision) :
    print("Would you like to")
    good = input("(1)Add or\n(2) Remove items or\n(3)Quit?:")
    if(good == "1") :
        goods = input("What will be added?: ")
        groceryList.append(goods)
    elif(good == "2") :
        itemNumber = len(groceryList)
        print("There are " + str(itemNumber) + " items in the list.")
        delection = input("Which item is deleted?: ")
        try:
            groceryList.pop(int(delection))
        except Exception :
            print("Incorrect selection.")
    elif(good == "3") :
        decision = False
        print("The following items remain in the list:")
        for i in groceryList :
            print(i)
    else :
        print("Incorrect selection.")

#exercise 9.3
#The third exercise also revolves around list methods, this time doing data manipulation. In the same folder as the source code, 
#there is a file named "words.txt", which has a randomly selected set of words. Build a program, which reads all of the words from the file, 
#sorts them in alphabetic order and prints out the list with the statement "Words in an alphabetical order:". When correctly implemented, the program prints out the following:
fileName = "words.txt"
wordList =[]
finalList =[]

try:
    source =open(fileName, "r")
except Exception :
    print("File not found here")

else:
    wordList = source.readlines() 
    
    for i in wordList :
        i = i[:-1]  
        finalList.append(i)

    finalList.sort()
    print("Words in an alphabetical order:")
    for i in finalList :
        print(i)

#exercise 9.4
#As this is the last exercise for procedural programming, this exercise is also a sort of final project, which implements all of the things 
#discussed during the course. Also, even this if this exercise is marked as an exercise for the continuing notebook program, the changes made 
#in the program will be rather excessive, so it may be a good idea to start from a clean plate. 

#In this exercise the idea is to build a notebook which applies the Python data structure list as a note manipulation method when the program is executed, 
#and saves the data in a bitwise mode with pickle. The program has the following features:
#A) It is possible to add notes, with similar timestamps as earlier. 
#B)It is possible to edit a note by selecting it from the list, and rewriting it with new data.
#C) It is possible to delete notes separately based on the selection and 
#D) Notebook loads an existing notebook file from the file "notebook.dat" if such a file exists. 

#When the program starts, the system should check for a notebook datafile "notebook.dat" and load it with pickle. 
#If no such file exists, or there was a problem with the file, a new file is created and the user is notified 
#"No default notebook was found, created one.". After this the basic main menu works as in the earlier notebook:


#in this exercise I write the diary 

import pickle #import pickle
import time  #import time

fileName = "notebook.dat"
notebook = []
try:
    fileHandle = open(fileName, "rb") #try if the file already exist
    notebook = pickle.load(fileHandle)
except Exception :
    print("No default notebook was found, created one.")
    fileHandle = open(fileName, "wb")
    #pickle.load(fileHandle)

decision = True #preparing the while loop for the menu 

while(decision) :
    print("(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit")
    selection = input("Please select one: ")
    
    if(selection == "1") : #the selection start here
        for i in notebook :
            print(i)
    elif(selection == "2") :
        newNote = input("Write a new note: ")
        newNote = newNote +  ":::" + time.strftime("%Xn %x") # add data
        notebook.append(newNote)  #append the data
        pickle.dump(notebook, fileHandle) #write to pickle
    elif(selection == "3") :
        qty = len(notebook) #how many notes
        print("The list has " + str(qty) + " notes.")
        change = input("Which of them will be changed?: ") #element selection
        try:
            change = int(change)
            print(notebook[change]) #try to get the element 
        except Exception :
            print("Element do not exist")

        else : #here if no exception 
            newNote = input("Give the new note: ")
            newNote = newNote + ":::" + time.strftime("%Xn %x") # add date 
            notebook.pop(change)  #delete the old note
            notebook.insert(change, newNote) #put the new one instead 
            fileHandle =open(fileName, "wb")
            pickle.dump(notebook, fileHandle)

    elif(selection == "4") :
        qty = len(notebook) #how many element
        print("The list has " + str(qty) + " notes.") #list content
        deleted = input("Which of them will be deleted?: ") 
        try:
            #if deleted == "1" and len(notebook) == 1 : #this is done to fix the bug inside viope second attemp (thank bro!)
             #  deleted = 0 
            print("Deleted note " +notebook[int(deleted)])
            notebook.pop(int(deleted))
            fileHandle =open(fileName, "wb")
            pickle.dump(notebook, fileHandle)
          
        except Exception: 
            print("Element do not exist") 

    elif(selection == "5") :
            fileHandle =open(fileName, "wb")
            pickle.dump(notebook, fileHandle)
            print("Notebook shutting down, thank you.")
            decision= False 
    else : 
            print("Wrong choice")






        

