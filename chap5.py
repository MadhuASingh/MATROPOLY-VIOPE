# -*- coding: cp1252 -*-
#exercise 5.1
#The first exercise in the fifth chapther is a straightforward file reading exercise. There is a file in the same directory with the exercise source code 
#called "facts.txt", which has a long strip of text. Create a program which reads the entire content of the file and prints it on the screen with the text
# "Following was read from the file:". When working correctly, the program prints something like this:

sourcefile = open("facts.txt", "r")
read = sourcefile.readlines()

print(read) 

print("Following was read from the file: ")

for i in read :
    print(i)

sourcefile.close() 

#exercise 5.2
#Unsurprisingly, the second exercise in this chapter discusses the task of writing to a file.
#Create a program which prompts the user for a file name "Give a file name: " and then for an input "Write something: ". 
#After this, the program writes the string given by the user to the file and reports "Wrote [input] to the file [name].". 
#When working correctly, the program prints something like this:
fileName = input("Give a file name: ")

sourcefile =open(fileName, "w")

content = input("Write something: ")#
print(content)
sourcefile.write(content)

sourcefile.close() 

#exercise 5.3
#In the third program, we take a look into the classification of file contents. In the same directory with the source code is a file "strings.txt", 
#which has random strings in several lines. The lines can be divided into two groups: those which only have letters (a-z, A-Z) and numbers (0-9), and 
#those which also have random special characters (?,&,@, $ ...).
#Create a program which reads all of the lines from the file and tests the lines. If the line has only letters and/or numbers, the program prints "[line] was ok.". 
#If the line has special characters, the program should print "[line] was invalid.". When the program works, it prints out something like this:
sourceFile = open("strings.txt", "r")

content = sourceFile.readlines()

for i in content: 
    i = i[:-1]
    if i.isalnum() :
        print(i, "was ok.")
    else :
        print(i, "was invalid.")

sourceFile.close(); 

#exercise 5.4
#The last exercise in this chapter is the first part of the second multi-part assignment of this course, the notebook. 
#In this notebook the user is able to add, read and delete notes from a separate note file "notebook.txt". 
#Create a program which allows the user to 
#(1) Read the contents of the notebook
#(2) Add notes to the file or
#(3) Delete all of the notes. 
#If the user selects 1, the entire notebook file is printed to the screen, if 2 then the program prompts "Write a new note: ", and adds the written note as 
#the last line into the file with a trailing line break "\n". If the player selects 3, the file is emptied and the message "Notes deleted" will be shown. 
#Also add the option (4) Quit, which ends the program, printing "Notebook shutting down, thank you.". With other selections the program prompts "Incorrect selection". 
#When working, the program prints following: 

decision = True; 

while(decision) :
    print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n")
    
    select =input("Please select one: ")
    
    if(select == "1") :
        source = open("notebook.txt", "r")
        content = source.readlines()
        
        for i in content :
            print(i)     
        source.close()
    elif(select == "2") :
     note = input("Write a new note: ")   
     #note = note + "\n"
     source = open("notebook.txt", "a")
     source.write(note)
     source.close()
    elif(select =="3") :
     source = open("notebook.txt", "w")
     print("Notes deleted.")
     source.write(" ")
     source.close()
    elif(select == "4") :
     print("Notebook shutting down, thank you.")
     decision = False;  


    
    


