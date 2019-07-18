# -*- coding: cp1252 -*-

#exercise 8.1
#The first exercise in this chapter discusses the most common problem with programs in Python: 
#getting a numeric value as input without a problem or constant fear of TypeError. Simply put, create a program, 
#which asks the user for input and tries to convert it to an integer value. If the conversion happens without problems, 
#the program prints "The input was suitable!". If the user gives something which does not convert, like letters or special characters,
# the program avoids the error with an exception handler and prints "The input was malformed.". When working correctly, the program prints out the following:
number = input("Give a number: ")

try :
    number = int(number)
    print("The input was suitable")
    
except Exception :
    print("The input was malformed.")
    
#exercise 8.2
#The second exercise combines several normal error scenarios into one program. In this exercise, create a program which prompts the user for a file name. 
#Based on user input, open the given file and read the contents into one big string. Then convert this string to an integer and divides the number 1000 with the number. 
#Finally, print out the result from the division.
#The idea here is that no matter what the user input is, the program works. If the file cannot be found, the program prints 
#"There seems to be no file with that name.", if the conversion fails, "The file contents are unsuitable.", in other errors 
#"There was a problem with the program." or if everything went correctly, "The result was [result].". 
#In any case (besides KeyboardInterruption with Ctrl-C), the program should be impossible to break with user input. If everything works as intended, it prints the following:
fileName = input("Give the file name: ")

try :
    fileHandle = open(fileName, "r")

except IOError :
    print("There seems to be no file with that name.") 

else :
    try :
        number = fileHandle.read()
        number = int(number)

    except Exception :
        print("The file contents were unsuitable.") 
    else:
        try: 
            number = 1000 / number 
        except Exception :
            print("There was a problem with the program.")
        else : 
          print("The result was ", number)

#exercise 8.3
#The third exercise in the chapter continues with the calculator exercises done earlier. This time the idea is to finally take out the annoying problems with numbers, 
#input validity and the stability problems caused by type conversion funvtion. 
#Make the following changes to the calculator: Every time the user gives numbers to the program, 
#the system asks for the numbers with the prompt "Give a number: " and continues until a valid number is given. 
#If the number is not correct, the system gives an error message "This input is invalid.". If the calculator works correctly, it prints out the following:
import math 

def AskNumber() :
    number = True
    ctn = 0 
    while(number) :
        temp_number = input("Give a number: ")
        
        try:
            temp_number = int(temp_number)
            ctn = ctn +1
            if(ctn == 1) :
                first_number = temp_number
            else : 
                second_number = temp_number
            if(ctn == 2) :
                number = False
        except Exception :
            print("This input is invalid.")
     

    return first_number, second_number


def main() :
    print("Calculator")
    first_number, second_number = AskNumber() 
    decisione = True
    while(decisione) :


        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8) Quit")
        print ("Current numbers: ",first_number, " ", second_number)
        selection = input("Please select something(1-6): ")
    
        if(selection == "1") :
            print("The result is: ", first_number + second_number)
        elif(selection == "2") :
            print("The result is: ", first_number - second_number)
        elif(selection == "3") :
            print("The result is: ", first_number * second_number)
        elif(selection == "4") :
            print("The result is: ", first_number / second_number)
        elif(selection == "5") :
            print("The result is: ", math.sin(first_number /second_number))
        elif(selection == "6") :
            print("The result is: ", math.cos(first_number/second_number))
        elif(selection =="7") :
            first_number, second_number = AskNumber()
        elif(selection == "8") :
            print("Thank you!")
            decisione = False 
        else :
            print("Wrong number")    

if __name__ =="__main__" :
    main() 

#exercise 8.4
#Also the other continuous project, the notebook, has relied on user actions in the sense that it would have broken down if the user had decided to read the 
#file without writing anything to it. In this exercise we fix this, and add the possiblity of changing the used notebook file while the program is running. 
#First of all, make the program start by checking if there is a file "notebook.txt" and create one if there is none. If this has to be done, also inform 
#the user with the warning "No default notebook was found, created one.".
#When this feature works, add a fourth selection to the notebook, "(4) Change the notebook". If the user selects this option, the user is prompted for 
#a new file "Give the name of the new file: ". If there is an existing file, it is opened and loaded into the notebook program, while the old notebook file is closed. 
#If the new notebook file does not exist, the system informs the user "No notebook with that name detected, created one." and makes a new file. Also add a note of the 
#used notebook file to the main menu, "Now using file [filename]". If everything is implemented correctly, the program works as follows: 
import time 
fileName ="notebook.txt"
try:
    source =open(fileName, "r")
except Exception :
    print("No default notebook was found, created one.")
    source = (fileName, "a")    
decision = True; 

while(decision) :
    print("Now using file ", fileName)
    print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit\n")
    
    select =input("Please select one: ")
    
    if(select == "1") :
        source = open(fileName, "r")
        content = source.readlines()
        
        for i in content :
            print(i)     
        source.close()

    elif(select == "2") :
     note = input("Write a new note: ")   
     note = note + ":::" + time.strftime("%Xn %x")
     source = open(fileName, "a")
     source.write(note)
     source.close()

    elif(select =="3") :
     source = open(fileName, "w")
     print("Notes deleted.")
     source.write(" ")
     source.close()

    elif(select == "4") :
        fileName = input("Give the name of the new file: ")
        try:
            source =open(fileName, "r")
            #print("Now using file ", fileName)
        except Exception :
            source = open(fileName, "a") 
            print("No notebook with that name detected, created one.")

    elif(select == "5") :
     print("Notebook shutting down, thank you.")
     decision = False; 