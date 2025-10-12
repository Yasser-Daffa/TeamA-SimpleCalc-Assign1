from math import ceil

#------------Helper Functions------------#
def valid_input_function(prompt_message, allow_float=False):
    """
    This function keeps prompting the user continously 
    until they enter a valid number or 'exit/back/stop' to exit.
    it only works with (int) until the coder makes allow_float=True.. then it allows float numbers!

    Paramaters:
        prompt_message (str): The message shown to the user
        allow_float (bool): True if decimal numbers are allowed

    returns:
        - int or float (depending on allow_float)
        - "exit" if user typed exit/back/stop
    """
    while True:
        user_input = input(prompt_message)

        if user_input.lower() in ("stop", "back", "exit", "leave", "end", "bye"):
            return "exit"

        try:
            evaluated = float(eval(user_input))  # evaluate simple math expressions
            if not allow_float and not evaluated.is_integer():
                print("   **Can't have float!!**")
                continue
            return int(evaluated) if not allow_float else evaluated
        except:
            print("   **Must be a number or valid expression! Please try again.**")


def unit_choice_function(prompt, units_list):
    """
    This function was made to reduce code repetition..
    it gets the unit choice and compares it to check if its
    within the list boundaries... if not then it prompts the user to try again.

    Paramaters:
        prompt (str): The message shown to the user
        units_list (list): your list that you want to compare with

    """

    while True:
        choice = input(prompt)

        if choice.lower() == "list":
            print_list_function(units_list)
            continue

        elif choice.lower() in ("stop", "back", "exit", "leave", "end", "bye", "return"):
            return "exit"
        
        try:
            if not float(choice).is_integer():
                print("   **Can't have floats!!!***")
                continue
            choice = int(choice) 

        except ValueError:
            print("**Please enter a number or type 'list' to show available units.**")
            continue

        if 1 <= choice <= len(units_list):
            return choice
        
        else:
            print(f"**No unit with the number {choice}... Try again.**")



def print_list_function(your_list):
    """"
    This function neatly prints the requested list
    its modular and adjustable.

    Paramaters:
        your_list (list): prints this list in a 4 row max
    
    """
    max_rows = 4   # max number of rows.. (default: 4)
    columns = ceil(len(your_list) / max_rows)     
    # takes number of rows divides it by length of list
    # if number of rows was 3.2 it becomes 4. cuz cant have float number as a coulmn

    for i in range(max_rows):            # each row (horizontal)
        for j in range(columns):         # each column (vertical)
            index = i + j * max_rows     # computes index for each cell
            if index < len(your_list):
                print(f" {index+1:2d}- {your_list[index]:<12}".title(), end="|")
        print()  # move to next line after each row
    print("")
 
def unit_pair_function(units_list, category_name="unit"):
    """
    Another function made to reduce repetition.
    It prompts the user to choose 'from' and 'to' units.
    Returns a tuple (from_unit_index, to_unit_index)
    or 'exit' if the user chooses to leave.

    paramaters:
        units_list (list): List of available units.
        category_name (str): Optional name for category (e.g., 'temperature').
    """

    while True:
        user_unit_from = unit_choice_function(
            f"Choose the {category_name} you want to convert FROM "
            f"\nor type 'back' to leave (or 'list' to show units again): ",
            units_list
        )
        if user_unit_from == "exit":
            print("*Exiting...*")
            return "exit"

        user_unit_to = unit_choice_function(
            f"Choose the {category_name} you want to convert TO "
            f"\nor type 'back' to leave (or 'list' to show units again): ",
            units_list
        )
        if user_unit_to == "exit":
            print("*Exiting...*")
            return "exit"

        return (user_unit_from, user_unit_to)
    





#------------Unit Converter Functions------------#
def length_converter_function(value: float, from_unit: str, to_unit: str):
    """
    Convert a numeric value from one unit to another.

    Uses a dictionary of units with meters as the baseline.
    """

    length_units = {
        "meters": 1,
        "picometers": 1e-12,
        "nanometers": 1e-9,
        "micrometers": 1e-6,
        "centimeters": 0.01,
        "decimeters": 0.1,
        "kilometers": 1000,
        "megameters": 1e6,
        "inches": 0.0254,
        "feet": 0.3048,
        "mile": 1609.34,
        "yard": 0.9144,
    }

    if from_unit not in length_units or to_unit not in length_units:
        print("Unsupported unit. Please check your spelling and try again")
        return False

    result = value * length_units[from_unit] / length_units[to_unit]
    result = round(result, 4)

    return result


def length_converter_menu():
    """
    Run the length_converter interactively with user input.

    Continuously prompts the user to enter units and values to convert.
    Accepts 'stop', 'back', or 'exit' to end the loop.
    
    NOTE: list spelling has to be exactly as the dictonary
    """
    length_units_list = [
        "meters",
        "picometers",
        "nanometers",
        "micrometers",
        "centimeters",
        "decimeters",
        "kilometers",
        "megameters",
        "inches",
        "feet",
        "miles",
        "yards"
    ]
    
    print(
        "--Welcome to Length Converter Function--" \
        "\n *INFO: Converts length from a unit to another...*\n" 
        + "-"*30 + \
        "\n  Supported units:\n" \
        +"-"*30
        )


    print_list_function(length_units_list)
    
    while True:
        
        unit_pair = unit_pair_function(length_units_list)
        if unit_pair == "exit":
            break

        user_unit_from , user_unit_to = unit_pair

        # while true loop so you can go back to choosing units at any point
        while True:
            user_value = valid_input_function("Enter value (or 'back' to return to picking units): ", allow_float=True)

            if user_value == "exit": 
                print("**Back to picking units...**")
                break

            try:

                from_unit_name = length_units_list[int(user_unit_from)-1] # -1 cuz lists start from 0 to n ... not from 1 to n
                to_unit_name   = length_units_list[int(user_unit_to)-1]

                result = length_converter_function(user_value, from_unit_name, to_unit_name)

                if result is not False:
                    print(f"{user_value} {from_unit_name} → {result} {to_unit_name}") # not chat gpt, I copy pasted this arrow

            except ValueError:
                print("**Please check inputs and try again**")
                continue

length_converter_menu()

def temperature_converter_function(value: float, from_unit:str, to_unit:str):
    """
    Convert a temperature value from one unit to another.
    Uses Kelvin as the baseline.
    """

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()


    # Step 1: Convert any input to Kelvin
    if from_unit == "celsius":
        kelvin_value = value + 273.15
    elif from_unit == "fahrenheit":
        kelvin_value = (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        kelvin_value = value
    else:
        print("Unsupported unit. Please check your spelling and try again")
        return False

    # Step 2: Convert Kelvin to target unit
    if to_unit == "celsius":
        result = kelvin_value - 273.15
    elif to_unit == "fahrenheit":
        result = (kelvin_value - 273.15) * 9/5 + 32
    elif to_unit == "kelvin":
        result = kelvin_value
    else:
        print("Unsupported unit. Please check your spelling and try again")
        return False

    return round(result, 4)


def temperature_converter_menu():
    """
    Run the temperature_converter interactively with user input.

    Continuously prompts the user to enter units and values to convert.
    Accepts 'stop', 'back', or 'exit' to end the loop.
    
    NOTE: SPELLING HAS TO BE EXACT
    """
    temperature_units_list = ["celsius", "fahrenheit", "kelvin" ]
    
    print(
        "--Welcome to Temperature Converter Function--" \
        "\n*INFO: Converts temperature from one unit to another.*\n"
        + "-"*40 + \
        "\n  Supported units:\n" \
        +"-"*40
        )


    print(f"1- {temperature_units_list[0]:<5} | 2- {temperature_units_list[1]:<5} | 3- {temperature_units_list[2]:<5}".title())

    while True:
        
        unit_pair = unit_pair_function(temperature_units_list,"Temperature")

        if unit_pair == "exit":
            break

        user_unit_from , user_unit_to = unit_pair

        # while true loop so you can go back to choosing units at any point
        while True:
            user_value = valid_input_function("Enter value (or 'back' to return): ", allow_float=True)

            if user_value == "exit": 
                print("**Back to picking units...**")
                break

            try:

                from_unit_name = temperature_units_list[user_unit_from - 1].lower()
                to_unit_name   = temperature_units_list[user_unit_to - 1].lower()

                result = temperature_converter_function(user_value, from_unit_name, to_unit_name)

                if result is not False:
                    print(f"{user_value} {from_unit_name} → {result} {to_unit_name}".title())


            except ValueError:
                print("**Please check inputs and try again**")
                continue



temperature_converter_menu()



def weight_converter_function(value: float, from_unit:str, to_unit:str):
    """
    Convert a weight value from one unit to another.
    Uses grams as the baseline.
    """

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()


    weight_units = {
        "gram": 1,
        "kilogram": 1000,
        "milligram": 0.001,
        "microgram": 1e-6,
        "ton": 1e6,
        "pound": 453.59237,
        "ounce": 28.349523125,
    }

    if from_unit not in weight_units or to_unit not in weight_units:
        print("Unsupported unit. Please check your spelling and try again.")
        return False

    result = value * weight_units[from_unit] / weight_units[to_unit]


    return round(result, 4)


def weight_converter_menu():
    """
    Run the weight_converter interactively with user input.

    Continuously prompts the user to enter units and values to convert.
    Accepts 'stop', 'back', or 'exit' to end the loop.
    
    NOTE: SPELLING HAS TO BE EXACT
    """
    weight_units_list = [
        "gram",
        "kilogram",
        "milligram",
        "microgram",
        "ton",
        "pound",
        "ounce"
    ]
    
    print(
        "--Welcome to Weight Converter Function--" \
        "\n*INFO: Converts weight from one unit to another.*\n"
        + "-"*40 + \
        "\n  Supported units:\n" \
        +"-"*40
        )


    print_list_function(weight_units_list)

    while True:
        
        unit_pair = unit_pair_function(weight_units_list,"Weight")

        if unit_pair == "exit":
            break

        user_unit_from , user_unit_to = unit_pair

        # while true loop so you can go back to choosing units at any point
        while True:
            user_value = valid_input_function("Enter value (or 'back' to return): ", allow_float=True)

            if user_value == "exit": 
                print("**Back to picking units...**")
                break

            try:

                from_unit_name = weight_units_list[user_unit_from - 1].lower()
                to_unit_name   = weight_units_list[user_unit_to - 1].lower()

                result = weight_converter_function(user_value, from_unit_name, to_unit_name)

                if result is not False:
                    print(f"{user_value} {from_unit_name} → {result} {to_unit_name}".title())


            except ValueError:
                print("**Please check inputs and try again**")
                continue


weight_converter_menu()


def volume_converter_function(value: float, from_unit:str, to_unit:str):
    """
    Convert a volume value from one unit to another.
    Uses Cubic meters as the baseline.
    """

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()


    volume_units = {
        "liter": 1,
        "milliliter": 0.001,
        "gallon": 3.78541,
        "cubic meter": 1000,
        "ounce": 0.0295735
    }

    if from_unit not in volume_units or to_unit not in volume_units:
        print("Unsupported unit. Please check your spelling and try again.")
        return False

    result = value * volume_units[from_unit] / volume_units[to_unit]


    return round(result, 4)


def volume_converter_menu():
    """
    Run the volume_converter interactively with user input.

    Continuously prompts the user to enter units and values to convert.
    Accepts 'stop', 'back', or 'exit' to end the loop.
    
    NOTE: SPELLING HAS TO BE EXACT
    """
    volume_units_list = [
        "liter",
        "milliliter",
        "gallon",
        "cubic meter",
        "ounce"
    ]
    
    print(
        "--Welcome to Volume Converter Function--" \
        "\n*INFO: Converts volume from one unit to another.*\n"
        + "-"*40 + \
        "\n  Supported units:\n" \
        +"-"*40
        )


    print_list_function(volume_units_list)

    while True:
        
        unit_pair = unit_pair_function(volume_units_list,"Volume")

        if unit_pair == "exit":
            break

        user_unit_from , user_unit_to = unit_pair

        # while true loop so you can go back to choosing units at any point
        while True:
            user_value = valid_input_function("Enter value (or 'back' to return): ", allow_float=True)

            if user_value == "exit": 
                print("**Back to picking units...**")
                break

            try:

                from_unit_name = volume_units_list[user_unit_from - 1].lower()
                to_unit_name   = volume_units_list[user_unit_to - 1].lower()

                result = volume_converter_function(user_value, from_unit_name, to_unit_name)

                if result is not False:
                    print(f"{user_value} {from_unit_name} → {result} {to_unit_name}".title())


            except ValueError:
                print("**Please check inputs and try again**")
                continue

volume_converter_menu()
