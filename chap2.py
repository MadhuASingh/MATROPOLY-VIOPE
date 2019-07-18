#exercise 2.1
#The first exercise in this chapter is an easy warm-up exercise to get things rolling. The objective is to create a 
#variable by giving it the correct name, and assign it the string "string-type content" as a value. 
#Then insert this variable into a print command so that the program prints out following text:

number1 = 1000; 
number2 = 24; 

sum = number1 + number2 + 15; 

multiplication = sum * sum; 

print("The final results of the calculation was: ", multiplication)

#exercise 2.3

#In this exercise the aim is to try out different datatypes. Start by defining two variables, and assign the first variable the float value 10.6411. 
#The second variable gets a string "Stringline!" as a value. 
#Convert the first variable to an integer, and multiply the variable with the string by 2. 
#After this, finalize the program to print out the results in the following way:

integer = 10.6411
string = "StringLine!"

mult = int(integer); 
multString = string * 2; 

print("Integer conversion cannot do roundings: ", mult)
print("Multiplying strings also causes trouble: ", multString)

#exercise 2.4
#In this program the objective is to understand how the layout-characters (\t and \n} and print in general works. 
#By using only the print command, make the interpreter to print out the following text:

stringNew ="This here is divided to several lines:\nI am still in the same print-command.\n\tName:\tPeter\n\tJob:\tBabysitter\n"
print(stringNew)

#exercise 2.5
#In this exercise, the objective is to try taking input for the first time. The idea is to create a simple program which takes two numbers and perfoms an addition. 
#So, take two numbers from the user with input(), calculate the result and make the program present the result in the following way:
#In this exercise it is OK to expect that the user wont give faulty inputs, such as strings or something else non-calculatable. 
#This exercise is also the starting point for the course's two "on-going" exercises, meaning that this code will be supplemented with new features in the future. 
#Therefore it may be worthwhile to start commenting the source code. 

print("Calculator\n")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))
print("The result is: ", num1+num2)

#exercise 2.6
#The last exercise in this chapter focuses on string slices. Define a variable and assign it a string "desserts" as a value. 
#Then create three new variables, and assign them values by slicing the A) first 4 characters B) the last 4 characters and 
#C) the entire string backwards as given values. Then make the program print the answers in the following way:

bigstring = "desserts"

firstFour = bigstring[0:4]
lastFour = bigstring[4:8]
backwards = bigstring[::-1]

print("The first 4 characters were: ", firstFour)
print("The last 4 characters were: ", lastFour)
print("The string backwards was:", backwards)
