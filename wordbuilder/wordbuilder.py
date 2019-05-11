import numpy as np

with open('wordbuilder/words.txt', 'r') as words:
    all_words = words.readlines()

allowed_chars = set('abcdefghijklmnopqrstuvwxyz\n')

all_words_clean = [word.lower()
                   for word in all_words
                   if set(word).issubset(allowed_chars)]

alphabet = {
'a': 0,
'b': 1,
'c': 2,
'd': 3,
'e': 4,
'f': 5,
'g': 6,
'h': 7,
'i': 8,
'j': 9,
'k': 10,
'l': 11,
'm': 12,
'n': 13,
'o': 14,
'p': 15,
'q': 16,
'r': 17,
's': 18,
't': 19,
'u': 20,
'v': 21,
'w': 22,
'x': 23,
'y': 24,
'z': 25,
'\n': 26
}

def create_probas(list_words=all_words_clean):
    all_poss = np.zeros(shape=[26,27])

    for word in list_words:
        #print(word)
        for letter_ind in range(len(word) - 1):
            all_poss[
                alphabet[word[letter_ind]]
                   ][
                alphabet[word[letter_ind + 1]]
                   ] = all_poss[
                       alphabet[word[letter_ind]]
                          ][
                       alphabet[word[letter_ind + 1]]
                          ] + 1

    return all_poss

#print(all_words_clean[:1])
all_probas = create_probas(all_words_clean)

all_probas = all_probas / all_probas.sum(axis=1)[:,None]

#print(all_probas[:,26])

def predict_next_letter(letter):
    letter_ind = alphabet[letter]
    probas = all_probas[letter_ind,:]
    next_letter_ind = np.random.choice(range(27), p=probas)
    return [k for (k,v) in alphabet.items() if v==next_letter_ind][0]

def generate_word(word, min_len=6):
    if len(word) == 0:
        return 'Please enter a word'
    else:
        next_letter = predict_next_letter(word[-1])
        print(word + next_letter)
        if next_letter == '\n' and len(word) >= 6:
            return word + next_letter
        elif next_letter == '\n':
            return generate_word(word, min_len=min_len)
        else:
            return generate_word(word + next_letter, min_len=min_len)

#print(predict_next_letter('a'))
print(generate_word('a'))
