def uses_all(word, letters):

    # if all of the letters in word exist the list of letters, we return True. 
    for letter in letters:
        if letter not in word:
            return False
        
    return True


fin = open(r'C:\Users\3yanl\Code\lectures\lecture9\words.txt')
required_letters = "aeiou"
for line in fin:
    word = line.strip()
    if uses_all(word, required_letters):
        print(word)