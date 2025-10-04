import math
def sinfunction(Value, DEG_RAD, user2):
    if user2 == "csc":
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        if Value == 0:
            print("Value cannot 0 for csc")
            Value1(Value, DEG_RAD, user2)
            return
        sin_csc = 1 / math.sin(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        sin_csc = math.sin(Value)
    print("Result:", sin_csc)
    return

def cosfunction(Value, DEG_RAD, user2):
    if user2 == "sec":
        Value0 = Value if DEG_RAD == "degrees" else math.degrees(Value)
        if Value0 % 180 == 90:
            print("Value not vild for sec")
            Value1(Value, DEG_RAD, user2)
            return
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        cos_sec = 1 / math.cos(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        cos_sec = math.cos(Value)
    print("Result:", cos_sec)
    return

def tanfunction(Value, DEG_RAD, user2):
    if user2 == "cot":
        Value0 = Value if DEG_RAD == "degrees" else math.degrees(Value)
        if Value0 % 180 == 0 :
            print("Value not vild for cot")
            Value1(Value, DEG_RAD, user2)
            return
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        tan_cot = 1 / math.tan(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        tan_cot = math.tan(Value)
    print("Result:", tan_cot)
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
    print("Result:", result)
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
    print("Result:", result)
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
    print("Result:", result,)
    return



def sinhfunction(Value, DEG_RAD, user2):
    if user2 == "csch":
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        if Value == 0:
            print("Value cannot be 0 for csch")
            Value1(Value, DEG_RAD, user2)
            return
        result = 1 / math.sinh(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        result = math.sinh(Value)

    print("Result:", result)
    return


def coshfunction(Value, DEG_RAD, user2):
    if user2 == "sech":
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        result = 1 / math.cosh(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        result = math.cosh(Value)

    print("Result:", result)
    return


def tanhfunction(Value, DEG_RAD, user2):
    if user2 == "coth":
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        if Value == 0:
            print("Value cannot be 0 for coth")
            Value1(Value, DEG_RAD, user2)
            return
        result = 1 / math.tanh(Value)
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        result = math.tanh(Value)

    print("Result:", result)
    return



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
         
        
          else:
              user2=input("the name of function invild try again ")
          return          
              
              

    





def scientific_mode():
      Value=0
      DEG_RAD=0
      print("sin,cos,tan,csc,sec,cot,\n" 
      "arcsin,arccos,arctan,arccsc,arcsec,arccot\n"
      "sinh,cosh,tanh,csch,sech,coth\nstop")
      user2 = input("Enter the function or stop if you wand end: ").lower()
      while True:
          if (user2=="sin"or user2=="cos" or user2=="tan" or user2=="csc" or user2=="sec"or user2=="cot"
          or user2=="arcsin" or user2=="arccos" or user2=="arctan" or user2 == "arccsc" or user2 =="arcsec"
          or user2=="arccot" or user2=="sinh" or user2=="cosh" or user2=="tanh" or user2=="csch" 
          or user2== "sech" or user2=="coth"):
              DEG_RAD1(Value,DEG_RAD,user2)
              break
          else:
              user2=input("invild name pleas Enter the function or stop if you wand end:: ").lower()
      if user2=="stop":
          exit()
      return  
      
      
def DEG_RAD1(Value,DEG_RAD,user2):
      DEG_RAD=input("degrees or radians or stop if you wand end or back:: ").lower()
      while True:
          if DEG_RAD == "degrees" or DEG_RAD=="radians" or DEG_RAD=="stop" or DEG_RAD=="back":

             break
          else:
              DEG_RAD=input("invild please choce degrees or radians: or stop or back: ").lower()
      if DEG_RAD=="stop":
          exit()
          
      elif DEG_RAD=="back":
          scientific_mode()
          return
      else:
          Value1(Value,DEG_RAD,user2)
      return
def Value1(Value,DEG_RAD,user2):

    while True:
        Value = input("Enter value or 'stop' to end or back: ").lower()

        if Value == "stop":
            exit()
        elif Value == "back":
            DEG_RAD1(Value, DEG_RAD, user2)
            return
        else:
            try:
                Value = float(Value)
                calculations(Value, DEG_RAD, user2)
                return
            except ValueError:
                print("Invalid number please enter again")

        

scientific_mode()        
    
        
    

       
     
    
