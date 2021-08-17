import re
import eel
import random
import sys


@eel.expose
def start_game():
    global word
    global tries
    lineLen = 0
    tries = 10
    word = list(random.choice(["apple", "orange", "grape", "avocado", "banana", "watermelon", "pineapple", "date", "apricot", "cherry",
                               "guava", "lemon", "mango", "pear", "pomegranate", "sapodilla", "prunes"]))
    for i in range(len(word)):
        game_state.append("_")
        lineLen += 1
    print(word)
    #print(lineLen)
    return lineLen


@eel.expose
def guss_char(userchar):
    index = []
    stop_game = False
    global correct_letter
    global tries
    winnig = 30

    tries -= 1
    stop_game = num_of_tries(tries)
    if stop_game:
        return -1

    if userchar in word:
        for i, j in enumerate(word):
            if j == userchar:
                index.append(i)
                correct_letter += 1
        if correct_letter == len(word): # user found all letters
            return winnig
        return index


def num_of_tries(tries):
    print(tries)
    if tries == 0:
        print("you lose")
        return True
    return False

correct_letter = 0
tries = 10
words = []
game_state = []

eel.spawn(start_game)
eel.init('web')
eel.start('mainPage.html', size=(850, 450), port=9000)

