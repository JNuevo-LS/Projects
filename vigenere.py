def vigenere_decode(message, keyword):
    translation = ''
    count = 0
    for letter_m in message:
        if letter_m in alphabet:
            letter_m_value = alphabet.find(letter_m)
            translation += alphabet[(letter_m_value + (alphabet.find(keyword[0+count]))) % 26]
            count+=1
            if count == len(keyword):
                count = 0
        else: translation += letter_m
    print(translation)

def vigenere_encode(message, keyword):
    translation = ''
    count = 0
    for letter_m in message:
        if letter_m in alphabet:
            letter_m_value = alphabet.find(letter_m)
            translation += alphabet[(letter_m_value - (alphabet.find(keyword[0+count]))) % 26]
            count+=1
            if count == len(keyword):
                count = 0
        else: translation += letter_m
    print(translation)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
