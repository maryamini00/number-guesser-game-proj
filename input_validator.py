def take_input():
    i = input("\nyour input (it has to be between 0 and 100): ")
    return i
def exit_program():
    print("\nexiting the program...")
    exit()
def validate_type_input():
    check = True
    while check:
        i = take_input()
        if isinstance(i, int):
            return validate_range_input(i)
        elif isinstance(i, float):
            print("This is a decimal number. Enter a whole number :)")
        elif isinstance(i, str):
            if i.lower() in ("e", "exit"):
                exit_program()
            elif i.isdigit():
                i = int(i)
                return validate_range_input(i)
            else:
                print("Enter only a number in numeric format :)")
        else:
            print("what was that? Please enter a number :) \ntry again...")
        
        
        
        # if i == "E" or i == "e" or i == "Exit" or i == "exit":
        #     exit_program()
        # else:
            
        # if type(i) == int:
        #     #corrct ans
        #     validate_range_input(i)
        #     return i
        # elif type(i) == float:
        #     print("this is a decimal number, please enter a whole number :) \ntry again...")
        # elif type(i) == str:
        #     if i == "E" or i == "e" or i == "Exit" or i == "exit":
        #         exit_program()
        #     else:
        #         print("enter only the number in numeric format :) \nIf you want to exit the program, type exit, 'E', or 'e' \ntry again...")
        # else:
        #     print("what was that? Please enter a number :) \ntry again...")
def validate_range_input(i):
    check = True
    while check:
        if i < 0:
            print("oh i said input a number between 0 and 100, it's less than 0 :( \ntry again...")
            i = validate_type_input()
        elif i > 100:
            print("oh i said input a number between 0 and 100, it's less than 0 :( \ntry again...")
            i = validate_type_input()
        else:
            #corrct ans
            check = False
    return i
def start_input():
    check = True
    while check:
        i = input("\nyour input: ")
        if i == "E" or i == "e" or i == "Exit" or i == "exit":
            exit_program()
        elif i == "P" or i == "p" or i == "Play" or i == "play":
            check = False
        else:
            print("this input is invalid")
            print("try again :)")