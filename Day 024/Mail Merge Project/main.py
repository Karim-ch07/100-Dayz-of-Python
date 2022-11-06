#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter:
    i_contents = letter.read()
    with open("./Input/Names/invited_names.txt") as names:
        n_contents = names.readlines()
        n_contents_stripped = []
        for line in n_contents:
            n_contents_stripped.append(line.strip("\n "))

        for name in n_contents_stripped:
            new_letter = i_contents.replace("[name]", f"{name}")
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as RTSend:
                RTSend.write(new_letter)
