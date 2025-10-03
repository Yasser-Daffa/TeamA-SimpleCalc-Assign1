import math
def sinfunction(Value,DEG_RAD,user2):
    if user2 == "csc":
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        sin_csc= (math.sin(Value))**-1
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        sin_csc= math.sin(Value)
    print("Result: ",sin_csc)
    return

def cosfunction(Value,DEG_RAD,user2):
    if user2 == "sec":
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        cos_sec= (math.cos(Value))**-1
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        cos_sec= math.cos(Value)
    print("Result: ",cos_sec)
    return

def tanfunction(Value,DEG_RAD,user2):
    if user2 == "cot":
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        tan_cot= (math.tan(Value))**-1
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        tan_cot= math.tan(Value)
    print("Result: ",tan_cot)
    return





def arcsinfunction(Value,DEG_RAD,user2):
    if user2 == "arccsc":
        sin_csc= (math.asin(Value))**-1
    else:
      
        sin_csc= math.asin(Value)
    print("Result: ",sin_csc)
    return

def arccosfunction(Value,DEG_RAD,user2):
    if user2 == "arcsec":
        cos_sec= (math.acos(Value))**-1
    else:
        cos_sec= math.acos(Value)
    print("Result: ",cos_sec)
    return

def arctanfunction(Value,DEG_RAD,user2):
    if user2 == "arccot":
        tan_cot= (math.atan(Value))**-1
    else:
        tan_cot= math.atan(Value)
    print("Result: ",tan_cot)
    return




def sinhfunction(Value,DEG_RAD,user2):
    if user2 == "csch":
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        sinh_csch= (math.sinh(Value))**-1
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
        sinh_csch= math.sinh(Value)
    print("Result: ",sinh_csch)
    return

def coshfunction(Value,DEG_RAD,user2):
    if user2 == "sech":
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
           
        cosh_sech= (math.cosh(Value))**-1
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
           
        cosh_sech= math.cosh(Value)
    print("Result: ",cosh_sech)
    return

def tanhfunction(Value,DEG_RAD,user2):
    if user2 == "coth":
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
          
        tanh_coth= (math.tanh(Value))**-1
    else:
        if DEG_RAD == "degrees":
            Value = math.radians(Value)
            
        tanh_coth= math.tanh(Value)
    print("Result: ",tanh_coth)
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
              
              

    





def scientific_menu():
    while True:
      print("sin\ncos\ntan\ncsc\nsec\ncot\narcsin\narccos\narctan\narccsc\narcsec\narccot\n
      sinh\ncosh\ntanh\ncsch\nsech\ncoth\nstop\n")    
      user2 = input("Enter the function: ").lower()
      while True:
          if (user2=="sin"or user2=="cos" or user2=="tan" or user2=="csc" or user2=="sec"or user2=="cot"
          or user2=="arcsin" or user2=="arccos" or user2=="arctan" or user2 == "arccsc" or user2 =="arcsec"
          or user2=="arccot" or user2=="sinh" or user2=="cosh" or user2=="tanh" or user2=="csch" 
          or user2== "sech" or user2=="coth" or user2=="stop"):
              break
          else:
              user2=input("invild name pleas Enter the function: ").lower()
      if user2=="stop":
          break
      
      

      DEG_RAD=input("degrees or radians: ").lower()
      while True:
          if DEG_RAD == "degrees" or DEG_RAD=="radians":
             break
          else:
              DEG_RAD=input("invild please choce degrees or radians: ").lower()
    
      while True:
           Value = input("Enter value: ")
           try:
               Value = float(Value)
               break
           except:
               print("invalid number, please enter again")


      calculations(Value,DEG_RAD,user2)          
    return  
scientific_menu()        
    
        
    

       
     
    

