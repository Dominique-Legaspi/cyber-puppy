# Authors:  Thien Nguyen, Dominique Legaspi Dilag
# Date:     December 8, 2023
# Desc:     Puppy Simulator, feed and play with your new puppy

import puppy
from check_input import get_int_range

def main():
    pup = puppy.Puppy()
    print("Congratulations on your new puppy!")
    
    while True:
        choice = get_int_range("What would you like to do?\n1. Feed the puppy\n2. Play with the puppy\n3. Quit\nEnter choice: ", 1, 3)
        print()
        if choice == 1:
            print(pup.give_food())
        elif choice == 2:
            print(pup.throw_ball())
        elif choice == 3:
            break

main()