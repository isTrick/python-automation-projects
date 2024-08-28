import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

rock = 'r'
paper = 'p'
scissors = 's'

_quit = 'q'

answer = ''
computer_answer = ''
random_answer = ''
while answer != _quit:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    answer = input()
    random_answer = random.randint(1, 3)

    if random_answer == 1:
        computer_answer = rock
    elif random_answer == 2:
        computer_answer = paper
    elif random_answer == 3:
        computer_answer = scissors
    
    if answer == _quit:
        print("Thank's for play")
        sys.exit()
    elif answer == computer_answer:
        print("It's a tie")
        ties += 1
    elif answer == rock and computer_answer == scissors or answer == paper and computer_answer == rock or answer == scissors and computer_answer == paper:
        print('You win!')
        wins += 1
    elif answer == scissors and computer_answer == rock or answer == rock and computer_answer == paper or answer == paper and computer_answer == scissors:
        print('You lose!')
        losses += 1
    else:
        print("This isn't expected, an error ocurred")

    


