# 3a. Compare List vs Set for Duplicate Analysis
users_list = ["alice", "bob", "alice", "charlie", "bob"]
users_set = set(users_list)

print(f"Original List (with duplicates): {users_list}")
print(f"Unique Set (duplicates removed): {users_set}")
print(f"Total duplicates found: {len(users_list) - len(users_set)}")


# 3b. Caesar Cipher (Encryption and Decryption)
def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift within A-Z or a-z range
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

msg = "Hello Python!"
encrypted = caesar(msg, 3)
decrypted = caesar(encrypted, -3)

print(f"\nOriginal: {msg}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
