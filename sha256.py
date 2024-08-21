import hashlib


def convert_to_sha256(word):
    word_bytes = word.encode('utf-16')
    result = hashlib.sha256(word_bytes)
    return result.hexdigest()


with open('input.txt', 'r') as file:
    content = file.read()

words = content.split()


hashed_words = [convert_to_sha256(word) for word in words]


with open('hash_data_sha256.txt', 'w') as output_file:
    for word, hashed_word in zip(words, hashed_words):
        output_file.write(f'{word}-> {hashed_word}\n')

print("Hashed data has been written to 'hash_data.txt'.")

