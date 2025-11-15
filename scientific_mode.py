import math
import helper_functions as hf
colors = hf.colors_function()

def sinfunction(Value, DEG_RAD, user2):
    if user2 == "csc":
        Value0 = Value if DEG_RAD == "degrees" else math.degrees(Value)
        if Value0 % 180 == 0:
            print("Value cannot be 0 for csc")
            Value1(Value, DEG_RAD, user2)
            return
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        
        sin_csc = 1 / math.sin(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        sin_csc = math.sin(Value)
    print(f"{colors['bright_green']}Result: {colors['reset']}", round(sin_csc,2),)
    Value1(Value,DEG_RAD,user2)
    return

def cosfunction(Value, DEG_RAD, user2):
    if user2 == "sec":
        Value0 = Value if DEG_RAD == "degrees" else math.degrees(Value)
        if Value0 % 180 == 90:
            print(f"{colors['bright_red']}Value not valid for sec (cos=0){colors['reset']}")
            Value1(Value, DEG_RAD, user2)
            return
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        cos_sec = 1 / math.cos(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        cos_sec = math.cos(Value)
    print(f"{colors['bright_green']}Result: {colors['reset']}", round(cos_sec,2))
    Value1(Value,DEG_RAD,user2)
    return

def tanfunction(Value, DEG_RAD, user2):
    if user2 == "cot":
        Value0 = Value if DEG_RAD == "degrees" else math.degrees(Value)
        if Value0 % 180 == 0 :
            print(f"{colors['bright_red']}Value not valid for cot (tan=0){colors['reset']}")
            Value1(Value, DEG_RAD, user2)
            return
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        tan_cot = 1 / math.tan(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        tan_cot = math.tan(Value)
    print(f"{colors['bright_green']}Result: {colors['reset']}", round(tan_cot,2))
    Value1(Value,DEG_RAD,user2)
    return










def arcsinfunction(Value, DEG_RAD, user2):
    if user2 == "arccsc":
        if Value == 0:
            print(f"{colors['bright_red']}Value cannot be 0 for arccsc{colors['reset']}")
            Value1(Value, DEG_RAD, user2)
            return
        result = math.asin(1 / Value)
    else:
        if -1 <= Value <= 1:
            result = math.asin(Value)
        else:
            print(f"{colors['bright_red']}The number must be between -1 and 1{colors['reset']}")
            Value1(Value, DEG_RAD, user2)
            return

    if DEG_RAD == "degrees":
        result = math.degrees(result)
    print(f"{colors['bright_green']}Result: {colors['reset']}", round(result,2))
    Value1(Value,DEG_RAD,user2)
    return


def arccosfunction(Value, DEG_RAD, user2):
    if user2 == "arcsec":
        if Value == 0:
            print(f"{colors['bright_red']}Value cannot be 0 for arcsec{colors['reset']}")
            Value1(Value, DEG_RAD, user2)
            return
        result = math.acos(1 / Value)
    else:
        if -1 <= Value <= 1:
            result = math.acos(Value)
        else:
            print(f"{colors['bright_red']}The number must be between -1 and 1{colors['reset']}")
            Value1(Value, DEG_RAD, user2)
            return

    if DEG_RAD == "degrees":
        result = math.degrees(result)
    print(f"{colors['bright_green']}Result: {colors['reset']}", round(result,2))
    Value1(Value,DEG_RAD,user2)
    return


def arctanfunction(Value, DEG_RAD, user2):
    if user2 == "arccot":
        if Value == 0:
            print(f"{colors['bright_red']}Value cannot be 0 for arccot{colors['reset']}")
            Value1(Value, DEG_RAD, user2)
            return
        result = math.atan(1 / Value)
    else:
        result = math.atan(Value)

    if DEG_RAD == "degrees":
        result = math.degrees(result)
    print(f"{colors['bright_green']}Result: {colors['reset']}", round(result,2))
    Value1(Value,DEG_RAD,user2)
    return



def sinhfunction(Value, DEG_RAD, user2):
    if user2 == "csch":
        
        if Value == 0:
            print(f"{colors['bright_red']}Value cannot be 0 for csch{colors['reset']}")
            Value1(Value, DEG_RAD, user2)
            return
        result = 1 / math.sinh(Value)
    else:
       
        result = math.sinh(Value)

    print(f"{colors['bright_green']}Result: {colors['reset']}", result)
    Value1(Value,DEG_RAD,user2)
    return


def coshfunction(Value, DEG_RAD, user2):
    if user2 == "sech":
        
        result = 1 / math.cosh(Value)
    else:
       
        result = math.cosh(Value)

    print(f"{colors['bright_green']}Result: {colors['reset']}", result)
    Value1(Value,DEG_RAD,user2)
    return


def tanhfunction(Value, DEG_RAD, user2):
    if user2 == "coth":
        
        if Value == 0:
            print(f"{colors['bright_red']}Value cannot be 0 for coth{colors['reset']}")
            Value1(Value, DEG_RAD, user2)
            return
        result = 1 / math.tanh(Value)
    else:
       
        result = math.tanh(Value)

    print(f"{colors['bright_green']}Result: {colors['reset']}", round(result,2))
    Value1(Value,DEG_RAD,user2)



def log_function(Value, DEG_RAD, user2):
     if Value <= 0:
        print(f"{colors['bright_red']}the number must be > 0 try again{colors['reset']}")
        Value1(Value,DEG_RAD,user2)
        return
     else:
        Value= math.log10(Value)
        print(f"{colors['bright_green']}Result: {colors['reset']}",round(Value,2))
        Value1(Value,DEG_RAD,user2)
        
def ln_function(Value, DEG_RAD, user2):
     if Value <= 0:
        print(f"{colors['bright_red']}the number must be > 0 try again{colors['reset']}")
        Value1(Value,DEG_RAD,user2)
        return
     else:
        Value= math.log(Value)
        print(f"{colors['bright_green']}Result: {colors['reset']}",round(Value,2))
        Value1(Value,DEG_RAD,user2)

def i_function(Value, DEG_RAD, user2):
     if Value < 0 or not float(Value).is_integer():
        print(f"{colors['bright_red']}the number must be > 0 and  not float try again{colors['reset']}")
        Value1(Value,DEG_RAD,user2)
        return
     else:
        Value= math.factorial(int(Value))
        print(f"{colors['bright_green']}Result: {colors['reset']}",round(Value,2))
        Value1(Value,DEG_RAD,user2)
        
def exp_function(Value, DEG_RAD, user2):
    print(f"{colors['bright_green']}Result: {colors['reset']}",round(math.exp(Value),2))
    Value1(Value,DEG_RAD,user2)
    
    
def e_pi_function(user2):

    if user2 =="e":
        print(f"{colors['bright_green']}Result: {colors['reset']}",round(math.e,2))
        otherfunction(Value=1,DEG_RAD=1,user2=1)
        
        
    elif user2=="pi":
        print(f"{colors['bright_green']}Result: {colors['reset']}", round(math.pi,2))
        otherfunction(Value=1,DEG_RAD=1,user2=1)
    
    
        
        
    

def calculations(Value,DEG_RAD,user2):
    
          if user2 == "sin" or user2== "csc":
              sinfunction(Value,DEG_RAD,user2)
              
          elif  user2 == "cos" or user2=="sec":
              cosfunction(Value,DEG_RAD,user2)
             
          elif  user2 == "tan" or user2=="cot": 
              tanfunction(Value,DEG_RAD,user2)
              
          
          
          elif user2 == "arcsin" or user2=="arccsc":
              arcsinfunction(Value,DEG_RAD,user2)
           
          elif  user2 == "arccos" or user2=="arcsec":
              arccosfunction(Value,DEG_RAD,user2)
           
          elif  user2 == "arctan" or user2=="arccot": 
              arctanfunction(Value,DEG_RAD,user2)
           
          
          elif user2 == "sinh" or user2== "csch":
              sinhfunction(Value,DEG_RAD,user2)
          
          elif  user2 == "cosh" or user2=="sech":
              coshfunction(Value,DEG_RAD,user2)
            
          elif  user2 == "tanh" or user2=="coth":
              tanhfunction(Value,DEG_RAD,user2)
              
          elif  user2 == "log10":
              log_function(Value,DEG_RAD,user2)
        
          elif user2== "ln":
              ln_function(Value,DEG_RAD,user2)
                  
          elif user2 == "factorial":
              i_function(Value, DEG_RAD, user2)
              
          elif user2=="exp":
              exp_function(Value, DEG_RAD, user2)
          elif user2=="e" or user2=="pi":
              e_pi_function(user2)
              
         
        
          else:
              user2=input(f"{colors['bright_red']}the name of function invild try again {colors['reset']}")
          return          
              
              

def scientific():
      Value=0
      DEG_RAD=0

      print()
      hf.print_welcome_message("there are specific functions that perform only a specific task",
                               f"{colors['bright_yellow']}Scientific-Mode{colors['reset']}")

      print(
      f"{colors['bright_cyan']}1.{colors['bright_white']} Trigonometric functions:\n"
      f"{colors['bright_cyan']}2.{colors['bright_white']} Inverse trigonometric functions:\n"
      f"{colors['bright_cyan']}3.{colors['bright_white']} Hyperbolic functions\n"
      f"{colors['bright_cyan']}4.{colors['bright_white']} logarthmic functions\n"
      f"{colors['bright_cyan']}5.{colors['bright_white']} other functions:\n"
      "----------------------------------------")
      
      user2 = input(f"{colors['cyan']}Enter the number of function "
                    f"({colors['bright_yellow']}'stop' {colors['cyan']}or {colors['bright_yellow']}'back'{colors['cyan']} if you want to end): {colors['reset']}")
      while True:
          if user2=="1":
              trifunction(Value,DEG_RAD,user2)
              break
          elif user2=="2":
              arcfunction(Value,DEG_RAD,user2)
              break
          elif user2=="3":
              hypfunction(Value,DEG_RAD,user2)
              break
          elif user2=="4":
              logfunction(Value,DEG_RAD,user2)
              break
          elif user2=="5":
              otherfunction(Value,DEG_RAD,user2)
              break
          elif user2 in ("exit","stop","end","back","return","leave"):
              print(colors['bright_yellow'] + colors['bold'] + "\n**Exiting Scientific Mode... Goodbye!**\n" + colors['reset'])
              hf.return_main_menu()
          else:
              user2=input(f"{colors['bright_red']}invild name.. {colors['cyan']}please Enter the function or stop: {colors['reset']}")
      
def trifunction(Value,DEG_RAD,user2):
    print()
    hf.print_welcome_message("Functions that use angles to find relationships between the sides of a triangle","Trigonometric")
    print(
      "\n"
      f"{colors['bold']}1- Sin  2- Cos  3- Tan"
      f"\n4- Csc  5- Sec  6- Cot\n{colors['reset']}"
      "----------------------------------------")
    user2= input(f"{colors['cyan']}\nChoose Function or "
                      f"({colors['bright_yellow']}'stop'{colors['cyan']} or {colors['bright_yellow']}back{colors['cyan']}): {colors['reset']}")
    while True:
        if user2=="1":
            user2="sin"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="2":
            user2="cos"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="3":
            user2="tan"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="4":
            user2="csc"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="5":
            user2="sec"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="6":
            user2="cot"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2 in ("back","return","leave"):
            scientific()
            break
        elif user2 in ("stop","exit","end"):
            hf.return_main_menu()
        else:
            user2=input(f"{colors['bright_red']}\nThe entry is invalid {colors['blue']} please try again: {colors['reset']}")
        
def arcfunction(Value,DEG_RAD,user2):
    print()
    hf.print_welcome_message("These give you the angle when you already know the trigonometric value","Inverse trigonometric")
    print(
      "\n"
      f"{colors['bold']}1- ArcSin  2- ArcCos  3- ArcTan"
      f"\n4- ArcCsc  5- ArcSec  6- ArcCot\n{colors['reset']}"
      "----------------------------------------")

    user2= input(f"{colors['cyan']}\nChoose Function or "
                      f"({colors['bright_yellow']}'stop'{colors['cyan']} or {colors['bright_yellow']}back{colors['cyan']}): {colors['reset']}")
    while True:
        if user2=="1":
            user2="arcsin"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="2":
            user2="arccos"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="3":
            user2="arctan"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="4":
            user2="arccsc"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="5":
            user2="arcsec"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="6":
            user2="arccot"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2 in ("back","return","leave"):
            scientific()
        elif user2 in ("stop","exit","end"):
            hf.return_main_menu()
        else:
            user2=input(f"{colors['bright_red']}The entry is invalid! {colors['cyan']}please try again: {colors['reset']}")
            
def hypfunction(Value,DEG_RAD,user2):
    print()
    hf.print_welcome_message("Similar to trigonometric functions but based on exponential equations","Hyperbolic")
    print(
      "\n"
      f"{colors['bold']}1- Sinh  2- Cosh  3- Tanh"
      f"\n4- Csch  5- Sech  6- Coth\n{colors['reset']}"
      "----------------------------------------")
    
    user2= input(f"{colors['cyan']}\nChoose Function or "
                      f"({colors['bright_yellow']}'stop'{colors['cyan']} or {colors['bright_yellow']}back{colors['cyan']}): {colors['reset']}")
    while True:
        if user2=="1":
            user2="sinh"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="2":
            user2="cosh"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="3":
            user2="tanh"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="4":
            user2="csch"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="5":
            user2="sech"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="6":
            user2="coth"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2 in ("back","return","leave"):
            scientific()
            break
        elif user2 in ("stop","exit","end"):
            hf.return_main_menu()
        else:
            user2=input(f"{colors['bright_red']}The entry is invalid! {colors['cyan']}please try again: {colors['reset']}")
            
            
def logfunction(Value,DEG_RAD,user2):
    print()
    hf.print_welcome_message("Used to find the power or exponent of a number","logarthmic")
    print(
      "\n"
      f"{colors['bold']}1- log10  2- ln\n{colors['reset']}"
      "----------------------------------------")

    user2= input(f"{colors['cyan']}\nChoose Function or "
                      f"({colors['bright_yellow']}'stop'{colors['cyan']} or {colors['bright_yellow']}back{colors['cyan']}): {colors['reset']}")
    while True:
        if user2=="1":
            user2="log10"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="2":
            user2="ln"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2 in ("back","return","leave"):
            scientific()
            break
        elif user2 in ("stop","exit","end"):
            hf.return_main_menu()
        else:
            user2=input(f"{colors['bright_red']}The entry is invalid! {colors['cyan']}please try again: {colors['reset']}")
            
            
def otherfunction(Value,DEG_RAD,user2):
    print()
    hf.print_welcome_message("Basic math functions like square root, absolute value, exponent, factorial, e, and π","other")
    print(
      "\n"
      f"{colors['bold']}1- factorial  2- exp  3- e   4- pi\n{colors['reset']}"
      "----------------------------------------")

    user2= input(f"{colors['cyan']}\nChoose Function or "
                      f"({colors['bright_yellow']}'stop'{colors['cyan']} or {colors['bright_yellow']}back{colors['cyan']}): {colors['reset']}")
    while True:
        if user2=="1":
            user2="factorial"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="2":
            user2="exp"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="3":
            user2="e"
            calculations(Value,DEG_RAD,user2)
            break
        elif user2=="4":
            user2="pi"
            calculations(Value,DEG_RAD,user2)
            break
        elif user2 in ("back","return","leave"):
            scientific()
            break
        elif user2 in ("stop","exit","end"):
            hf.return_main_menu()
        else:
            user2=input(f"{colors['bright_red']}\nThe entry is invalid {colors['cyan']}please try again: {colors['reset']}")
            
            
def DEG_RAD1(Value,DEG_RAD,user2):
    if user2=="log10" or user2=="ln"or user2=="factorial" or user2=="exp" or user2 =="sinh" or user2=="cosh" or user2=="tanh" or user2=="csch" or user2=="sech" or user2=="coth":
        Value1(Value,DEG_RAD,user2)
        
    else:
        
        DEG_RAD=input(f"{colors['cyan']}\nEnter {colors['bright_yellow']}1 to degrees or 2 to radians{colors['cyan']} or "
                      f"({colors['bright_yellow']}'stop'{colors['cyan']} or {colors['bright_yellow']}back{colors['cyan']}): {colors['reset']}")
        
        while True:
            if DEG_RAD=="1":
               DEG_RAD="degrees"
            elif DEG_RAD=="2":
               DEG_RAD="radians"
            if DEG_RAD == "degrees" or DEG_RAD=="radians" \
            or DEG_RAD=="stop" or DEG_RAD in ("back","return","leave"):

               break
            else:
                DEG_RAD=input(f"{colors['bright_red']}Invild.. {colors['cyan']}please select 1 for degrees and 2 for radians or (stop or back): {colors['reset']}")
    if DEG_RAD in ("stop","exit","end"):
        hf.return_main_menu()
          
    elif DEG_RAD in ("back","return","leave"):
        if user2=="sin"or user2=="cos" or user2=="tan" or user2=="csc" or user2=="sec"or user2=="cot":
            trifunction(Value,DEG_RAD,user2)
        elif user2=="arcsin" or user2=="arccos" or user2=="arctan" or user2 == "arccsc" or user2 =="arcsec" or user2 =="arccot":
            arcfunction(Value,DEG_RAD,user2)
    else:
        Value1(Value,DEG_RAD,user2)
        
    return

def Value1(Value,DEG_RAD,user2):

    while True:
        Value = input(f"{colors['cyan']}\nEnter value or "
                      f"({colors['bright_yellow']}'stop'{colors['cyan']} or {colors['bright_yellow']}back{colors['cyan']}): {colors['reset']}")

        if Value in ("stop","exit","end"):
            hf.return_main_menu()
    
            
        elif Value in ("back","return","leave") and (user2 in ("sinh", "cosh", "tanh", "csch", "sech","coth")):
            hypfunction(Value,DEG_RAD,user2)
        elif Value in ("back","return","leave") and (user2=="log10" or user2=="ln"):
            logfunction(Value,DEG_RAD,user2)
        elif Value in ("back","return","leave") and (user2=="factorial" or user2=="exp"):
            otherfunction(Value,DEG_RAD,user2)
        elif Value in ("back","return","leave"):
            DEG_RAD1(Value, DEG_RAD, user2)
        else:
            try:
                Value = float(Value)
                calculations(Value, DEG_RAD, user2)
                hf.return_main_menu()
            
            except ValueError:
                print(f"{colors['bright_red']}Invalid number please enter again{colors['reset']}")


