# Load the hash data into a dictionary
hash_to_word = {}

with open('hash_data_sha256.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(' -> ')
        if len(parts) == 2:
            hashed_word, word = parts
            hash_to_word[hashed_word] = word
        else:
            print(f"Skipping malformed line: {line}")

    # Prompt the user to input a SHA-256 hash
    user_input_hash = input("Enter a SHA-256 hash: ")

    # Search for the hash in the dictionary
    if user_input_hash in hash_to_word:
    print(f"The plain text for the hash {user_input_hash} is: {hash_to_word[user_input_hash]}")
    else:
    print("No matching plain text found for the given hash.")
