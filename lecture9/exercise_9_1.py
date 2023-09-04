fin = open(r'C:\Users\3yanl\Code\lectures\lecture9\words.txt')
for line in fin:
    word = line.strip()
    word = line.replace(" ", "")
    if len(word) > 20:
        print(word)