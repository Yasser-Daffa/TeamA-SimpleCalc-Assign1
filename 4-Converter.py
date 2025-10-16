
import helper_functions as hf

colors = hf.colors_function()

#==========================================================================#
#------------------------Unit Converter Functions--------------------------#

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
        user_unit_from = hf.unit_choice_function(
            f"{colors['cyan']}({colors['yellow']}'back'{colors['cyan']} leaves."
            f"{colors['yellow']}'list'{colors['cyan']} displays table again) "
            f"\n{colors['bold']}{colors['cyan']}Choose {category_name} to convert {colors['bright_white']}FROM: "
            f"{colors['reset']}",
            units_list
        )
        if user_unit_from == "back":
            print("\n"+" "*10 + f"{colors['bold']}{colors['bright_yellow']}*Back to Converter Menu*\n{colors['reset']}")
            return "back"
        
        user_unit_to = hf.unit_choice_function(
            f"\n{colors['cyan']}({colors['yellow']}'back'{colors['cyan']} leaves."
            f"{colors['yellow']}'list'{colors['cyan']} displays table again) "
            f"\n{colors['bold']}{colors['cyan']}Choose {category_name} to convert {colors['bright_white']}TO: "
            f"{colors['reset']}",
            units_list
        )
        if user_unit_to == "back":
            print("\n"+" "*10 + f"{colors['bold']}{colors['bright_yellow']}*Back to Converter Menu*\n{colors['reset']}")
            return "back"

        return (user_unit_from, user_unit_to)

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
    
    # prints in scientific notation if result is too small or too large
    if result == 0:
        return "0"
    elif abs(result) < 0.0001 or abs(result) > 10000:
        return f"{result:.4e}"  # scientific notation after 4 decimal places
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

    
    while True:

        hf.print_welcome_message(f"{colors['cyan']}Converts {category_name} from a unit to another.{colors['reset']}", category_name)

        print(" " * 7 + "Available units:\n" + "-"*40)

        hf.print_list_function(units_list, max_rows,spacing)

        unit_pair = unit_pair_function(units_list, category_name)
        if unit_pair == "back":
            break
        
        user_unit_from, user_unit_to = unit_pair

        while True:
            user_value = hf.valid_input_function(f"\n{colors['bright_cyan']}Enter value ({colors['bright_yellow']}'back'{colors['bright_cyan']} to return): {colors['reset']}"
                                                , allow_float=True, allow_negative=allow_negative)
            if user_value == "back":
                print(f"{colors['bright_yellow']}\n**Back to picking units...**\n{colors['reset']}")
                break

            from_unit_name = units_list[int(user_unit_from) - 1]
            to_unit_name = units_list[int(user_unit_to) - 1]

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


    # Step 2: Convert Kelvin to target unit
    if to_unit == "celsius":
        result = kelvin_value - 273.15
    elif to_unit == "fahrenheit":
        result = (kelvin_value - 273.15) * 9/5 + 32
    elif to_unit == "kelvin":
        result = kelvin_value

    return round(result, 4)


def temperature_menu_function():
    """
    Run the temperature_converter interactively with user input.

    Continuously prompts the user to enter units and values to convert.
    Accepts 'stop', 'back', or 'exit' to end the loop.
    
    NOTE: SPELLING HAS TO BE EXACT
    """
    temperature_units_list = ["celsius", "fahrenheit", "kelvin" ]

    while True:
        print()
        hf.print_welcome_message("Converts Tempereature from one unit to another","Temperature")

        print(f"1- {temperature_units_list[0]:<5} | 2- {temperature_units_list[1]:<5} | 3- {temperature_units_list[2]:<5}".title())
        print()
        
        unit_pair = unit_pair_function(temperature_units_list,"Temperature")

        if unit_pair == "back":
            break

        user_unit_from , user_unit_to = unit_pair

        # while true loop so you can go back to choosing units at any point
        while True:
            user_value = hf.valid_input_function(f"\n{colors['bright_cyan']}Enter value ({colors['bright_yellow']}'back'{colors['bright_cyan']} to return): {colors['reset']}"
                                                , allow_float=True)

            if user_value == "back": 
                print(f"{colors['bright_yellow']}\n**Back to picking units...**\n{colors['reset']}")
                break

            try:

                from_unit_name = temperature_units_list[int(user_unit_from) - 1].lower()
                to_unit_name   = temperature_units_list[int(user_unit_to) - 1].lower()

                result = temperature_logic(user_value, from_unit_name, to_unit_name)

    
                print(
                f"{colors['bright_green']}{user_value} {from_unit_name.title()} "
                f"{colors['bold']}{colors['bright_yellow']}→{colors['reset']} "
                f"{colors['bright_green']}{result} {to_unit_name.title()}{colors['reset']}"
                )

            except ValueError:
                print(f"{colors['bright_red']}**Please check inputs and try again**{colors['reset']}")
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
        hf.print_welcome_message("This is the Main menu for converter mode",f"{colors['yellow']}Converter")

        hf.print_list_function(converter_list,4)

        user_choice = hf.unit_choice_function(
                                            f"{colors['bright_cyan']}Choose a conversion category"
                                            f" ({colors['bright_yellow']}'back'{colors['bright_cyan']} to return): {colors['reset']}"
                                            ,converter_list)
        print()

        if user_choice == "back":
            print(colors['bold'] + colors['bright_yellow'] + "\nThanks for using the converter! Goodbye :)\n" + colors['reset'])
            break

        selected_function = converter_dict[converter_list[int(user_choice) - 1]]
        selected_function()

