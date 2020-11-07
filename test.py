import string
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", help = "Set length of a password")

def generate(length):
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    punctuation   = string.punctuation
    digits        = string.digits
    digits        = str(digits)

    all_c = f'{lower_letters}{upper_letters}{digits}{punctuation}'

    all_c = list(all_c)
    random.shuffle(all_c)

    password = []

    for i in range(int(length)):
		password.append(random.choice(all_c))

    password = ''.join(password)

    return password

if __name__ == "__main__":
    args = parser.parse_args()
    password = generate(args.length)
    print(password)
