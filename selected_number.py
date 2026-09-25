import random
def select_random_number():
    check = True
    while check:
        i = random.randint(0, 100)
        if i >= 0 and i <= 100:
            check = False
    return i