import random as r

while True:
    list = ["Rock", "Paper", "Scissors"]
    computer_action = r.choice(list)

    print("""1. Rock
    2. Paper
        3. Scissorcs""")
    user_input = input("Choose one: ")
    if user_input == computer_action:
        print(f"Both players chose {user_input}. It's a tie")
    elif user_input == "Rock":
        if computer_action == "Scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose!")
    elif user_input == "Paper":
        if computer_action == "Rock":
            print("Paper beats rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user_input == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")
    u_input = input("""Would you like to go again: Yes/No 
    """)
    if u_input == "Yes":
        continue
    else:
        break



