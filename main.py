from input_validator import validate_type_input, start_input
from selected_number import select_random_number
import score_handling as sh
selected_number = -1
last_num = -1
new_num = -1
score = 100
print("-------------------------")
print("|                       |")
print("|  Number Guesser Game  |")
print("|                       |")
print("-------------------------")
print("\n")
sh.first_score_print()
while score > 0:
    selected_number = select_random_number()
    print("\n-------------------------\n")
    print("If you want to play, type play, 'P', or 'p'")
    print("If you want to exit the program, type exit, 'E', or 'e'\n")
    start_input()
    print("-------------------------")
    print("|                        |")
    print("|    The Game Started    |")
    print("|      let's go! :)      |")
    print("|                        |")
    print("-------------------------")
    check = True
    while check:
        new_num = validate_type_input()
        if new_num > selected_number:
            if last_num == -1:
                print("\nno, that wasn't right")
                print("hint: \nchoose a smaller number")
                print("try again :)\n")
                score = sh.decrease_score(score)
                sh.print_score(score)
                print("-------------------------")
                last_num = new_num
            elif new_num > last_num:
                print("\nno, that wasn't right")
                print("hint: \nchoose a smaller number")
                print("try again :)\n")
                score = sh.decrease_score(score)
                sh.print_score(score)
                print("-------------------------")
                last_num = new_num
            elif last_num > new_num:
                print("\nno, that wasn't right")
                print("but it was good continue, you can find it")
                print("hint: \nchoose a smaller number")
                print("try again :)\n")
                score = sh.decrease_score(score)
                sh.print_score(score)
                score = sh.decrease_score(score)
                sh.print_score(score)
                print("-------------------------")
                last_num = new_num
            else:
                print("Are you messing with me? \nWhy did you write the same number as before?") 
                print("try again :)\n")
                score = sh.decrease_score(score)
                sh.print_score(score)
                print("-------------------------")
        elif selected_number > new_num:
            if last_num == -1:
                print("\nno, that wasn't right")
                print("hint: \nchoose a larger number")
                print("try again :)\n")
                score = sh.decrease_score(score)
                sh.print_score(score)
                print("-------------------------")
                last_num = new_num
            elif new_num > last_num:
                print("\nno, that wasn't right")
                print("but it was good continue, you can find it")
                print("hint: \nchoose a larger number")
                print("try again :)\n")
                score = sh.decrease_score(score)
                sh.print_score(score)
                print("-------------------------")
                last_num = new_num
            elif last_num > new_num:
                print("\nno, that wasn't right")
                print("hint: \nchoose a larger number")
                print("try again :)\n")
                score = sh.decrease_score(score)
                sh.print_score(score)
                print("-------------------------")
                last_num = new_num
            else:
                print("Are you messing with me? \nWhy did you write the same number as before?") 
                print("try again :)\n")
                score = sh.decrease_score(score)
                sh.print_score(score)
                print("-------------------------")
        else:
            selected_number = -1
            last_num = -1
            new_num = -1
            print("Bravo!")
            print("you found it :)")
            score = sh.increase_score(score)
            sh.print_score(score)
            check = False
        



#Checking the last digit against the selected digit.