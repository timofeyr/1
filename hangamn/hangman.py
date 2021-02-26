import sys
import sqlite3

con = sqlite3.connect('players.db')
c = con.cursor()


def add_user():
    username = str(input("Type in username: "))
    c.execute("INSERT INTO players VALUES (?, ?)", (username, 0))
    con.commit()


def add_score(user):
    score = c.execute("SELECT score FROM players WHERE username = ?", (user,)).fetchone()
    c.execute("UPDATE players SET score = ? WHERE username = ?", (score[0] + 1, user))
    con.commit()


def get_word(word):
    list_word = list(word)
    word_length = len(list_word)
    guessing_word = []
    guessing_word.append(list_word[0])
    for i in range(word_length - 2):
        guessing_word.append("_")
    guessing_word.append(list_word[-1])
    return guessing_word


def start_guessing(users_word, listed_word, user):
    counter = 9
    list_word = listed_word
    user_word = list(users_word)
    wrong_letters = []
    print(list_word)
    run = True
    while run:
        char = str(input("Enter a character: "))
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
                add_score(user)
                score = c.execute("SELECT score FROM players WHERE username = ?", (user,)).fetchone()
                print("You have " + str(score[0]) + " scores!")
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
    users = c.execute("SELECT username FROM players").fetchall()
    print("Users: " + str(users))
    login = True
    while login:
        log_ans = int(input("1. Create new user.\n2. Play as created user.\n"))
        if log_ans == 1:
            add_user()
        elif log_ans == 2:
            trying = True
            while trying:
                user = str(input("Enter your username: "))
                users = c.execute("SELECT username FROM players").fetchall()
                if user not in str(users):
                    print("There is no " + user + " user! Try again.")
                elif user in str(users):
                    print("You are playing as " + user + "!")
                    trying = False
                    login = False
        else:
            print("Something went wrong.\n")

    p = True
    while p:
        play = str(input("Hello " +  user + ", wanna play a hangman?\n'y' or 'n'\n"))
        if play.lower() == "y":
            user_word = str(input("Enter a word: "))
            list_word = get_word(user_word)
            start_guessing(user_word, list_word, user)
            p = False
        elif play.lower() == "n":
            sys.exit("See ya later!\n")
            p = False
        else:
            print("Something went wrong, try again.\n")

    con.close()