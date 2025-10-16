import helper_functions as hf
colors = hf.colors_function()


def valid_integer(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() in ("back", "leave", "return"):
            print("\n"+" "*12+f"{colors['yellow']}Going Back...\n{colors['reset']}")
            return "back"
            
        if user_input in ("exit", "stop", "end"):
            print(colors['bright_yellow'] + colors['bold'] + "\n**Exiting Programmer Mode... Goodbye!**\n" + colors['reset'])
            hf.return_main_menu()

        try:
            number = int(user_input)
            return number
        except ValueError:
            print(colors['bright_red'] + "\nError, Input must be an integer only\n" + colors['reset'])
            

def convert_base():

    while True:
        print(f"\n{colors['bright_magenta']}--- Base Conversion ---{colors['reset']}")
        print(f"{colors['bright_cyan']}1.{colors['bright_yellow']} Decimal to Other Base")
        print(f"{colors['bright_cyan']}2.{colors['bright_yellow']} Other Base to Decimal{colors['reset']}")
            
        choice = valid_integer(
            f"{colors['blue']}Enter conversion type ({colors['yellow']}1-2{colors['blue']}, or {colors['yellow']}'back'{colors['blue']}): {colors['reset']}"
        )
        if choice == "back":
            break
        elif choice not in (1, 2):
            print(f"{colors['bright_red']}Invalid selection!! Please select numbers 1 or 2{colors['reset']}")
            continue

        # ---------- Decimal to Other Base ----------
        if choice == 1:
            while True:
                print(f"""\n{colors['magenta']}Convert to which base?{colors['reset']}
{colors['bright_yellow']}1. Binary (Example: 13 → 1101)
2.{colors['bright_yellow']} Octal (Example: 13 → 15)
3.{colors['bright_yellow']} Hexadecimal (Example: 13 → D)
""")
                targer_choice = input(f"{colors['blue']}Enter conversion type (1-3): {colors['reset']}")
                if targer_choice in ("back", "leave", "return"):
                    break
                elif targer_choice in ("stop", "end", "exit"):
                    hf.return_main_menu()

                try:
                    targer_choice = int(eval(targer_choice))
                    if targer_choice not in (1, 2, 3):
                        raise ValueError
                except:
                    print(colors['bright_red'] + "Error Invalid selection" + colors['reset'])
                    continue

                # Edited to ask for the decimal number last
                while True:
                    try:
                        dec_num = valid_integer(f"{colors['cyan']}Enter the Decimal Number: {colors['reset']}")
                        
                        if dec_num in ("back", "leave", "return"):
                            break
                        elif dec_num in ("stop", "end", "exit"):
                            hf.return_main_menu()
                        
                        if targer_choice == 1:
                            result = bin(int(dec_num))[2:]
                            print(f"\n{colors['bright_green']}Binary: {result}{colors['reset']}")
                        elif targer_choice == 2:
                            result = oct(int(dec_num))[2:]
                            print(f"\n{colors['bright_green']}Octal: {result}{colors['reset']}")
                        elif targer_choice == 3:
                            result = hex(int(dec_num))[2:].upper()
                            print(f"\n{colors['bright_green']}Hexadecimal: {result}{colors['reset']}")
                    except ValueError:
                        print(colors['bright_red'] + "Invalid Decimal input! Try again." + colors['reset'])
                        continue


        # ---------- Other Base to Decimal ----------
        elif choice == 2:
            while True:
                print(f"\n{colors['magenta']}What is the original base of the number?{colors['reset']}")
                print(f"1.{colors['bright_yellow']} Binary (Base 2 ex. 1101 → 13)")
                print(f"2.{colors['bright_yellow']} Octal (Base 8 ex. 15 → 13)")
                print(f"3.{colors['bright_yellow']} Hexadecimal (Base 16 ex. D → 13)")

                choice_num = input(f"{colors['blue']}Enter conversion type (1-3): {colors['reset']}")
                if choice_num in ("back", "leave", "return"):
                    break
                elif choice_num in ("stop", "end", "exit"):
                    hf.return_main_menu()

                try:
                    choice_num = int(eval(choice_num))
                    base_transformation = {1: 2, 2: 8, 3: 16}
                    base = base_transformation.get(choice_num)
                    if not base:
                        raise ValueError
                except:
                    print(f"{colors['bright_red']}Invalid input!! Try again...{colors['reset']}")
                    continue

                # same edit: ask for the number last
                while True:
                    num_string = input(f"\n{colors['cyan']}Enter the number in base {base} (0-9, A-F for Hex): {colors['reset']}")
                    if num_string in ("back", "leave", "return"):
                        break
                    elif num_string in ("stop", "end", "exit"):
                        hf.return_main_menu()

                    try:
                        dec_num = int(num_string, base)
                        print(f"\n{colors['bright_green']}Decimal: {dec_num}{colors['reset']}")
                        
                    except ValueError:
                        print(f"{colors['bright_red']}Error: Invalid number format for base {base}.{colors['reset']}")
                        continue

                break




def bitwise_operations():

    while True:
        print(f"\n{colors['bright_magenta']}--- Bitwise Operations ---{colors['reset']}")

        print(f"\n{colors['bright_yellow']}1{colors['reset']}. AND (&)")
        print(f"{colors['bright_yellow']}2{colors['reset']}. OR (|)")
        print(f"{colors['bright_yellow']}3{colors['reset']}. XOR (^)")
        print(f"{colors['bright_yellow']}4{colors['reset']}. LEFT SHIFT (<<)")
        print(f"{colors['bright_yellow']}5{colors['reset']}. RIGHT SHIFT (>>)")
        print(f"{colors['bright_yellow']}6{colors['reset']}. NOT (~)\n")

        operator = input(f"{colors['blue']}Enter the operation ({colors['yellow']}1-6"
                         f" or{colors['yellow']}'back'{colors['blue']} to return): {colors['reset']}")
        
        if operator in ("back", "leave", "return"):
            break
        elif operator in ("stop", "end", "exit"):
            hf.return_main_menu()

        if operator not in ("1","2","3","4","5","6"):
            print(colors['bright_red'] + "\nError: Invalid operation! Choose 1–6." + colors['reset'])
            continue

        while True:

            num1 = valid_integer(f"{colors['cyan']}Enter the first integer ({colors['bright_yellow']}'back'{colors['cyan']} to return): {colors['reset']}")

            if num1 in ("back", "leave", "return"):
                break
            elif num1 in ("stop", "end", "exit"):
                hf.return_main_menu()

            num1 = int(num1)

            if operator != "6":
                num2 = valid_integer(f"{colors['cyan']}Enter the second integer (or shift amount for <</>>) "
                                     f"({colors['bright_yellow']}'back'{colors['cyan']} to return): {colors['reset']}")
                if num2 in ("back", "leave", "return"):
                    continue
                elif num2 in ("stop", "end", "exit"):
                    hf.return_main_menu()

            num2 = int(num2)

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
            elif operator == "6": 
                result = ~num1

            print(f"\n{colors['bright_green']}Decimal Result: {result}{colors['reset']}")
            print(f"{colors['bright_cyan']}Binary Result: {bin(result)}{colors['reset']}\n")




def programmer():
    
    while True:
        hf.print_welcome_message("Binary, Hex, Octal, and Bitwise Calculations",f"{colors['bright_yellow']}Programmer")
        print(f"{colors['bright_cyan']}Select an operation:{colors['reset']}")
        print(f"{colors['bright_yellow']}1.{colors['bright_white']} Base Conversions")
        print(f"{colors['bright_yellow']}2.{colors['bright_white']} Bitwise Operations")
        print(f"{colors['bright_yellow']}3.{colors['bright_white']} Exit{colors['reset']}")
        
        choice = input(f"{colors['blue']}\nEnter your choice "
                       f"({colors['yellow']}1-3{colors['blue']}, or{colors['yellow']} 'exit'{colors['blue']}): {colors['reset']}")
        
        if choice == '1':
            convert_base()
        elif choice == '2':
            bitwise_operations()
        elif choice == '3'or choice in ("exit","stop","end","leave","back"):
            print(colors['bold'] + colors['yellow'] + "\nThanks for using the Programmer-mode! Goodbye.\n" + colors['reset'])
            hf.return_main_menu()
        else:
            print(colors['bright_red'] + "Error Invalid choice, Please try again." + colors['reset'])



