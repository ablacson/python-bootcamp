# # TODO: Ask the user for an input
# user_choice = input("Pick a choice (rock/paper/scissors): ")
#
# # TODO: Make a random choice for the computer
# # Note: Read the slide for this part
# cpu_choice = None
#
# # TODO: Determine if the user wins, the cpu wins, or its a draw
#
# # Challenge: TODO: Robust Input
# # Challenge: TODO: Multi-rounds

Options("Rock", "Paper", "Scissors")

user_choice = input("Pick (rock/paper/scissors): ")
cpu_choice = None


def use_choice():
    if:
        user_choice = input("Pick a choice (rock/paper/scissors): ")
        if user_choice:
            return user_choice

def cpu_choice()
    return choice(options)


def winner(player, cpu):
    if player == cpu:
        return "Draw"
    elif (
            (player == "rock" and cpu == "scissors") or
            (player == "paper" and cpu == "rock") or
            (player == "scissors" and cpu == "paper")
    ):
        return "Player"
    else:
        return "CPU"


    print(f"Player chose {player_choice}, CPU chose {cpu_choice}")
    if result == "Tie":
        print("Tie")
    else:
        print(result, "Tie")

game()