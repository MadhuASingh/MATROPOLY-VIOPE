#exercise 4.1
#The first exercise in the fourth chapter is a basic while-iteration. The assignment is simple: 
#create a program which on each turn prints the round number. Start by the round number 0 and make the iteration continue for four loops. 
#When the program works correctly, it prints out something like this:
lapNumber = 0; 
i =4; 

while(lapNumber <=i) :
    print("This is lap ", lapNumber)
    lapNumber = lapNumber +1

#exercise 4.2
#The second exercise tries to elaborates on the first task. The idea is to create an iteration where the user is able to define when the loop ends by testing the input which the user gave.
#Create a program which, for every loop, prompts the user for input, and then prints it on the screen. If the user inputs the string "quit", the program prints 
#"Bye bye!" and shuts down. When the program is working correctly it should print out something like this:

decision = True 

while(decision) :
    something = input("Write something: ")
    
    if(something == "quit") :
        decision = False
        print("Bye bye!")
    else :
        print(something) 

#exercise 4.3
#The third progam tests a for-iteration. In this program, build a calculator, which asks the user for a number, and calculates the sum of all positive numbers 
#from 0 to the usergiven input. If the user gives the number 4, the program calculates the sum 0+1+2+3, if 7, the calculation is 0+1+2+3+4+5+6. Finally, 
#the program produces an answer with the printout "The sum was:" and an answer. 
#When working correctly, the program prints something like this:
sum = 0
number = int(input("Give a number: "))
for i in range(number) :
    sum = sum + i
print("The sum was: ", sum)
 
#exercise 4.4
#The last exercise in this chapter continues with the exercise from the last chapter, the calculator. 
#In this exercise, expand the existing code by implementing the following new features: (A) Calculator does not automatically quit when the result is given, 
#allowing user to do new calculations. The user has to select "6" in the menu to exit the program. (B) The calculator shows the selected numbers in the main menu by printing 
#"Current numbers:" and the user-given input. By selecting "5" in the calculator menu, the user can change the given numbers. When implemented correctly, the program prints out following:
print("Calculator")
first_number = int(input("Give the first number: "))
second_number = int(input("Give the second number: "))
decisione = True
while(decisione) :


    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6) Quit")
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
        first_number = int(input("Give the first number: "))
        second_number = int(input("Give the second number: "))
    elif(selection == "6") :
        print("Thank you!")
        decisione = False 
    else :
        print("Wrong number")





    
