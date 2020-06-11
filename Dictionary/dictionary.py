import json
from difflib import get_close_matches
# json -> javascript object  notation
data = json.load(open("data.json"))


def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        user_input = input(
            "Did you perhaps mean %s ? If so press 'Y' else press 'N': " % get_close_matches(word, data.keys())[0]).lower()
        if user_input == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        else:
            user_input = input(
                "Did you perhaps mean %s ? If so press 'Y' else press 'N': " % get_close_matches(word, data.keys())[1]).lower()
            if user_input == 'y':
                return data[get_close_matches(word, data.keys())[1]]
            elif user_input == 'n':
                return "Please ensure the spelling is correct"
            else:
                return "The input was not recognized"
    else:
        return "The word does not exist"


def display(meanings):
    if type(meanings) == list:
        print("The definition(s) are: ")
        i = 1
        for x in meanings:
            print(str(i) + ". " + x)
            i += 1
    else:
        print(meanings)


repeat = ""

while repeat != "no":

    to_be_defined = input("\nEnter a word to be defined: ")

    definitions = define(to_be_defined)

    display(definitions)

    test = 0
    while test != 1:
        u_input = input("\nDo you wish to search for another word? (yes/no) ").lower()
        if u_input == "yes":
            repeat = "yes"
            test += 1
        elif u_input == "no":
            repeat = "no"
            test += 1
        else:
            print("Only enter either yes or no!")