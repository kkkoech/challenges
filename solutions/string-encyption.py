import math 
import re

def stringEncryption(stri):
    if len(stri.strip()) == 0:
        return ""
    #removes spaces
    stri = "".join(list(filter(lambda x:x!=" ",list(stri))))
    stri_len = len(stri)
    rows = math.floor(stri_len**0.5)
    cols = math.ceil(stri_len**0.5)

    def split_string(stri,jump):
        if len(stri) < jump:
            return [stri]
        #else:
        #    return list(list(stri[:jump])) + split_string(stri[jump:], jump)
        return [stri[:jump]] + split_string(stri[jump:], jump)

    #print(split_string("breadandcrumbs",3))
    word_list = split_string(stri, cols)

    #pad the shorter word with " "
    word_list = list(map(lambda x: x + (max(map(lambda y: len(y), word_list)) - len(x)) * " ", word_list))

    #'transpose' the word_list
    encrypted_word = ""
    for i in range(len(word_list[0])):
        encrypted_word += " " + "".join(list(map(lambda x:x[i], word_list)))

    encrypted_word = re.sub(" +"," ", encrypted_word)
    return encrypted_word.strip()


print(stringEncryption("feedthedog"))