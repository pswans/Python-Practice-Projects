import random #random now accessible in this file.

#If you want, you can also just import 'random,' 'randint,' (and so on) as shorter, more acessible functions using from (package name) import as (whatever you want). 
#Below, the 'while true' statement is used to ask the player if they want to play again; it's not entirely necessary. 
#However, if one does decide to keep it in place, make sure your code lines are properly indented.

while True:
   
# print(random.randint (0,5)) #This will print a random interger from range 0 through 5, 'randint' is a function accessible through the random module.
# print(random.random() * 256) #random seems to give a completely random number, also includes bools.
# print(random.random())

    RPS = ['Rock', 'Paper', 'Scissors'] #print(random.choice(RPS)); prints one random. Works for any type as well, not just strings. 
    user_action = input("Rock, Paper, or Scissors:")
    possible_actions = ['Rock', 'Paper', 'Scissors']
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, the computer chose {computer_action}.\n")
    if user_action == computer_action:
        print("It's a tie! Both players selected the same thing!")
    elif user_action == 'Rock':
        if computer_action == 'Scissors':
            print('Rock smashes Scissors! You win!')
        else: 
            print('Paper covers Rock? You lose, I guess...')
    elif user_action == 'Scissors':
        if computer_action == 'Paper':
            print('Scissors cut Paper. You win!')
        else:
            print('Rock smashes Scissors. You lose!')
    elif user_action == 'Paper':
        if computer_action == 'Rock':
            print('Rock gets covered by Paper? You win, I guess...')
        else:
            print('Scissors cuts Paper. You lose!')

    play_again = input('Run it back? (y/n): ')
    if play_again.lower() != 'y':
        break
