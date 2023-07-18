import random

choice = None

fh=open("Word_list.txt","r")  

lst=list()
for line in fh:
    line=line.rstrip()
    line=line.split()
    for wor in line:
        lst.append(wor)
while choice != 0:
    print('''
    Welcome to Console Hangman!

    Please select a menu option:

    0 - Exit
    1 - Play Game

    ''')
    choice= input("Enter you choice: ")

    if choice == 0:
        print("Exiting the program...")
    elif choice == 1:
        word = random.choice(lst)
        while len(word)<4:
            word = random.choice(lst)            
        hidden_word = "_" * len(word)
        lives = 8
        guessed = []

        while lives != 0 and hidden_word != word:
            print("\n")
            print("The secret word looks like:",hidden_word)
            print("\n")
            #print(hidden_word)
            print("Your bad guesses so far: ",' '.join(guessed))
            print("\n")
            #print(' '.join(guessed))
            print("You have", lives,"guesses remaining")
            print("\n")
            guess = input("What's your next guess?")
            # here give your guess letter inside double quotes ""
            guess = guess.lower()
            print("\n")
            while len(guess) > 1:
                guess = input("\n You can only guess one letter at a time!\n Try again: ")
                guess = guess.lower()
            while guess in guessed:
                print("\n You have already guessed that letter!\n")
                guess = input("\n Please take another guess: ")
                guess = guess.lower()
            
            if guess in word:
                print("Nice guess!")
                print("\n")
                word_so_far = ""
                for i in range (len(word)):
                    if guess == str(word[i]):
                        word_so_far += guess
                    else:
                        word_so_far += hidden_word[i]
                hidden_word = word_so_far
            else:
                guessed.append(guess)
                print("Sorry there is no ", guess)
                print("\n")
                lives -= 1 #lives=lives-1

        if lives == 0:
                print("GAME OVER! You have no lives left")
        else:
            print("\n CONGRATULATIONS! You have guessed the word")
            print("The word was", word)
            print("\nThank you for playing Hangman")
    else:
        print("\n That is not a valid option! Please try again!\n ")
