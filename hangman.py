import sys


def get_word(word):
    list_word = list(word)
    word_length = len(list_word)
    guessing_word = []
    guessing_word.append(list_word[0])
    for i in range(word_length - 2):
        guessing_word.append("_")
    guessing_word.append(list_word[-1])
    return guessing_word


def start_guessing(users_word, listed_word):
    run = True
    counter = 9
    list_word = listed_word
    user_word = list(users_word)
    wrong_letters = []
    print(list_word)
    while run:
        char = str(input("Введи букву: "))
        if char in user_word:
            index = user_word.index(char)
            user_word[index] = " "
            print(user_word)
            list_word[index] = char
            print()
            print(list_word)
            print("You have " + str(counter) + " tries!")
            if list_word == list(users_word):
                print()
                print("You won!")
                run = False
        else:
            wrong_letters.append(char)
            print()
            print(list_word)
            print("Wrong letters:" + ', '.join(wrong_letters))
            print("You have " + str(counter) + " tries!")
        counter -= 1
        if counter == 0:
            print("You lost! Word was: " + users_word + "\n")
            run = False


if __name__ == "__main__":
    p = True
    while p:
        play = str(input("Hello Username, wanna play a hangman?\n'y' or 'n'\n"))
        if play.lower() == "y":
            user_word = str(input("Введи слово: "))
            list_word = get_word(user_word)
            start_guessing(user_word, list_word)
            p = False
        elif play.lower() == "n":
            sys.exit("See ya later!\n")
            p = False
        else:
            print("Something went wrong, try again.\n")
            