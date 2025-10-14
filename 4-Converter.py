#==========================================================================#
#----------------------------Helper Functions------------------------------#

def colors_function():
    """
    Returns a dictionary of common terminal colors
    that can be used to print colored text.
    Usage:
        colors = get_colors()
        print(colors['red'] + "This is red text" + colors['reset'])
    """
    colors = {
        "reset": "\033[0m",
        "bold": "\033[1m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "bright_black": "\033[90m",
        "bright_red": "\033[91m",
        "bright_green": "\033[92m",
        "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m",
        "bright_magenta": "\033[95m",
        "bright_cyan": "\033[96m",
        "bright_white": "\033[97m"
    }
    return colors

colors = colors_function()

def valid_input_function(prompt_message, allow_float=False, allow_negative=True):
    """
    This function keeps prompting the user continously 
    until they enter a valid number or 'exit/back/stop' to exit.
    it only works with (int) until the coder makes allow_float=True.. then it allows float numbers!

    Paramaters:
        prompt_message (str): The message shown to the user
        allow_float (bool): True if decimal numbers are allowed. (Default: False)
        allow_negative (bool): True if negative numbers are allowed. (Default: True)

    returns:
        - int or float (depending on allow_float)
        - "exit" if user typed exit/back/stop
    """
    colors = colors_function()
    while True:
        user_input = input(prompt_message)

        if user_input.lower() in ("stop", "back", "exit", "leave", "end", "bye", "return"):
            return "exit"

        try:
            evaluated = float(eval(user_input))  # evaluate simple math expressions
            if not allow_negative and evaluated < 0:
                print(colors['bright_red']+"   **Can't have Negative Numbers!!**"+ colors['reset'])
                continue
            if not allow_float and not evaluated.is_integer():
                print(colors['bright_red']+"   **Can't have float!!**"+ colors['reset'])
                continue
            return int(evaluated) if not allow_float else evaluated
        except ZeroDivisionError:
            print(colors['bright_red'] + "   **You tried to divide by zero :( **" + colors['reset'])
        except:
            print(colors['bright_red'] + "   **Must be a number or valid expression! Please try again.**"+ colors['reset'])


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
            print()
            print_list_function(units_list)
            continue

        elif choice.lower() in ("stop", "back", "exit", "leave", "end", "bye", "return"):
            return "exit"
        
        try:
            if not float(choice).is_integer():
                print(colors['red'] + "   **Can't have floats!!!***"+ colors['reset'])
                continue
            choice = int(choice) 

        except ValueError:
            print(f"{colors['bright_red']}**Please enter a number or type 'list' to show available units.**{colors['reset']}")
            continue

        if 1 <= choice <= len(units_list):
            return choice
        
        else:
            print(colors['bright_red']+f"**No unit with the number"
                  f"{colors['bright_yellow']} {choice}{colors['reset']}{colors['bright_red']}... Try again.**{colors['reset']}")



def print_list_function(your_list,max_rows=4,spacing=12):
    """"
    This function neatly prints as tables the requested list
    its modular and adjustable.

    max rows by default is 4
    columns are added as the list needs.

    Paramaters:
        your_list (list): prints this list in a 4 row max
        max_rows (int): max rows you'd like to have
        spacing (int): spacing between each line (default 12)
    
    """
    from math import ceil

    # max_rows = 4   # max number of rows.. (default: 4)
    columns = ceil(len(your_list) / max_rows)     
    # takes number of rows divides it by length of list
    # if number of rows was 3.2 it becomes 4. cuz cant have float number as a coulmn

    for i in range(max_rows):            # each row (horizontal)
        for j in range(columns):         # each column (vertical)
            index = i + j * max_rows     # computes index for each cell
            if index < len(your_list):
                print(f" {index+1:2d}- {your_list[index]:<{spacing}}".title(), end="|")
        print()  # move to next line after each row
    print()

 

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
            f"{colors['cyan']}({colors['yellow']}'back'{colors['cyan']} leaves."
            f"{colors['yellow']}'list'{colors['cyan']} displays table again) "
            f"\n{colors['bold']}{colors['cyan']}Choose {category_name} to convert {colors['bright_white']}FROM: "
            f"{colors['reset']}",
            units_list
        )
        if user_unit_from == "exit":
            print("\n"+" "*10 + f"{colors['bold']}{colors['bright_yellow']}*Back to Converter Menu*\n{colors['reset']}")
            return "exit"
        
        user_unit_to = unit_choice_function(
            f"\n{colors['cyan']}({colors['yellow']}'back'{colors['cyan']} leaves."
            f"{colors['yellow']}'list'{colors['cyan']} displays table again) "
            f"\n{colors['bold']}{colors['cyan']}Choose {category_name} to convert {colors['bright_white']}TO: "
            f"{colors['reset']}",
            units_list
        )
        if user_unit_to == "exit":
            print("\n"+" "*10 + f"{colors['bold']}{colors['bright_yellow']}*Back to Converter Menu*\n{colors['reset']}")
            return "exit"

        return (user_unit_from, user_unit_to)
    


def print_welcome_message(info_message,category_name):
        """
        Prints colored welcome message:

        --Welcome to {category_name} Mode-- \n
        **INFO: {info_message}
        

        parameters:
            - info_message (str)
            - category_name (str)
        """
                
        print(
        "-" * 40 + f"{colors['bold']}{colors['bright_magenta']}\n"
        f"--Welcome to {colors['bright_blue']}{category_name}{colors['bright_magenta']} Mode--" 
        f"{colors['cyan']}\n*INFO: {colors['reset']}{colors['cyan']} {info_message}.*{colors['reset']}\n"
        + "-" * 40 
        )

#==========================================================================#
#------------------------Unit Converter Functions--------------------------#


def unit_conversion(value: float, from_unit: str, to_unit: str, units_dict: dict):
    """
    Converts a value from one unit to another using a common baseline.
    
    in order for this to work, you must make a dictionary and a list
    that has the exact same unit spelling as the dictionary keys.
    
    The function works for all linear conversions (e.g., length, weight, volume).
    All units have to be with regards to 1 value
    as baseline (e.g., 1 second -> 60 seconds for min and so on).

    Doesnt work for temperature and other non linear units.

    paramaters:
        - value (float): value you want to convert
        - from_unit (str): unit index(position) inside a list/dictonary
        - to_unit (str): unit index(position) inside a list/dictonary
    """

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in units_dict or to_unit not in units_dict:
        print("Unsupported unit. Please check your spelling and try again.")
        return False

    result = value * units_dict[from_unit] / units_dict[to_unit]
    if result == 0:
        return "0"
    # Displays in scientific notation if result is too small or too large
    elif abs(result) < 0.0001 or abs(result) > 10000:
        return f"{result:.4e}"  # scientific notation with 4 decimal places
    else:
        return round(result, 4)


def unit_conversion_menu(units_list, units_dict, category_name="unit"):
    """
    Interactive menu for any type of linear unit conversion.
    
    parameters:
        - units_list (list): list of the units
        - units_dict (dictonary): dictonary of the units
        - category_name (str): optional name of the category i.e., "Volume"
    """
    
    allow_negative = True
    if category_name.lower() in ("length", "area", "volume", "weight", "speed", "power", "data", "pressure"):
        allow_negative = False

    max_rows = 4
    spacing = 12
    if category_name.lower() in ("area", "weight"):
        spacing = 17
    elif category_name.lower() in ("power"):
        max_rows = 3
    elif category_name.lower() in ("data"):
        max_rows = 5
    elif category_name.lower() in ("speed"):
        spacing = 21
        max_rows = 5
    elif category_name.lower() in ("pressure"):
        spacing = 22
        max_rows = 3

        
    

    print_welcome_message(f"{colors['cyan']}Converts {category_name} from a unit to another.{colors['reset']}", category_name)

    print(" " * 7 + "Available units:\n" + "-"*40)
    
    while True:

        print_list_function(units_list, max_rows,spacing)

        unit_pair = unit_pair_function(units_list, category_name)
        if unit_pair == "exit":
            break

        user_unit_from, user_unit_to = unit_pair

        while True:
            user_value = valid_input_function(f"\n{colors['bright_cyan']}Enter value ({colors['bright_yellow']}'back'{colors['bright_cyan']} to return): {colors['reset']}"
                                                , allow_float=True, allow_negative=allow_negative)
            if user_value == "exit":
                print(f"{colors['bright_yellow']}\n**Back to picking units...**\n{colors['reset']}")
                break

            from_unit_name = units_list[user_unit_from - 1]
            to_unit_name = units_list[user_unit_to - 1]

            result = unit_conversion(user_value, from_unit_name, to_unit_name, units_dict)
            if result is not False:
                print(
                    f"{colors['bright_green']}{user_value} {from_unit_name.title()} "
                    f"{colors['bold']}{colors['bright_yellow']}→{colors['reset']} "
                    f"{colors['bright_green']}{result} {to_unit_name.title()}{colors['reset']}"
                )



#------------temperature function------------#


def temperature_logic(value: float, from_unit:str, to_unit:str):
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


def temperature_menu_function():
    """
    Run the temperature_converter interactively with user input.

    Continuously prompts the user to enter units and values to convert.
    Accepts 'stop', 'back', or 'exit' to end the loop.
    
    NOTE: SPELLING HAS TO BE EXACT
    """
    temperature_units_list = ["celsius", "fahrenheit", "kelvin" ]
    
    print()
    print_welcome_message("Converts Tempereature from one unit to another","Temperature")



    while True:
        print(f"1- {temperature_units_list[0]:<5} | 2- {temperature_units_list[1]:<5} | 3- {temperature_units_list[2]:<5}".title())
        print()
        
        unit_pair = unit_pair_function(temperature_units_list,"Temperature")

        if unit_pair == "exit":
            break

        user_unit_from , user_unit_to = unit_pair

        # while true loop so you can go back to choosing units at any point
        while True:
            user_value = valid_input_function(f"\n{colors['bright_cyan']}Enter value ({colors['bright_yellow']}'back'{colors['bright_cyan']} to return): {colors['reset']}"
                                                , allow_float=True)

            if user_value == "exit": 
                print(f"{colors['bright_yellow']}\n**Back to picking units...**\n{colors['reset']}")
                break

            try:

                from_unit_name = temperature_units_list[user_unit_from - 1].lower()
                to_unit_name   = temperature_units_list[user_unit_to - 1].lower()

                result = temperature_logic(user_value, from_unit_name, to_unit_name)

                if result is not False:
                    print(f"{user_value} {from_unit_name} → {result} {to_unit_name}".title())


            except ValueError:
                print("**Please check inputs and try again**")
                continue

#-----temp-----#

def length_function():
    length_units_dict = {
    "picometer": 1e-12,
    "nanometer": 1e-9,
    "micrometer": 1e-6,
    "millimeter": 1e-3,
    "centimeter": 0.01,
    "decimeter": 0.1,
    "meter": 1,
    "kilometer": 1e3,
    "megameter": 1e6,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34
    }

    length_units_list = list(length_units_dict)
    unit_conversion_menu(length_units_list,length_units_dict,"length")


def weight_function():
    weight_units_dict = {
        "microgram": 1e-6,
        "milligram": 1e-3,
        "gram": 1,
        "kilogram": 1e3,
        "ton": 1e6,
        "ounce": 28.349523125,
        "pound": 453.59237
        }

    weight_untis_list = list(weight_units_dict)

    unit_conversion_menu(weight_untis_list,weight_units_dict,"Weight")

def volume_function():

    volume_units_dict = {
        "milliliter": 0.001,
        "liter": 1,
        "cubic meter": 1000,
        "ounce": 0.0295735,
        "gallon": 3.78541
        }

    volume_units_list = list(volume_units_dict)
    unit_conversion_menu(volume_units_list,volume_units_dict,"Volume")

def energy_function():

    energy_units_dict = {
        "joule": 1,
        "kilojoule": 1e3,
        "megajoule": 1e6,
        "gigajoule": 1e9,
        "calorie": 4.184,
        "kilocalorie": 4184,
        "electronvolt": 1.602e-19
        }

    energy_units_list = list(energy_units_dict)
    unit_conversion_menu(energy_units_list,energy_units_dict,"Energy")

def area_function():

    area_units_dict = {
        "square millimeter": 1e-6,
        "square centimeter": 1e-4,
        "square meter": 1,
        "are": 100,
        "hectare": 10000,
        "square kilometer": 1e6,
        "square inch": 0.00064516,
        "square foot": 0.092903,
        "square yard": 0.836127,
        "acre": 4046.86,
        "square mile": 2.59e6
        }

    area_units_list = list(area_units_dict)
    unit_conversion_menu(area_units_list,area_units_dict,"Area")

def speed_function():

    speed_units_dict = {
        "centimeter per second": 1e-2,
        "meter per second": 1,
        "kilometer per second": 1e3,
        "kilometer per hour": 2.77778e-1,
        "foot per second": 3.048e-1,
        "mile per second": 1.60934e3,
        "mile per hour": 4.4704e-1,
        "knot": 0.514444,
        "mach 1": 343
    }

    unit_conversion_menu(list(speed_units_dict),speed_units_dict,"Speed")

def time_function():

    time_units_dict = {
    "microsecond": 1e-6,
    "millisecond": 1e-3,
    "second": 1,
    "minute": 60,
    "hour": 3600,
    "day": 86400,
    "week": 604800,
    "month": 2.628e+6,
    "year": 3.156e+7,
    "decade": 3.154e+8,
    "century": 3.154e+9
    }

    unit_conversion_menu(list(time_units_dict),time_units_dict,"Time")

def power_function():

    power_units_dict = {
    "microwatt": 1e-6,
    "milliwatt": 1e-3,
    "watt": 1,
    "kilowatt": 1e3,
    "megawatt": 1e6,
    "gigawatt": 1e9
    }

    unit_conversion_menu(list(power_units_dict),power_units_dict,"Power")

def pressure_function():

    pressure_units_dict = {
    "atmosphere": 101325,
    "bar": 1e5,
    "kilopascal": 1e3,
    "millimeters of mercury": 133.322,
    "pascal": 1,
    "psi": 6894.76
    }

    unit_conversion_menu(list(pressure_units_dict),pressure_units_dict,"Pressure")

def data_function():
    data_units_dict = {
        "bit": 1,
        "byte": 8,
        "kilobit": 1e3,
        "kilobyte": 8e3,
        "megabit": 1e6,
        "megabyte": 8e6,
        "gigabit": 1e9,
        "gigabyte": 8e9,
        "terabit": 1e12,
        "terabyte": 8e12,
        "petabit": 1e15,
        "petabyte": 8e15,
        "exabit": 1e18,
        "exabyte": 8e18
    }
    unit_conversion_menu(list(data_units_dict),data_units_dict,"Data")

def angle_function():
    from math import pi

    angle_units_dict = {
    "radian": 1,
    "degree": 180 / pi,
    "gradian": 200 / pi
}
    unit_conversion_menu(list(angle_units_dict),angle_units_dict,"Angle")


def converter():

    converter_dict = {
        "Length": length_function,
        "Temperature": temperature_menu_function,
        "Weight": weight_function,
        "Volume": volume_function,
        "Energy": energy_function,
        "Area": area_function,
        "Speed": speed_function,
        "Time": time_function,
        "Power": power_function,
        "Pressure": pressure_function,
        "Data": data_function,
        "Angle": angle_function
    }


    converter_list = list(converter_dict)

    
    while True:
        print_welcome_message("This is the Main menu for converter mode",f"{colors['yellow']}Converter")

        print_list_function(converter_list,4)

        user_choice = unit_choice_function(
                                            f"{colors['bright_cyan']}Choose a conversion category"
                                            f" ({colors['bright_yellow']}'back'{colors['bright_cyan']} to return): {colors['reset']}"
                                            ,converter_list)
        print()

        if user_choice == "exit":
            print(colors['bold'] + colors['bright_blue'] + "\nThanks for using the converter! Goodbye :)\n" + colors['reset'])
            break

        selected_function = converter_dict[converter_list[user_choice - 1]]
        selected_function()
