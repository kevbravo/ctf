#!/usr/bin/python3

a = 90
b = 26
p = 97
g = 31

u = 64
v = 9

key = 22
b_key = 22

def xor_encrypt():
    
    key_length = 7
    
def decrypt(cipher, key):
    unencrypted_text = ""
    for i in cipher:
        unencrypted_text += chr(i//key//311)
        
    return unencrypted_text
    
def xor_decrypt(cipher, text_key):
    plain_text = ""
    key_length = len(text_key)
    print(cipher)
    for i, char in enumerate(cipher):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plain_text += decrypted_char
    return plain_text

cipher_text = ""
text_key = "trudeau"
plaintext = "please encrypt this"
for i, char in enumerate(plaintext[::-1]):
    key_char = text_key[i % 7]
    encrypted_char = chr(ord(char) ^ ord(key_char))
    cipher_text += encrypted_char

cipher = []
for char in cipher_text:
    cipher.append(((ord(char) * key*311)))
    
test_cipher = [61578, 109472, 437888, 6842, 0, 20526, 129998, 526834, 478940, 287364, 0, 567886, 143682, 34210, 465256, 0, 150524, 588412, 6842, 424204, 164208, 184734, 41052, 41052, 116314, 41052, 177892, 348942, 218944, 335258, 177892, 47894, 82104, 116314]
semi_decrypt = decrypt(test_cipher, key)
plain = xor_decrypt(semi_decrypt, text_key)
print(plain[::-1])
