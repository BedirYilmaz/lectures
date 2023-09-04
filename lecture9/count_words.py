

fin = open(r'C:\Users\3yanl\Code\lectures\lecture9\words.txt')
count = 0
for line in fin:
    word = line.strip()
    print(word)
    count += 1
