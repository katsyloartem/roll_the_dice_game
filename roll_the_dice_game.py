from random import randint
roll_count = 0
dice_rolls = (1)
while True:
    print(f"Roll Count is: {roll_count}")
    game_goes = input("Roll the dice (y/n) ")
    if game_goes.lower() == "y":
        amount_dice = input("How many dices do you want to roll? ")
        if amount_dice.isdigit() and int(amount_dice) != 0:
            dice_rolls = int(amount_dice)
            for i in range(dice_rolls):
                first = randint(1, 6)
                second = randint(1, 6)
                print((first, second))
            roll_count += 1
        else:
            print("You have to type a number")
    elif game_goes.lower() == "n":
        print(f"Thanks for playing! Your roll count is {roll_count}")
        break

    else:
        print("That's weird, that is not an option. Choose out of the existing options")
        continue
