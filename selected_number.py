import random
def select_random_number():
    check = True
    while check:
        i = random.randint(1, 100)
        if i >= 1 and i <= 100:
            check = False
    return i