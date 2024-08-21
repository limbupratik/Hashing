import hashlib

def convert_to_md5(word):
    word_bytes = word.encode('utf-16')
    result = hashlib.md5(word_bytes)
    return result.hexdigest()


with open('input.txt', 'r') as file:
    content = file.read()

words = content.split()

hashed_words = [convert_to_md5(word) for word in words]


with open('hash_data.txt', 'w') as output_file:
    for word, hashed_word in zip(words, hashed_words):
        output_file.write(f'{word}->{hashed_word}\n')

print("Data is converted to MD5 'hash_data.txt'.")

with open('hash_data_sha256.txt', 'w') as output_file:
    for word, hashed_word in zip(words, hashed_words):
        output_file.write(f'{word}-> {hashed_word}\n')

print("Hashed data has been written to 'hash_data_sha256.txt'.")

