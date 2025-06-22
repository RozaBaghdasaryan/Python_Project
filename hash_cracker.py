# www.geeksforgeeks.org
import hashlib

def crack_hash(hash_to_crack, wordlist_file, hash_algorithm='md5'):
    with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
        for word in file:
            word = word.strip()
            hashed_word = hashlib.new(hash_algorithm, word.encode()).hexdigest()
            if hashed_word == hash_to_crack:
                return word
    return None

if __name__ == '__main__':
    target_hash = input("Enter the hash to crack: ").strip()
    wordlist = input("Enter the path to the wordlist file: ").strip()
    hash_algo = input("Enter the hash algorithm (md5, sha1, sha256): ").strip().lower()

    if hash_algo not in ['md5', 'sha1', 'sha256']:
        print("Unsupported hash algorithm. Please choose md5, sha1, or sha256.")
        exit(1)

    result = crack_hash(target_hash, wordlist, hash_algo)

    if result:
        print(f"[+] Hash cracked! The original text is: {result}")
    else:
        print("[-] Password not found in the wordlist.")
