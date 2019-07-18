
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


        


