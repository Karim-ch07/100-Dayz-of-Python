import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
NATO_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

NATO = {row.letter:row.code for (index,row) in NATO_dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Tell me a word!\t")
user_word = user_word.upper()
user_NATO = []

for user_letter in user_word:
    for (letter, code) in NATO.items():
        if user_letter == letter:
            user_NATO.append(code)

print(user_NATO)
