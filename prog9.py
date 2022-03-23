while True:  
    print("================MENU================\n")  
    print("1. For bitwise AND operation")  
    print("2. For bitwise OR operation")  
    print("3. For bitwise NOT operation")      
    print("4. For bitwise XOR operation")  
    print("5. Exit")  
    choice = int(input("Enter your Choice: "))  

    if choice == 1: 
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        print(a, " & ", b, " = ", (a & b))
        
    elif choice == 2:  
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        print(a, " | ", b, " = ", (a | b))

    elif choice == 3:  
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        print("~a =", ~a)
        print("~b =", ~b)    
    elif choice == 4:  
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: ")) 
        print(a, " ^ ", b, " = ", (a ^ b))
    elif choice == 5:  
        break  
    else:  
        print( "Please enter a valid Input from the list")


    