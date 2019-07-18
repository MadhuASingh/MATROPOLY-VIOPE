 # -*- coding: cp1252 -*-

#exercise 7.1
#The first exercise in this chapter consists of simple module library operations. In the chapter, a module called random was introduced. 
#This module consists of several functions which can be used to get random numbers. The idea here is to create a program, which simulates 
#coin flips by randomly selecting 0 (Tails) or 1 (Heads) and printing out the result. When working correctly, the program prints out something like this:
import random 

coin = random.randint(0,1)
if(coin == 1) :
    print("Heads!")
else :
    print("Tails!")
    
#exercise 7.2
#The second exercise in this chapter continues with random selection. In this exercise the objective is to develop a game called nuke-foot-cockroach, 
#which is pretty similar to the more popular variant, paper-rock-scissors. The rules are simple: both players select either nuke, foot or cockroach, and 
#the winner is determined in the following way: Foot beats cockroach, nuke beats foot and cockroach beats nuke. If both the player and the AI select the same, it's a tie, 
#except if both choose nuke, then both lose.
#Implement the game so that the other player is computer controlled, and chooses randomly either foot(number 1), cockroach(number 3) or nuke(number 2). 
#Also implement a feature which keeps the score, calculating both rounds the player won, and ties. If the player wins, print "You WIN!", if they loose 
#"You LOSE!". If the round was a tie, either "It is a tie!" or "Both LOSE!", depending on if the tie was caused by a nuke or not. If the player selects
#"quit", the game ends and the final score is given. When the game works correctly, it prints the following:

decision = True
humanCtn = 0
computerCtn = 0
game = 0
tie = 0

while(decision) :

    human = input("Foot, Nuke or Cockroach? (Quit ends):")
    computer = random.randint(0, 3)

    if('Foot' in human) :
        print("You chose: Foot")
        if(computer == 1) :
            print("Computer chose: Foot")
            print("It is a tie!")
            game = game +1
            tie = tie +1
        elif(computer == 2) :
            print("Computer chose: Nuke")
            print("You LOSE!")
            game = game +1
            computerCtn = computerCtn + 1
        else :
            print("Computer chose: Cockroach")
            print("You LOSE!")
            game = game + 1
            computerCtn = computerCtn + 1
      
    elif('Nuke' in human) :
        print("You chose: Nuke")
        if(computer == 1) :
            print("Computer chose: Foot")
            print("You WIN!")
            game = game + 1
            humanCtn = humanCtn +1
        elif(computer == 2) :
            print("Computer chose: Nuke")
            print("It is a tie!")
            game = game + 1
            tie = tie + 1
        else :
            print("Computer chose: Cockroach")
            print("You LOSE!")
            game = game +1
            computerCtn = computerCtn + 1
    elif('Cockroach' in human) :
        print("You chose: Cockroach")
        if(computer == 1) :
            print("Computer chose: Foot")
            print("You WIN!")
            game = game +1
            humanCtn = humanCtn +1
        elif(computer == 2) :
            print("Computer chose: Nuke")
            print("You WIN!")
            game = game + 1
            humanCtn = humanCtn + 1
        else :
            print("Computer chose: Cockroach")
            print("It is a tie!")
            game = game +1
            tie = tie +1 

    elif('Quit' in human) :
        print("You played " + str(game) + " rounds, and won " + str(humanCtn) + " rounds, playing tie in " + str(tie) + " rounds." )
        decision = False
    else :
        print("Incorrect selection.")
             

#exercise 7.3
#The third exercise of this chapter goes back from game programming to a more serious line, and discusses the creation of self-made modules. 
#Unlike other exercises, in this exercise the idea is not to create a full program, but only to write a module for existing software.
#In the exercise, we already have the main program in the module, which is as follows:
#The objective is to implement this mymodule-module applied in the exercise. Create a module, which has a function printme, which prints 
#the given parameter with the disclaimer "I got:" and after that, "The parameter was [length] characters long." 
#When the module is implemented correctly, the program prints out the following
def printme(wordHere) :
    """Printing the stuff"""
    print("I got: ", wordHere )
    print("The parameter was "  + str(len(wordHere)) + "characters long.")

#exercise 7.4
#The fourth exercise in this module elaborates on the idea applied in the last exercise. In the exercise the idea is once again to
#create a module for an existing main program. The module tests the feasibility of different user-given inputs for a password. The existing code which uses the module is as follows:
def testme(userinput) :
    if(len(userinput)<5) :
        return False
    elif(userinput.isdigit() == True) or (userinput.isalpha() == True) :
        return False
    else :
        return True

#exercise 7.5
#exercise 7.5
#This exercise expands on the calculator, which was made in chapter 4, exercise 4. In this exercise, add sin() and cos() 
#-calculations from the library module math to the calculator. Add these actions as selections 5 and 6, simultaneously moving the 
#"change numbers" feature to 7 and "Quit" to 8. When the user calls either of the new features, the first number is the divident and 
#second the divider like this: sin(number_1/number2). When correctly implemented, the program prints the following:
import math

print("Calculator")
first_number = int(input("Give the first number: "))
second_number = int(input("Give the second number: "))
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
        first_number = int(input("Give the first number: "))
        second_number = int(input("Give the second number: "))
    elif(selection == "8") :
        print("Thank you!")
        decisione = False 
    else :
        print("Wrong number")

#exercise 7.6
#The last exercise in this chapter adds a small feature to the other continuous exercise project, the notebook. I
#n this exercise, add a feature which includes the date and time of the written note to the program. The program works as earlier, 
#but saves data in the form "[note]:::[date and time]" meaning that there is a three-colon separator between the note and timestamp. 
#The timestamp can be generated as follows:
import time 

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
     note = note + ":::" + time.strftime("%Xn %x")
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



            
                
       



    
    
