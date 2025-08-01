type=input("Enter the value : ").lower()

match type:
    case "sleeper":
        print("It is a sleeper")
    case "ac":
        print("It is ac") 
    case _:
        print("Invalid type")    
