PLACE = "[name]"

with open("Input/Names/invited_names.txt") as file:
    content = file.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
        letter_cont = letter.read()
        for names in content:
            name = names.strip()
            new_letter = letter_cont.replace(PLACE, name)

            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final:
                final.write(new_letter)



