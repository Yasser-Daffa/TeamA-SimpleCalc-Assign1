
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

