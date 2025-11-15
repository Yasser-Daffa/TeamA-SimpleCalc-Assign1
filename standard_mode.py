# standard.py
import helper_functions as hf


colors = hf.colors_function()


def multi_expression_function():
    print()
    hf.print_welcome_message("Calculates Expression entered for real numbers","Multi Expression")
    while True:
    
        user_input = hf.valid_input_function(f"{colors['blue']}Enter expression{colors['blue']}"
                                          f" ({colors['yellow']}'back'{colors['blue']} to return): {colors['reset']}", allow_float=True)

        if user_input == "back":
            
            break

        print(f"{colors['bright_green']}\nanswer is {colors['yellow']}{user_input}{colors['reset']}\n")


def roots_function():
    from math import pow
    print()
    hf.print_welcome_message("Calculates roots for real numbers","Roots")
    
    while True:
        
        user_roots = hf.valid_input_function(f"{colors['blue']}Enter {colors['magenta']}n-th{colors['blue']} of the root"
                                          f" ({colors['yellow']}'back'{colors['blue']} to return): {colors['reset']}", allow_float=True)
        print()

        if user_roots == "back":
            break
        
        if user_roots < 1:
            print(f"{colors['bright_red']}Error: The root must be integer and equal or greater than one.{colors['reset']}")
            continue

        user_value = hf.valid_input_function(f"{colors['blue']}Enter value under the root: {colors['reset']}", True)
        if user_value == "back":
            break
        
        if int(user_value) <= 0:
            print(f"{colors['bright_red']}Error: Roots do not accept negative numbers." \
            f" Please, enter a positive number.{colors['reset']}")
            continue
        
        result = pow(user_value, (1/user_roots))
        print(f"{colors['bright_green']}The result of root "
              f"{colors['bright_yellow']}{user_roots}{colors['bright_green']} for {colors['bright_yellow']}{user_value}"
              f"{colors['bright_green']} = {colors['bright_yellow']}{result}{colors['reset']}")


def power_function():
    """Calculates a number raised to an integer power."""
    from math import pow
    print()
    hf.print_welcome_message("Calculates a number raised to an integer power", "Power")
    
    while True:
        user_value = hf.valid_input_function(f"{colors['blue']}Enter the base number ({colors['yellow']}'back'{colors['blue']} to return): {colors['reset']}", allow_float=True)
        if user_value == "back":
            break
        
        user_power = hf.valid_input_function(f"{colors['cyan']}Enter the exponent (integer >= 0): {colors['reset']}")
        if user_power == "back":
            break
        
        if user_power < 0 or not float(user_power).is_integer():
            print(colors['bright_red'] + "**Exponent must be an integer >= 0**" + colors['reset'])
            continue

        result = pow(user_value, int(user_power))
        print(f"{colors['bright_green']}{user_value}^{int(user_power)} = {result}{colors['reset']}\n")



def reciprocal_function():
    """Calculates the reciprocal of a number."""
    print()
    hf.print_welcome_message("Calculates the reciprocal of a number", "Reciprocal")
    
    while True:
        number = hf.valid_input_function(f"{colors['blue']}Enter the number (or {colors['yellow']}'back'{colors['blue']} to return): {colors['reset']}", allow_float=True)
        if number == "back":
            break

        if number == 0:
            print(colors['bright_red'] + "**Cannot divide by zero**" + colors['reset'])
            continue
        
        result = 1 / number
        print(f"{colors['bright_green']}Reciprocal of {number} = {result}{colors['reset']}\n")


def percent_function():
    """Converts a number given in percent to decimal."""
    print()
    hf.print_welcome_message("Converts percentages to decimal numbers", "Percent")
    
    while True:
        expression = input(f"{colors['blue']}Enter a number in percent like 55% (or {colors['yellow']}'back'{colors['blue']} to return): {colors['reset']}")
        if expression in ("back", "leave", "return"):
            print("\n"+" "*12+f"{colors['bold']}{colors['yellow']}Going Back...\n{colors['reset']}")
            break
        elif expression in ("exit","stop","end"):
            print(colors['yellow'] + colors['bold'] + "\n**Exiting Mode... Goodbye!**\n" + colors['reset'])
            hf.return_main_menu()
        
        elif "%" in expression:
            expression = expression.replace("%", "/100")
            try:
                result = eval(expression)
                print(f"{colors['bright_green']}{expression} → {result}{colors['reset']}\n")
            except Exception as e:
                print(colors['bright_red'] + f"**Invalid input: {e}**" + colors['reset'])
        else:
            print(colors['bright_red'] + "**Please include '%' symbol in your input**" + colors['reset'])


def standard():
    modes_dict = {
        "multi-expression": multi_expression_function,
        "roots": roots_function,
        "power": power_function,
        "reciprocal": reciprocal_function,
        "percent": percent_function
    }

    modes_list = list(modes_dict)

    while True:
        print()
        hf.print_welcome_message("Calculator that supports the following modes", f"{colors["bright_yellow"]}Standard Calculator{colors['reset']}")
        
        
        print(f"""
{colors['bright_yellow']}1-{colors['reset']} Multi-Expression
{colors['bright_yellow']}2-{colors['reset']} Roots
{colors['bright_yellow']}3-{colors['reset']} Power
{colors['bright_yellow']}4-{colors['reset']} Reciprocal
{colors['bright_yellow']}5-{colors['reset']} Percent
              """)

        user_choice = hf.unit_choice_function(
            f"{colors['blue']}Choose a mode ({colors['yellow']}'back'{colors['blue']} to exit): {colors['reset']}", 
            modes_list
        )

        if user_choice in ("back", "leave", "return", "stop", "end", "exit"):
            print(colors['bright_yellow'] + colors['bold'] + "\nExiting Standard Calculator. Goodbye!\n" + colors['reset'])
            hf.return_main_menu()

        selected_function = modes_dict[modes_list[int(user_choice) - 1]]
        selected_function()



