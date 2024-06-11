import random
import string

def random_string(length=4):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def encode_word(word):
    if len(word) == 2:
        return word[::-1]
    elif len(word) > 2:
        first_two = word[:2]
        random_chars = random_string()
        return random_chars + word + first_two
    return word

def decode_word(word):
    if len(word) == 2:
        return word[::-1]
    elif len(word) > 6:  # 4 random characters + word + 2 original first characters
        main_word = word[4:-2]  # remove 4 random chars and the last 2 chars
        return main_word  # return the main part of the word without the last two chars
    return word

def process_sentence(sentence, func):
    words = sentence.split()
    processed_words = [func(word) for word in words]
    return ' '.join(processed_words)

if __name__ == "__main__":
    choice = input("Do you want to encode or decode? (e/d): ").strip().lower()

    if choice == 'e':
        sentence = input("Enter a sentence to encode: ")
        encoded_sentence = process_sentence(sentence, encode_word)
        print(f"Encoded sentence: {encoded_sentence}")
    elif choice == 'd':
        sentence = input("Enter a sentence to decode: ")
        decoded_sentence = process_sentence(sentence, decode_word)
        print(f"Decoded sentence: {decoded_sentence}")
    else:
        print("Invalid choice. Please enter 'e' to encode or 'd' to decode.")
