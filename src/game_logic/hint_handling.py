def hint_fault():
    return print("\nno, that wasn't right", "\ntry again :)\n")


def hint_smaller():
    return print("hint: \nchoose a smaller number\n")
def hint_similler():
    return print("Are you messing with me? \nWhy did you write the same number as before?")
def hint_larger():
    return print("hint: \nchoose a larger number")


def ignoring_smaller_hint(last_num):
    return print("i told you choose a smaller number than ", last_num, "\n")
def ignoring_larger_hint(last_num):
    return print("i told you choose a larger number than ", last_num, "\n")


def good_continue():
    return print("but it was good continue, you can find it")


def congratulation():
    return print("congratulation !\nyou found it :)")