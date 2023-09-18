def is_abecedarian(word):

    # if all of the letters in word exist the list of letters, we return True.
    previous_letter = "a" 
    for letter in word:
        if letter < previous_letter:
            return False
        previous_letter = letter
    return True


fin = open(r'C:\Users\3yanl\Code\lectures\lecture9\words.txt')
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        print(word)