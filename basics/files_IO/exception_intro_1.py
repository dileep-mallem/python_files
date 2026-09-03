# try : # Risky COde
#     x=int(input("Enter Numebr : "))
#     result =10/x 
#     s="a"+x 
# except ZeroDivisionError :
#     print("Number Cant be Zero ")
# except (ValueError , TypeError): # Multiple Combines
#     print("Wrong Type")
# except Exception as e : # Catch all Exceptions as other Exception
#     print(f"UnExxpected Error : {e}")
# else : # Runs Only if NO Exception Raises 
#     print(f"Success  Result :  {result}")
# finally:
#     print("This Always Excepcute")
# Only One Excpet Excecute ( Her for x=0 onlye ZeroDivEoor NOt Type Error )

# BaseException
# ├── Exception ← catch this, not BaseException
# │ ├── ValueError ← int("hello")
# │ ├── TypeError ← "a" + 1
# │ ├── IndexError ← lst[99] out of range
# │ ├── KeyError ← d["missing_key"]
# │ ├── AttributeError ← None.upper()
# │ ├── ZeroDivisionError ← n / 0
# │ ├── FileNotFoundError ← open("ghost.txt")
# │ ├── ImportError ← import nothing
# │ ├── StopIteration ← iterator exhausted
# │ └── YourCustomError ← defined by you (next section)
# └── KeyboardInterrupt ← Ctrl+C (don't catch this casually)

# Voter Exception 

def get_age():
    while True :
        try :
            age=int(input("Enter Age : "))
            if age < 0 :
                raise ValueError("Age Cant be -ve")
            return age 
        except ValueError as e:
            print(f"Inva;id : {e} . try Again")
get_age()

def divide(a,b):
    try :
        return a/b 
    except ZeroDivisionError :
        print("Caught It ! re-Raising ....")
        # raise  -> re-raise the Original Exception
divide(6,0)
