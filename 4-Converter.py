


#This function takes the user input and fixes it so the function LenghthConverter Fucntion can read it
def units_fix(unit:str):
    unit = unit.lower().strip()

    if unit == "foot": return "feet"
    if unit == "inch": return "inches"
    if unit == "metre": return "meters"

    return unit
    




def length_converter(value:float, From_Unit:str, To_Unit:str):
    From_Unit = units_fix(From_Unit)
    To_Unit = units_fix(To_Unit)

    #unit dictonary from meters as a baseline to specified unit.. you can add more if you want. (should all be lowercase)
    #I typed the values twice for all units so the function can read if the user entered it as "m" or as "meters".
    units = { 
        "meters": 1, "m": 1, 

        "feet":0.3048, "ft":0.3048,
        
        "inches": 0.0254, "in": 0.0254,

        "nanometers": 10**-9, "nm": 10**-9,

        "centimeters": 0.01, "cm": 0.01,

        "kilometers": 1000, "km": 1000
        
        #add a comma after every unit if you want to add more units on it.
        }
    
    
    # check if units are supported
    if From_Unit not in units or To_Unit not in units:
        print("Unsupported unit. Please check your spelling and try again")
        return False
    
    result = value * units[From_Unit] / units[To_Unit]
    result = round(result, 2)

    return result


#this function runs the LengthConverter function and error handles it
def length_converter_runner():
    print("--Welcome to Length Converter Fubnction-- \n *INFO: This function converts length from a unit to another...*")
    while True:
        Units_User_Choice = input("Pick a unit you want to convert to and from separated by commas.. \n(E.g. 'm,ft' or 'Meters,Feet') \n " \
        "enter the value here or enter 'stop' to go back: ")

        if Units_User_Choice.lower() in ("stop", "back", "exit"):
            print("Exiting Length converter function...")
            break  # exit the loop

        
        try: 

            #trys to split the choices from user and adds it to a list
            #then we take each lists and put them in a variable
            Units_List = Units_User_Choice.split(',')
            
            From_Unit = Units_List[0].strip()
            To_Unit = Units_List[1].strip()

        except ValueError:
            print("**Please enter two Strings as instructed.. e.g. m,ft**")
            continue
        except Exception:
            print("**ERROR.. please enter values as instructed.. e.g. 'm,ft'** ")
            continue

        try:
            User_Value = float(input("enter value you want to convert..: "))
                
            result = length_converter(User_Value,From_Unit,To_Unit)

            if result is not False:
                    print(f"{User_Value} '{From_Unit}' = {result} in '{To_Unit}'")

        except ValueError:
            print("**please check inputs and try again**")
    

length_converter_runner()






# while True:
#     userinput = input("enter catagory you want \nLegnth, Weight, Temperature or Volume: ")
#     break


