import random
def select_random_number():
    while True:
        i = random.randint(1, 100)
        if i >= 1 and i <= 100:
            break
    return i