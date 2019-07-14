import json

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data :
        return data[w]
    else:
        return "The word doesn't exit, Please re-check it!"
word = input("Enter word:")

print(translate(word))
