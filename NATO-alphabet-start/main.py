import pandas

#Create a dictionary in this format:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
all_dict = {row['letter'] : row['code'] for (index,row) in data.iterrows()}

#Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a Word: ").upper()
code = [all_dict[letter] for letter in word]
print(code)

