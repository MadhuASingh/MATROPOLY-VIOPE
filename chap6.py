# -*- coding: cp1252 -*-
#The first assignment in this chapter is easy: create a program with a main function and a separate subfunction called hello, 
#which when called prints "Hello there!". The subfunction does not take any parameters or return any value, just prints the line. Then, to the main function,
# add a call to the subfunction and two print commands, the first one before the call which says "Lets call the subfunction:", and one after the subfunction
# call, a print command which prints "Quitting.". If implemented correctly, the program will print the following:
#exercise 6.1

def hello() :
    print("Hello there!")

def main() :
   print("Lets call the subfunction:")

   hello()
    
   print("Quitting.")

if __name__ == "__main__" :
    main()    

#exercise 6.2
#In the second exercise the idea is to try out parameters between functions. Create a program which has the main function and a subfunction "poweroftwo". 
#The main function prompts the user for a number "Give a number: " and then this number is sent to the subfunction as a parameter. 
#The subfunction calculates the n:th power of 2 of the number (if given 3, 2*2*2; if 5, 2*2*2*2*2 and so on, 2**[number]) and prints it out with the message 
#"The result was [result]". When working correctly, the program prints: 

def poweroftwo(power) :
    for i in range(1, power) :
        result = 2**power
    return result

def main() :
    power = int(input("Give a number: "))
    result = poweroftwo(power)
    print("The result is ", result)

if __name__ == "__main__" :
    main() 

#exercise 6.3
#The third exercise tests out the default values of parameters. Create a program which has a main function and a subfunction called tester. 
#The main function prompts user for an input "Write something (quit ends): " and sends this input to the subfunction as a parameter. 
#Define the subfunction tester so that it has one parameter called "givenstring", which has the default value "Too short". 
#If the user input is less than 10 characters, the program uses the default value and if 10 or more, it prints the usergiven input. 
#If the user inputs "quit", the program is terminated. When working correctly, the program will print out something like this:
def something(givenstring="Too short") :
    print(givenstring)

def main() :
    decision = True 
    while(decision) :
        givenstring = input("Write something (quit ends):")
        
        if (givenstring == "quit") :
            decision = False 
            break; 

        if(len(givenstring) <=10) :
            something()
        else :
            something(givenstring)
if __name__ == "__main__" :
    main() 

#exercise 6.4
#The last exercise in this chapter extends the previous exercise, but it is also possible to make it completely independently. 
#Modify the function tester so that, besides testing if the length of the given string is more than ten characters, it also tests if there is the character 
#"X" (capital X) in the given string. If the string is longer than 10 characters and it has X in it, the tester subfunction returns a value True to the main function, otherwise False.
#If the subfunction returns True to the main function, the program prints "X spotted!". As earlier, if the user inputs "quit", the program terminates. 
#When working correctly, the program prints something like this:
def something(givenstring="Too short") :
    print(givenstring)

def main() :
    decision = True 
    while(decision) :
        givenstring = input("Write something (quit ends):")
        
        if (givenstring == "quit") :
            decision = False 
            break;

        if ('X' in givenstring) and (len(givenstring)>= 10) :
            something(givenstring)
            print("X spotted!") 
            continue 

        if(len(givenstring) <=10) :
            something()
        else :
            something(givenstring)
if __name__ == "__main__" :
    main() 



    

    

    


