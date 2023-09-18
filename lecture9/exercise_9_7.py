def is_triple_double(word):

    # if there are three consecutive double lettersin the word
    previous_letter = "a"
    count_letter = 0
    was_double = False
    for i,letter in enumerate(word):
        if letter == previous_letter:
            count_letter = count_letter + 1
            if count_letter == 3:
                return True
        elif not (i > 1 and word[i-1] == word[i-2]):
            count_letter = 0

        previous_letter = letter
    return False

print(is_triple_double("committee"))


# fin = open(r'C:\Users\3yanl\Code\lectures\lecture9\words.txt')
# for line in fin:
#     word = line.strip()
#     if is_triple_double(word):
#         print(word)