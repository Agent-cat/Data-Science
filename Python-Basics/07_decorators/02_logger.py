from functools import wraps


# it is used to keep the same metadata of fnc even in wrapper fnc
def logger(fnc):
    @wraps(fnc)
    def wrapper(*args,**kwargs): 
        # taking arguments to wrapper and passing to function
       print(f"Calling {fnc.__name__}")
       result=fnc(*args,**kwargs)
       return result
    return wrapper
@logger
def brew_chat(type):
   print(f"Brewing {type}")  
brew_chat("choco")
