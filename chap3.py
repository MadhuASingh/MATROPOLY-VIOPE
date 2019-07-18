#exercise 3.1
#The exercises of the third chapter, as well as the third chapter itself, focus on the conditional if-structure. 
#In the first exercise the objective is to create a simple if-structure. The program should first ask a number from the user and save it to a variable. 
#Then if the number is even (possible to divide by 2), the program should print the text "The given number was even.". The best way to do this is to use the operator remainder. 
#The program should print the following:

value = int(input("Give a number: "))
print(value); 

if(value % 2 == 0) :
    print("The given number was even")

#exercise 3.2
#The second exercise takes another step towards more realistic programming structures. 
#In this exercise the idea is to create an if-structure, which has another if-structure inside it. 
#Basically the idea is to implement the following structure

user = "John"
password = "ABC123"

insertUser = input("Give name: ")

if(insertUser == user) : 
    insertPsw = input("Give password: ")
    
    if(insertPsw == password) :
        print("Both inputs are correct!")
    else :
        print("The password is incorrect")
    
else :
    print("The given name is wrong.")

        
#exercise 3.3 
#The third exercise is to create a conditional structure which prints a line depending on the given selection. 
#The program asks a number between 1 and 3, and based on the number prints the following: 1 prints "You selected one.", 2 prints "You selected two."
# and 3 prints "You selected three.", like this

number = input("Select a number (1-3): ")

if(number == "1") :
    print("You selected one.")
elif(number == "2") :
    print("You selected two.")
else : 
    print("You selected three.")    

#exercise 3.4
#In the fourth exercise the idea is to define an if-structure which decides the action based on several inputs. The program asks for two numbers. 
#If both of the numbers are even, the program prints "Both numbers are even." If only one of the numbers is even, the program prints "One of the numbers is even.". 
#Finally, if neither of the numbers is even, the program prints "Both numbers are odd". When correct, the program works as following:

number1 = int(input("Give a number: "))
number2 =int(input("Give another number: "))

if(number1 % 2 == 0) and (number2 %2 == 0) :
    print("Both numbers are even.")
elif(number1 % 2 != 0) and (number2 % 2 != 0) :
    print("Both numbers are odd.")
else : 
    print("One of the numbers is even.")

#exercise number 3.5
#The last exercise of chapter 5 continues the exercise made in the previous chapter. In this exercise, expand the calculator so that the user can select what kind of calculation is done. 
#If the user chooses 1, the calculator does addition as earlier. If 2, the calculator does substraction, if 3, it does multiplication, if 4, division. 
#Also add the instructions for the user to know what to do as shown in the example below. Also, if the user selects anything else besides 1-4, the program prints 
#"Selection was not correct.". When working correctly, the progam looks like the following: 

print ("Calculator")
first_num = int(input("Give the first number: "))
second_num = int(input("Give the second number: "))
print("(1) +\n(2) -\n(3) *\n(4) /\n")
choice = input("Please select something (1-4): ")

if(choice == "1") :
    print("The result is: ", first_num + second_num)
elif(choice == "2") :
    print("The result is: ", first_num - second_num)
elif(choice == "3") :
    print("The result is: ", first_num * second_num)
elif(choice == "4") : 
    print("The result is: ", first_num / second_num)
else :
    print("Selection was not correct.")


    

