
def valid_integer(prompt):
    while True:
        try:
            user_input = input(prompt)
            number = int(user_input)
            return number
        except ValueError:
            print("Error, Input must be an integer only")
            
def convert_base():
    print("\n--- Base Conversion ---")
    print("1. Decimal to Other Base")
    print("2. Other Base to Decimal ")
    
    choice = valid_integer("Enter conversion type (1 or 2): ")
    
    if choice == 1:
        
        dec_num = valid_integer("Enter the Decimal Number: ")
        
        print("""\nConvert to which base?"
1 for Binary
2 for Octal
3 for Hexadecimal\n"""
              )
        
        targer_choice = eval(input("Enter conversion type (1 or 2 or 3): "))
        
        if targer_choice == 1:
            result = bin(dec_num)[2:]
            print(f"\n Binary: {result}")
        elif targer_choice == 2:
            result = oct(dec_num)[2:]
            print(f"\n Octal: {result}")
        elif targer_choice == 3:
            result = hex(dec_num)[2:].upper()
            print(f"\n Hexadecimal: {result}")
        else:
            print("Error Invalid selection")
            
    elif choice == 2:

        print("\nWhat is the original base of the number?")
        print("1 Binary (Base 2)")
        print("2 Octal (Base 8)")
        print("3 Hexadecimal (Base 16)")
        
        choice_num = eval(input("Enter conversion type (1 or 2 or 3)"))
        
        base_transformation = {1: 2, 2: 8, 3: 16}
        base = base_transformation.get(choice_num)
        
        if base:
            num_string = input(f"\nEnter the number in base {base} (0-9, A-F for Hex): ")
            try:
                dec_num = int(num_string, base)
                print(f"\n Decimal: {dec_num}")
            except ValueError:
                print(f" Error Invalid number format for base {base}. Please ensure all digits are valid.")
        else:
            print("Error Invalid original base selection")
def bitwise_operations():

    print("\n--- Bitwise Operations ---")
    
    num1 = valid_integer("Enter the first integer: ")
    
    operator = input("Enter the operation (1 for &, 2 for |, 3 for ^, 4 for <<, 5 for >>, 6 for ~ ): ")
    
    if operator == "6":
        result = ~num1
        print(f"\n Decimal Result: {result}")
        print(f" Binary Result: {bin(result)}")
        return
        
    num2 = valid_integer("Enter the second integer (or the shift amount for << and >>): ")
    
    if operator == "1":
        result = num1 & num2
    elif operator == "2":
        result = num1 | num2  
    elif operator == "3":
        result = num1 ^ num2  
    elif operator == "4":
        result = num1 << num2 
    elif operator == "5":
        result = num1 >> num2 
    else:
        print("Error Invalid operation")
        return

    print(f"\n Decimal Result: {result}")
    print(f" Binary Result: {bin(result)}")

def menu_programmer_mode():

    print("\n===========================================")
    print("   Welcome to Programmer Mode Calculator  ")
    print("===========================================")
    
    while True:
        print("\nSelect an operation:")
        print("1. Base Conversions")
        print("2. Bitwise Operations")
        print("3. Exit")
        
        choice = input("Enter your choice (1 or 2 or 3) ")
        
        if choice == '1':
            convert_base()
        elif choice == '2':
            bitwise_operations()
        elif choice == '3':
            print("Exit")
            break
        else:
            print("Error Invalid choice, Please try again.")

menu_programmer_mode()

