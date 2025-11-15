import helper_functions as hf

from standard_mode import standard
from programmer_mode import programmer
from scientific_mode import scientific
from converter_mode import converter

colors = hf.colors_function()

def all_modes_menu():
    modes_dict = {
        "standard-mode": standard,
        "programmer-mode": programmer,
        "scientific-mode": scientific,
        "coverter-mode": converter
    }

    modes_list = list(modes_dict.keys())

    while True:
        print("#"+"-"*44+"#")
        print(" "*5 +f"{colors['bold']}{colors['bright_magenta']}Team-A Simple Calculator {colors['yellow']}Main Menu{colors['reset']}")
        print("#"+"-"*44+"#")

        print(" "*10+f"{colors['bright_green']}1- {colors['bright_white']}Standard-Mode")
        print(" "*10+f"{colors['bright_green']}2- {colors['bright_white']}Programmer-Mode")
        print(" "*10+f"{colors['bright_green']}3- {colors['bright_white']}Scientific-Mode")
        print(" "*10+f"{colors['bright_green']}4- {colors['bright_white']}Coverter-Mode\n")

        user_choice = hf.unit_choice_function(f"{colors['bright_cyan']}Select calculation mode: {colors['reset']}",modes_list)

        if user_choice in ("stop","end","exit","leave","return","back"):
            exit()
    
        selected_mode = modes_dict[modes_list[int(user_choice) - 1]]
        
        selected_mode()

all_modes_menu()
