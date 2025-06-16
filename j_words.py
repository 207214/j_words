import json

russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

alphabet_dict = dict(zip(russian_alphabet, range(1, len(russian_alphabet) +1)))

j_words_dict = {
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": []
}

russian_words_file = "russian.utf-8"
result_file = "j_words.json"

def handle_word(word):
    word_sum = 0
    word_len = len(str(word))
    if word_len > 1:
        for letter in word.lower():
            if letter in russian_alphabet:
                word_sum += alphabet_dict[letter]
        j_value = pow(2, word_len) 
        if word_sum == j_value:
            j_words_dict[str(word_len)].append(word)
    return 0;

with open(russian_words_file, "r") as f:
    for line in f:
        word = line.strip()
        handle_word(word)

print(j_words_dict)
print("\n")
for key in j_words_dict.keys():
    print(key, " - ", len(j_words_dict[key]))

