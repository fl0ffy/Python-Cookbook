import random

print("ROCK, PAPER, SCISSORS")
wins = losses = ties = 0

while True:
    print("{} Wins, {} Losses, {} Ties".format(wins, losses, ties))
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")

    player_move = input()
    program_move = random.choice(["ROCK", "PAPER", "SCISSORS"])

    if player_move == 'q':
        break
    if player_move == 'p':
        print("PAPER versus...")
        print(program_move)
        if program_move == "PAPER":
            print("It is a tie!")
            ties += 1
        if program_move == "ROCK":
            print("You win!")
            wins += 1
        if program_move == 'SCISSORS':
            print("You lose!")
            losses +=1

    if player_move == 'r':
        print("ROCK versus...")
        print(program_move)
        if program_move == "ROCK":
            print("It is a tie!")
            ties += 1
        if program_move == "SCISSORS":
            print("You win!")
            wins += 1
        if program_move == 'PAPER':
            print("You lose!")
            losses +=1

    if player_move == 's':
        print("SCISSORS versus...")
        print(program_move)
        if program_move == "SCISSORS":
            print("It is a tie!")
            ties += 1
        if program_move == "PAPER":
            print("You win!")
            wins += 1
        if program_move == 'ROCK':
            print("You lose!")
            losses +=1
