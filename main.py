# Name: David Lee
# Purpose: The purpose of this program is to create a number guessing game that allows the user to continue
# to guess until they correctly guess the actual value of a randomly generated number between 1 and 100.
# It will continuously update the accompanying txt file that holds the current top 5 leaderboard.
# The game is also updated to be able to handle exceptions and leave the user a pretty error message
# detailing the error.

from random import randint


try:
    exit_cond = False

    print("Welcome to the number guessing game! You may exit the game at any time by entering in Q or q at any time.")
    player_name = input("Please enter in your name (less than or equal to 10 characters): ")

    # To prevent the player from entering in names that are too long
    if len(player_name) > 10:
        player_name = player_name[:10]

    while not exit_cond:
        rand_num = randint(1, 100)
        user_guess = input("Please guess a number between 1 and 100: ")
        guess_count = 1
        correct = False

        while not exit_cond and not correct:
            # If user inputs the exit command
            if user_guess.lower() == "q":
                print("Thank you for playing the number guessing game. Please join us again soon!")
                exit_cond = True

            # Do not accept any non positive integer values
            elif user_guess.isnumeric() == False:
                print("Incorrect input. Please only enter in an integer value between 1 and 100. ")
                user_guess = input("Please guess a number between 1 and 100:  ")

            # Only accept numbers in the range 1-100
            elif int(user_guess) < 1 or int(user_guess) > 100:
                user_guess = input("Please only enter a number between 1 and 100. Please guess another number: ")

            # If user guesses too low
            elif int(user_guess) < rand_num:
                user_guess = input("Guess is too low. Please guess again: ")
                guess_count += 1

            # If user guesses too high
            elif int(user_guess) > rand_num:
                user_guess = input("Guess is too high. Please guess again: ")
                guess_count += 1

            # If user guesses correctly
            else:
                print("That is correct. Good job!")
                print(f"It took {guess_count} guesses to reach the correct number.")
                print("Thank you for playing the guessing game! See you again next time!")
                correct = True

        if correct:
            file = open("topPlayers.txt", "r+")
            list_top_players = []
            for line in file:
                elem = int(line[:10].rstrip()), line[10:].rstrip()
                list_top_players.append(elem)

            # inserting new leaderboard score
            for i in range(5):
                if guess_count < list_top_players[i][0]:
                    list_top_players.insert(i, [guess_count, player_name])
                    break
            list_top_players = list_top_players[:5]

            # To do inplace file replace after reading
            file.seek(0)
            file.truncate()

            # Writing updated top 5 to file in correct format
            for i in range(5):
                if i != 4:
                    file.write(str(list_top_players[i][0]) + " "*(10-len(str(list_top_players[i][0]))) + list_top_players[i][1] + "\n")
                else:
                    file.write(str(list_top_players[i][0]) + " "*(10-len(str(list_top_players[i][0]))) + list_top_players[i][1])

            file.close()

            # Printing updated leaderboard
            print("Here is the updated leaderboard:")
            for i in range(5):
                print(str(list_top_players[i][0]) + " " * (10 - len(str(list_top_players[i][0])))  + list_top_players[i][1])
            input("\nPress [ENTER] to continue playing.")

except Exception as e:
  print()
  print(f"Error encountered. Exiting: {e}")
  print("Thank you for playing the Number Guessing Game 2.0!")
