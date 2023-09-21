alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decode_caesar(message, offset):
    translation = ''
    for letter in message:
        if letter in alphabet:
            letter_value = alphabet.find(letter)
            translation += alphabet[(letter_value + offset) % 26]
        else:
            translation += letter
    return translation

def encode_caesar(message, offset):
    translation = ''
    for letter in message:
        if letter in alphabet:
            letter_value = alphabet.find(letter)
            translation += alphabet[(letter_value - offset) % 26]
        else: translation += letter
    return translation


def brute_force(message1):
    count = 0
    while count < 25:
        message_decoded = decode_caesar(message1, count)
        print(message_decoded)
        count += 1
