import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

user_input = input("Enter a word: ").upper()

input_list = list(user_input)

print([nato_dict[nato_letter] for nato_letter in input_list])
