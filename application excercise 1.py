import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def my_dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        return "Did you mean %s instead?" % get_close_matches(w,data.keys())[0]
    else:
        return "This word does not exist in the dictionary. Please double check the spelling"

word = input("Enter a word: ")

 print(my_dictionary(word))

