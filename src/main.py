from utils.input_validator import validate_type_input, start_input
from game_logic.selected_number import select_random_number
import game_logic.score_handling as sh
import utils.titles_prints as p
import game_logic.hint_handling as h
def main():
    selected_number = -1
    last_num = -1
    new_num = -1
    score = 100
    p.game_title()
    sh.first_score_print()
    while score > 0:
        selected_number = select_random_number()
        print("\n-------------------------\n")
        p.play_or_exit()
        start_input(score)
        p.letsgo_title()
        while True:
            new_num = validate_type_input(score)
            if new_num > selected_number:
                if last_num == -1:
                    h.hint_fault()
                    h.hint_smaller()
                    score = sh.decrease_score(score)
                    sh.print_score(score)
                    print("-------------------------")
                    last_num = new_num
                elif new_num > last_num:
                    h.hint_fault()
                    if last_num > selected_number: 
                        h.ignoring_smaller_hint(last_num)
                    else:
                        h.hint_smaller()
                    score = sh.decrease_score(score)
                    sh.print_score(score)
                    print("-------------------------")
                    last_num = new_num
                elif last_num > new_num:
                    hint = 4
                    h.hint_fault()
                    h.good_continue()
                    h.hint_smaller()
                    score = sh.decrease_score(score)
                    sh.print_score(score)
                    print("-------------------------")
                    last_num = new_num
                else:
                    hint = 5
                    h.hint_fault()
                    h.hint_similler()
                    score = sh.decrease_score(score)
                    sh.print_score(score)
                    print("-------------------------")
            elif selected_number > new_num:
                if last_num == -1:
                    h.hint_fault()
                    h.hint_larger()
                    score = sh.decrease_score(score)
                    sh.print_score(score)
                    print("-------------------------")
                    last_num = new_num
                elif new_num > last_num:
                    h.hint_fault()
                    h.good_continue()
                    h.hint_larger()
                    score = sh.decrease_score(score)
                    sh.print_score(score)
                    print("-------------------------")
                    last_num = new_num
                elif last_num > new_num:
                    h.hint_fault()
                    if selected_number > last_num:
                        h.ignoring_larger_hint(last_num)
                    else:
                        h.hint_larger()
                    score = sh.decrease_score(score)
                    sh.print_score(score)
                    print("-------------------------")
                    last_num = new_num
                else:
                    h.hint_fault()
                    h.hint_similler()
                    score = sh.decrease_score(score)
                    sh.print_score(score)
                    print("-------------------------")
            else:
                h.congratulation()
                selected_number = -1
                last_num = -1
                new_num = -1
                score = sh.increase_score(score)
                sh.print_score(score)
                break
            
if __name__ == "__main__":
    main()