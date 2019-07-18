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