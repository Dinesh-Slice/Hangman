import random
import time

def timed_input(prompt, timeout):
    start = time.time()
    s = input("({}s) {}".format(timeout, prompt))
    stop = time.time()
    if stop-start > timeout:
        print("TIMEOUT!")
        return ''
    return s

def input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("You should have picked a number instead! Now play at max difficulty!!")
        return 8

''' Testing new code on Github ''' 

def new_funtion():
    pass 

def play_game():
    print()
    name = input("What is your name? : ")
    print()

    diff = input_int("Choose your difficulty (4-8 letters): ")
    if diff > 8:
        print("You had 1 job! Now max difficulty! 8 letters!")
        diff = 8
    if  diff < 4:
        diff = 8
        print("You had 1 job! Now max difficulty! 8 letters!")

    print()
    print("Welcome to Hangman {} ...".format(name))
    print()
    time.sleep(2)
    print("Get ready to play in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print()

    word = open("words.txt").read().splitlines()
    word = [w for w in word if "'" not in w]
    word = [w for w in word if len(w) >= 3]
    word = [w for w in word if w == w.lower()]
    word = [w for w in word if len(w) <= 8]
    word = [w for w in word if len(w) == diff]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    w = random.choice(word)
    length  = len(w)

    underscore = "_ " * length
    underscore =  underscore.split()

    used_lets = []

    turns = 10

    while True:
        print (" ".join(underscore))
        let = (timed_input("Guess a letter: ",2*turns).lower())
        print()
        time.sleep(0.5)

        if let == "TIMEOUT!":
            turn = turn - 1
            print("You have {} turns left".format(turns))
            if turns == 0:
                print("Game over!! You lose! ")
                print ("The word was {}".format(w.upper()))
                break

        if len(let) > 1:
            print ("Only one letter!")
            print("You have {} turns left".format(turns))
            if turns == 0:
                print("Game over!! You lose! ")
                print ("The word was {}".format(w.upper()))
                break

        elif let == "" or let not in alphabet:
            turns = turns - 1
            print("Try typing a letter next time! You have {} turns left".format(turns))
            if turns == 0:
                print("Game over!! You lose! ")
                print ("the word was {}".format(w.upper()))
                break


        elif (let not in w):
            if let not in used_lets:
                turns = turns - 1
            if turns == 0:
                print("Game over!! You lose! ")
                print ("the word was {}".format(w.upper()))
                break


            print ("Try again, you have only {} lives left!".format(turns))
            print()
            time.sleep(0.25)

            if let not in used_lets:
                used_lets.append(let)

                print ("So far you have used:")
                print ((", ".join(used_lets)).upper())
                print()
                time.sleep(0.25)
            else:
                print ("So far you have used:")
                print ((", ".join(used_lets)).upper())
                print()
                time.sleep(0.2)

        else:
            for i in range(length):
                if let == w[i]:
                    underscore[i] = let

        if "".join(underscore) == w:
            print ("Congratulations {}!! You won!! The word was {}".format(name,w.upper()))
            print()
            break

def application():
    play_game()
    another = input("Would you like to play again (y/n): ")
    while another.lower().startswith('y'):
        play_game()
        time.sleep(2)
        another = input("Would you like to play again (y/n): ")

application()

