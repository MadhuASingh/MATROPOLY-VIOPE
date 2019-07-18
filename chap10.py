 # -*- coding: cp1252 -*-

#exercise 10.1
#The first exercise is related to basic class definition. Create a program which has a class Player, which has two attributes, teamcolor and points. 
#Then create a main function which creates an object from this class, gives its attributes values "Blue" and "300". After this, make the program print 
#the object data in the form "The [color] contender has [points] points!" like this:

class Player : 
    teamcolor = "Blue"
    points = "300"


def main() :
    print("The " + Player.teamcolor + " contender has " + Player.points + " points!" )

if __name__ == "__main__" :
    main() 


#exercise 10.2

#This exercise continues with the code made in the last exercise. In the last exercise one of the objectives was to create a class with two attributes, teamcolor and points. 
#Now, add two methods called "tellscore" and "goal". When the method "tellscore" is called, the objects prints out "I am [teamcolor], we have [points] points!", and if the method goal is called, 
#the object adds one point to the attribute points. Also make the attribute points a private attribute, and to accommodate that change, make the neccessary changes to get the class to work properly.
#Then modify the program's main function so that instead of printing the data itself, the main function first calls the method "goal" and then the method "tellscore". If everything went correctly, 
#the program should print out this:

class Player:
    """This is the player class"""
    
    teamcolor ="Blue"
    __points = 0 

    def goal(self):
        """add goal function"""
        self.__points =+1


    def tellscore(self):
        """tell score"""
    
        print("I am ", self.teamcolor + ", we have {}  points".format(self.__points))
    


def main() :
    """Function main"""

    player = Player()
    player.goal() 

    player.tellscore() 

if __name__ == "__main__" :
    main() 

#exercise 10.3

#In the third exercise we make one final adjustment to the class by adding initialization data and a docstring. First add a docstring "Player-class: stores data on team colors and points.". 
#After this, add an initializing method __init__ to the class, and make it prompt the user for a new player color with the message"What color do I get?: ". 
#Edit the main function to first create two player objects from the class, player1 and player2. After this, make the program call player1's method "goal" twice and player2's goal once. 
#After this, call both objects with the method "tellscore". If everything went correctly, the program should print something like this:

class Player:
    """Player-class: stores data on team colors and points."""
    __points = 0 

    def __init__(self):
        self.teamcolor = input("What color do I get?: ")
    
    def goal(self):
        """add goal function"""
        self.__points = self.__points + 1


    def tellscore(self):
        """tell score"""
    
        print("I am ", self.teamcolor + ", we have {}  points".format(self.__points))
    


def main() :
    """Function main"""

    Luca = Player()
    Mauro = Player()
    
    Luca.goal()
    Luca.goal()


    Mauro.goal()


    Luca.tellscore()
    Mauro.tellscore() 

if __name__ == "__main__" :
    main() 

#exercise 10.4
#The last exercise in chapter 10, and at the same time the course tries out inheritance. In this exercise, your task is to define a new class which will be inherited from the 
#class Customer defined in the chapter's theory part.
#Define a new class called ManageCustomer which has the following abilities: 
#1) A method "addbill", which increases the attribute total by 50, and 
#2) a method "payment" which decreases the attribute total by 100.
#Remember that you only need to write the new inheriting class ManageCustomer. 
#The system will test the class, but in the submitted answer only the class definition is needed. If the class is defined correctly, the program will print the following


class Customer:
    name ="John John"
    total = 1000
    paymenttype = "Mastercard"
    number = "1234"

    def printout(self):
        print("Name: ", self.name)
        print("Total: ", self.total)
        print("Payment type: ", self.paymenttype)
        print("Card/Bill number: ", self.number)

class ManageCustomer(Customer):
    """Manage Customer class"""
    def addbill(self):
        self.total = self.total + 50 
    def payment(self):
        self.total = self.total - 100

def main():
    person = ManageCustomer()
    person.name ="Luca Zelioli"
    person.addbill()
    person.payment()
    person.payment()
    person.printout()
