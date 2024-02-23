def encryption(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha(): #need for text only if unicode larger greater next part dealing with it
            shifted = ord(char)+shift
            if char.islower():
                if shifted>ord("z"):
                    shifted -= 26
                elif shifted<ord("a"):
                    shifted +=26
            if char.isupper():
                if shifted>ord("Z"):
                    shifted -=26
                elif shifted<ord("A"):
                    shifted +=26
            encrypted_text += chr(shifted) #chr is the opp of ord 
        else:
            encrypted_text += char
    return encrypted_text

def decryption(text, shift):
    return encryption(text, -shift)

input_string = input("Enter text to encrypt: ")
shift_value = int(input("Enter shift value: "))
e_text = encryption(input_string, shift_value)
print("Encrypted text- ", e_text)

d_text = decryption(e_text, shift_value)
print("Decrypted text- ", d_text)

