def uses_only(word, letters):

    # if any of the letters in word does not exist the list of letters, we return false. 
    for letter in word:
        if letter not in letters:
            return False
        
    return True


fin = open(r'C:\Users\3yanl\Code\lectures\lecture9\words.txt')
allowed_letters = "acefhlo"
for line in fin:
    word = line.strip()
    if uses_only(word, allowed_letters):
        print(word)