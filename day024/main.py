#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('/100daysofcode/day024/Input/Letters/starting_letter.txt') as fbase:
    contents = fbase.read()
    with open('/100daysofcode/day024/Input/Names/Invited_names.txt') as fnames:
        names = [line.strip() for line in fnames]
        for name in names:
            with open(f'/100daysofcode/day024/Output/ReadyToSend/letter_for_{name}.txt', 'a') as letter:
                letter.write(contents.replace('[name]', name))