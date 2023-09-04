def has_no_e(word):
    if "e" in word:
        return False
    else:
        return True


def has_no_e_short(word):
    return "e" not in word


fin = open(r'C:\Users\3yanl\Code\lectures\lecture9\words.txt')
for line in fin:
    word = line.strip()
    if has_no_e(word):
        print(word)