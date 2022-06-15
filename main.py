import pandas as pd
data = pd.read_csv('morse.txt', sep=" ")
asa = data['MORSE'].loc[data['LETTER'] == 'A']
program_run = True
def morse_converter(text):
    convert = data['MORSE'].loc[data['LETTER'] == f'{text}']
    return convert.values
while program_run:
    user_data = input("Please write a text you want to convert into Morse Code: ")
    for symbols in user_data:
        print(morse_converter(symbols.upper()))
    if user_data == 'Exit':
        program_run = False