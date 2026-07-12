import random

num_dice = int(input("How many dies do you want to roll? "))
roll_count = 0
while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        roll_count += 1
        dice = []
        
        for _ in range(num_dice):
            dice.append(random.randint(1, 6))
        print(dice)
        print("Total:", sum(dice))
    elif choice == 'n':
        print(f"\nThanks for playing!")
        print(f"Total rolls: {roll_count}")
        break
    else:
        print("Invalid choice")
    