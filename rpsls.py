import random 


# p > r > l > sp > s > l > p > sp > r > s
def rpsls():
    while True:
        choices = ['rock', 'paper', 'scissors','lizard', 'spock']
        player = input('rock, paper, scissors, lizard, or spock?: ')
        computer = random.choice(choices)
        while player not in choices:
            player = input('rock, paper, scissors, lizard, or spock?: ')
        print(f"player: {player}")
        print(f"computer: {computer}")
        if player == computer:
            print("It's a tie!")

        elif computer == 'rock':
            if player == 'paper':
                print('you win!')
            elif player == 'scissors':
                print('you lose!')
            elif player == 'lizard':
                print('you lose!')
            elif player == 'spock':
                print('you win!')
        elif computer == 'paper':
            if player == 'rock':
                print('you lose!')
            elif player == 'scissors':
                print('you win!')
            elif player == 'lizard':
                print('you win!')
            elif player == 'spock':
                print('you lose!')
        elif computer == 'scissors':
            if player == 'paper':
                print('you lose!')
            elif player == 'rock':
                print('you win!')
            elif player == 'lizard':
                print('you lose!')
            elif player == 'spock':
                print('you win!')# p > r > l > sp > s > l > p > sp > r > s
        elif computer == 'lizard':
            if player == 'paper':
                print('you lose!')
            elif player == 'rock':
                print('you win!')
            elif player == 'scissors':
                print('you win!')
            elif player == 'spock':
                print('you lose!')
        elif computer == 'spock':
            if player == 'paper':
                print('you win!')
            elif player == 'rock':
                print('you win!')
            elif player == 'lizard':
                print('you win!')
            elif player == 'scissors':
                print('you lose!')   
        play_again = input('do you want to play again? yes/no: ').lower()
        if play_again != 'yes':
            break


    
    
rpsls()




