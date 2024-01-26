import pandas
#craete dictionary
data=pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows() }

#take user input and create list of phonetic word

def generate_phonetic():
        user_input = input("Enter any word").upper()
        try:
           user_output_list = [phonetic_dict[every_letter] for every_letter in user_input]
        except KeyError:
            print("Sorry,only letters in the alphabet please")
            generate_phonetic()
        else:
             print(user_output_list)
generate_phonetic()





























