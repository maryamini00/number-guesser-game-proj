from input_validator import exit_program
def first_score_print():
    print("your first score: 100 :)")
    print("1 point is deducted from your score for every incorrect guess, \nand you earn 5 points for every correct guess \n(correct guess means the exact number selected by the computer).")
def print_score(s):
    print("your score is: ", s)
def decrease_score(s):
    if s > 1:
        if s < 10:
            print("oh, be carefull your score is less than 10 \nbut don't scare you can do it :)")
        else:
            return s-1
    elif s == 1:
        print("you lost \nI hope you win next time :)")
        exit_program()
    else:
        print("erorr...")
        exit_program()
def increase_score(s):
    print("excelent \nthat was right :) \n")
    return s+5