import random
options=["rock","paper","scissors"]


while True:
    
    print("Welcome to Rock, Paper, Scissors!")
    print("In this game there are two users one is Computer and other is You i.e player ")
    computer= random.choice(options)

    player = input("Enter your choice (rock/paper/scissors): ").lower()

    while player not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        player = input("Enter your choice (rock/paper/scissors): ").lower()

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player== computer:
        print(f"Both player are selected  {player}.It is Tie Game!")

    elif player=='rock':
        if computer=="scissors":
           print("Rock Smashes scissors! You Win!")

        else:
           print("Paper Covers rock! You lose !")


    elif player=="paper":
        if computer=="rock":
           print("Paper Covers rock! You Win!")

        else:
           print("Scissors Cuts paper! You lose !")

    elif player=="scissors":
        if computer=="paper":
           print("Scissors Cuts paper! You Win!")

        else:
           print("Scissors Cuts Paper! You Win!")




    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thank You For Playing This Game!Hope you Enjoy ")
        break
    






