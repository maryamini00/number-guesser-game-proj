def take_input():
    i = input("\nyour input (it has to be between 1 and 100): ")
    return i
def exit_program(s):
    print("Well, well...\nyour latest score was ", s ," :)")
    print("come back later and let's play together again.")
    print("I'll be waiting for you.")
    print("\nexiting the program...")
    exit()
def validate_type_input(s):
    while True:
        i = take_input()
        if isinstance(i, int):
            return validate_range_input(i)
        elif isinstance(i, float):
            print("This is a decimal number. Enter a whole number :)")
        elif isinstance(i, str):
            if i.lower() in ("e", "exit"):
                exit_program(s)
            elif i.isdigit():
                i = int(i)
                return validate_range_input(i)
            else:
                print("Enter only a number in numeric format :)")
        else:
            print("what was that? Please enter a number :) \ntry again...")
def validate_range_input(i):
    while True:
        if i < 1:
            print("oh i said input a number between 1 and 100, it's less than 1 :( \ntry again...")
            i = validate_type_input()
        elif i > 100:
            print("oh i said input a number between 1 and 100, it's less than 1 :( \ntry again...")
            i = validate_type_input()
        else:
            #corrct ans
            break
    return i
def start_input(s):
    while True:
        i = input("\nyour input: ")
        if i == "E" or i == "e" or i == "Exit" or i == "exit":
            exit_program(s)
        elif i == "P" or i == "p" or i == "Play" or i == "play":
            break
        else:
            print("this input is invalid")
            print("try again :)")