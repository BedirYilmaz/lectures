def avoids(word, forbiddens):
    for forbidden_letter in forbiddens:
        if forbidden_letter in word:
            return False
    return True


fin = open(r'C:\Users\3yanl\Code\lectures\lecture9\words.txt')
forbidden_letters = "clemens"
for line in fin:
    word = line.strip()
    if avoids(word, forbidden_letters):
        print(word)