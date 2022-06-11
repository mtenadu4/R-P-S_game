import random

game_list = ["R", "P", "S"]
user_action = input("Enter a choice(R, P, S): ")
possible_actions = ["R", "P", "S"]
computer_action = random.choice(possible_actions)
print(f"\nPlayer {user_action}, CPU {computer_action}.\n")

if user_action == computer_action:
    print("the computer and player picked the same move")
elif user_action == "R":
    if computer_action == "S":
        print("Player wins")
    else:
        print("CPU wins")
elif user_action == "P":
    if computer_action == "R":
        print("Player wins")
    else:
        print("CPU wins")
elif user_action == "S":
    if computer_action == "P":
        print("Player wins")
    else:
        print("CPU wins")

if(user_action not in possible_actions):
    print("data not found")
