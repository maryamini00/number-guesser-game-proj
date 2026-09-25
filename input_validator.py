def take_input():
    print("\nyour input (it has to be between 0 and 100) :")
    i = input()
    return i
def exit_program(i):
    print("\nexiting the program...")
    exit()
def validate_type_input():
    i = take_input()
    check = True
    while check:
        if type(i) == int:
            #corrct ans
            validate_range_input(i)
            check = False
        elif type(i) == float:
            print("this is a decimal number, please enter a whole number :) \ntry again...")
            i = take_input()
        elif type(i) == str:
            if i == "E" or i == "e" or i == "Exit" or i == "exit":
                exit_program()
            else:
                print("enter only the number in numeric format :) \nif you want to finish the program inter (E) or (e) or write the full word Exit \ntry again...")
                i = take_input()
        else:
            print("what was that? Please enter a number :) \ntry again...")
            i = take_input()
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
            return i
            check = False
# def check_with_number(selected_number, next_number, i):
#     check = True
#     while check:
#         if next_number > selected_number:
#             if i > next_number:
#                 print("i told you it should be less than ", next_number, " \noh god, try again :)")
#                 validate_type_input()
#             else:
#                 check = False
#         else:
#             if i > next_number:
#                 check = False
#             else:
#                 print("i tolld you it should be less than ", next_number, " \noh god, try again :)")
#                 validate_type_input()
    
            

