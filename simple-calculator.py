
again = "y"

while again == "y":
    
    
    first_number = int(input("first number: "))
    operations = input("enter operation(+,-,*,/:) ")
    second_number = int(input("second number: "))
  
        

    if operations == "+":
        result = first_number + second_number
        print(result)
        

    elif operations == "-":
        result = first_number - second_number
        print(result)
        
        

    elif operations == "*":
        result = first_number * second_number
        print(result)



    elif operations == "/":
        
        if second_number == 0:
            print("cant divide by zero")
        else:
            result = first_number / second_number
            print(result)
    else:
        print("Invalid Number")
        
    again = input("Do you want to calculate again? (y/n):")
        
