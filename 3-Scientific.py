import math
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
    print("Result:", round(sin_csc,2),)
    Value1(Value,DEG_RAD,user2)
    return

def cosfunction(Value, DEG_RAD, user2):
    if user2 == "sec":
        Value0 = Value if DEG_RAD == "degrees" else math.degrees(Value)
        if Value0 % 180 == 90:
            print("Value not valid for sec (cos=0)")
            Value1(Value, DEG_RAD, user2)
            return
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        cos_sec = 1 / math.cos(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        cos_sec = math.cos(Value)
    print("Result:", round(cos_sec,2))
    Value1(Value,DEG_RAD,user2)
    return

def tanfunction(Value, DEG_RAD, user2):
    if user2 == "cot":
        Value0 = Value if DEG_RAD == "degrees" else math.degrees(Value)
        if Value0 % 180 == 0 :
            print("Value not valid for cot (tan=0)")
            Value1(Value, DEG_RAD, user2)
            return
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        tan_cot = 1 / math.tan(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        tan_cot = math.tan(Value)
    print("Result:", round(tan_cot,2))
    Value1(Value,DEG_RAD,user2)
    return










def arcsinfunction(Value, DEG_RAD, user2):
    if user2 == "arccsc":
        if Value == 0:
            print("Value cannot be 0 for arccsc")
            Value1(Value, DEG_RAD, user2)
            return
        result = math.asin(1 / Value)
    else:
        if -1 <= Value <= 1:
            result = math.asin(Value)
        else:
            print("The number must be between -1 and 1")
            Value1(Value, DEG_RAD, user2)
            return

    if DEG_RAD == "degrees":
        result = math.degrees(result)
    print("Result:", round(result,2))
    Value1(Value,DEG_RAD,user2)
    return


def arccosfunction(Value, DEG_RAD, user2):
    if user2 == "arcsec":
        if Value == 0:
            print("Value cannot be 0 for arcsec")
            Value1(Value, DEG_RAD, user2)
            return
        result = math.acos(1 / Value)
    else:
        if -1 <= Value <= 1:
            result = math.acos(Value)
        else:
            print("The number must be between -1 and 1")
            Value1(Value, DEG_RAD, user2)
            return

    if DEG_RAD == "degrees":
        result = math.degrees(result)
    print("Result:", round(result,2))
    Value1(Value,DEG_RAD,user2)
    return


def arctanfunction(Value, DEG_RAD, user2):
    if user2 == "arccot":
        if Value == 0:
            print("Value cannot be 0 for arccot")
            Value1(Value, DEG_RAD, user2)
            return
        result = math.atan(1 / Value)
    else:
        result = math.atan(Value)

    if DEG_RAD == "degrees":
        result = math.degrees(result)
    print("Result:", round(result,2))
    Value1(Value,DEG_RAD,user2)
    return










def sinhfunction(Value, DEG_RAD, user2):
    if user2 == "csch":
        
        if Value == 0:
            print("Value cannot be 0 for csch")
            Value1(Value, DEG_RAD, user2)
            return
        result = 1 / math.sinh(Value)
    else:
       
        result = math.sinh(Value)

    print("Result:", result)
    Value1(Value,DEG_RAD,user2)
    return


def coshfunction(Value, DEG_RAD, user2):
    if user2 == "sech":
        
        result = 1 / math.cosh(Value)
    else:
       
        result = math.cosh(Value)

    print("Result:", result)
    Value1(Value,DEG_RAD,user2)
    return


def tanhfunction(Value, DEG_RAD, user2):
    if user2 == "coth":
        
        if Value == 0:
            print("Value cannot be 0 for coth")
            Value1(Value, DEG_RAD, user2)
            return
        result = 1 / math.tanh(Value)
    else:
       
        result = math.tanh(Value)

    print("Result:", round(result,2))
    Value1(Value,DEG_RAD,user2)








def log_function(Value, DEG_RAD, user2):
     if Value <= 0:
        print("the number must be > 0 try again")
        Value1(Value,DEG_RAD,user2)
        return
     else:
        Value= math.log10(Value)
        print("result: ",round(Value,2))
        Value1(Value,DEG_RAD,user2)
        
def ln_function(Value, DEG_RAD, user2):
     if Value <= 0:
        print("the number must be > 0 try again")
        Value1(Value,DEG_RAD,user2)
        return
     else:
        Value= math.log(Value)
        print("result: ",round(Value,2))
        Value1(Value,DEG_RAD,user2)

def i_function(Value, DEG_RAD, user2):
     if Value < 0 or not float(Value).is_integer():
        print("the number must be > 0 and  not float try again")
        Value1(Value,DEG_RAD,user2)
        return
     else:
        Value= math.factorial(Value)
        print("result: ",round(Value,2))
        Value1(Value,DEG_RAD,user2)
        
def exp_function(Value, DEG_RAD, user2):
    print("result: ",round(math.exp(Value),2))
    Value1(Value,DEG_RAD,user2)
    
    
def e_pi_function(user2):
    if user2 =="e":
        print("result: ",round(math.e,2))
        
    elif user2=="pi":
        print("result", round(math.pi,2))
        
    






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
              user2=input("the name of function invild try again ")
          return          
              
              

    





def scientific_mode():
      Value=0
      DEG_RAD=0
      
      print("--Welcome to scientific_mode--\n"
      "--Here there are specific functions that perform only a specific task--\n"
      "-----------------------------------------------------------------------\n"
      "1- Trigonometric functions:\n"
      "2- Inverse trigonometric functions:\n"
      "3- Hyperbolic functions\n"
      "4- logarthmic functions\n"
      "5- other functions:\n"
      "-----------------------------------------------------------------------")
      
      user2 = input("Enter the number of function or stop if you want end or back: ")
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
          elif user2=="stop":
              exit()
          elif user2=="back":
              main_menu()
          else:
              user2=input("invild name pleas Enter the function or stop: ")
      
def trifunction(Value,DEG_RAD,user2):
    print("\n\n\n--Welcome to Trigonometric functions--\n"
      "--Functions that use angles to find relationships between the sides of a triangle--\n"
      "-----------------------------------------------------------------------\n"
      "1- sin  2- cos  3- tan  4- csc  5- sec  6- cot\n"
      "-----------------------------------------------------------------------")
    user2= input("please enter the number of function or stop or back:")
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
        elif user2=="back":
            scientific_mode()
            break
        elif user2=="stop":
            exit()
        else:
            user2=input("The entry is invalid please try again: ")
        
def arcfunction(Value,DEG_RAD,user2):
    print("\n\n\n--Welcome to Inverse trigonometric functions--\n"
      "--These give you the angle when you already know the trigonometric value--\n"
      "-----------------------------------------------------------------------\n"
      "1- arcsin  2- arccos  3- arctan  4- arccsc  5- arcsec  6- arccot\n"
      "-----------------------------------------------------------------------")
    user2= input("please enter the number of function or stop or back: ")
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
        elif user2=="back":
            scientific_mode()
        elif user2=="stop":
            exit()
        else:
            user2=input("The entry is invalid please try again: ")
            
def hypfunction(Value,DEG_RAD,user2):
    print("\n\n\n--Welcome to Hyperbolic functions--\n"
      "--Similar to trigonometric functions but based on exponential equations--\n"
      "-----------------------------------------------------------------------\n"
      "1- sinh  2- cosh  3- tanh  4- csch  5- sech  6- coth\n"
      "-----------------------------------------------------------------------")
    user2= input("please enter the number of function or stop or back: ")
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
        elif user2=="back":
            scientific_mode()
            break
        elif user2=="stop":
            exit()
        else:
            user2=input("The entry is invalid please try again: ")
            
            
def logfunction(Value,DEG_RAD,user2):
    print("\n\n\n--Welcome to logarthmic functions--\n"
      "--Used to find the power or exponent of a number--\n"
      "-----------------------------------------------------------------------\n"
      "1- log10  2- ln\n"
      "-----------------------------------------------------------------------")
    user2= input("please enter the number of function or stop or back: ")
    while True:
        if user2=="1":
            user2="log10"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="2":
            user2="ln"
            DEG_RAD1(Value,DEG_RAD,user2)
            break
        elif user2=="back":
            scientific_mode()
            break
        elif user2=="stop":
            exit()
        else:
            user2=input("The entry is invalid please try again: ")
            
            
def otherfunction(Value,DEG_RAD,user2):
    print("\n\n\n--Welcome to other functions--\n"
      "--Basic math functions like square root, absolute value, exponent, factorial, e, and π--\n"
      "-----------------------------------------------------------------------\n"
      "1- factorial  2- exp  3- e   4- pi\n"
      "-----------------------------------------------------------------------")
    user2= input("please enter the number of function or stop or back: ")
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
        elif user2=="back":
            scientific_mode()
            break
        elif user2=="stop":
            exit()
        else:
            user2=input("The entry is invalid please try again: ")
            
            
def DEG_RAD1(Value,DEG_RAD,user2):
    if user2=="log10" or user2=="ln"or user2=="factorial" or user2=="exp" or user2 =="sinh" or user2=="cosh" or user2=="tanh" or user2=="csch" or user2=="sech" or user2=="coth":
        Value1(Value,DEG_RAD,user2)
        
    else:
        
        DEG_RAD=input("\n\n\ndegrees or radians or stop or back:: ").lower()
        while True:
            if DEG_RAD == "degrees" or DEG_RAD=="radians" or DEG_RAD=="stop" or DEG_RAD=="back":

               break
            else:
                DEG_RAD=input("invild please choce degrees or radians: or stop or back: ").lower()
    if DEG_RAD=="stop":
        exit()
          
    elif DEG_RAD=="back":
        if user2=="sin"or user2=="cos" or user2=="tan" or user2=="csc" or user2=="sec"or user2=="cot":
            trifunction(Value,DEG_RAD,user2)
        elif user2=="arcsin" or user2=="arccos" or user2=="arctan" or user2 == "arccsc" or user2 =="arcsec":
            arcfunction(Value,DEG_RAD,user2)
    else:
        Value1(Value,DEG_RAD,user2)
        
    return

def Value1(Value,DEG_RAD,user2):

    while True:
        Value = input("\n\n\nEnter value or stop or back: ")

        if Value == "stop":
            exit()
    
            
        elif Value=="back" and (user2 =="sinh" or user2=="cosh" or user2=="tanh" or user2=="csch" or user2=="sech" or user2=="coth"):
            hypfunction(Value,DEG_RAD,user2)
        elif Value=="back" and (user2=="log10" or user2=="ln"):
            logfunction(Value,DEG_RAD,user2)
        elif Value=="back" and (user2=="factorial" or user2=="exp"):
            otherfunction(Value,DEG_RAD,user2)
        elif Value == "back":
            DEG_RAD1(Value, DEG_RAD, user2)
        else:
            try:
                Value = float(Value)
                calculations(Value, DEG_RAD, user2)
                exit()
            
            except ValueError:
                print("Invalid number please enter again")

        

scientific_mode()        
    
        
