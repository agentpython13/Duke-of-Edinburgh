import string
import time
import getpass

def caeser_cipher(plaintext, key):
    plaintext = list(plaintext)
    
    counter = 0
    
    while counter != len(plaintext):
        letter = plaintext[counter]
        check = True
        
        if letter == ' ':
            check = False
        else:
            case = letter.isupper()
            letter = letter.lower()
            if key >= 0:
                if ord(letter) + (key%26) <= 122:
                    plaintext[counter] = chr(ord(letter) + (key%26))
                else:
                    plaintext[counter] = chr(96 + ord(letter) + (key%26) - 122)
            else:
                if ord(letter) - (abs(key)%26) >= 97:
                    plaintext[counter] = chr(ord(letter) - (abs(key)%26))
                else:
                    plaintext[counter] = chr(123 - (97 - (ord(letter) - (abs(key)%26))))
        
        if check:
            if case:
                plaintext[counter] = plaintext[counter].upper()
        
        counter += 1
        
    plaintext = "".join(plaintext)
    return plaintext

def cipher_animation(plaintext, key):
    specials = ["!",",", ".", "?", "/", "(", ")", ":", ";", "[", "]", "-", ' ', ">", "<", "{", "}", "_", "+", "=", "@", "#", "£", "%", "&", "*", "'", '"']
    characters = string.printable
    plaintext = list(plaintext)
    
    counter = 0
    for letter in plaintext:
        if letter in specials:
            plaintext[counter] = letter
        else:
            for ch in characters:
                plaintext[counter] = ch
                print("".join(plaintext), end='\r')
                time.sleep(0.02)
                if ch == caeser_cipher(letter, key):
                    break
        if counter == len(plaintext)-1:
            print("".join(plaintext))
        counter += 1
        

#user interactions
print()
print("Welcome to Bennet Thomas' Caeser Cipher Encrypter!")
time.sleep(2)
print("\033[A                             \033[A")

key = int(input("What key would you like to use to encrypt? (+ve or -ve accepted) "))
time.sleep(2)
print("\033[A                                        \033[A")

print("Type the plaintext you would like encrypt below (no special characters, max. 100 characters): ")
time.sleep(3)
print("\033[A                                                                                                          \033[A")

plaintext = input()
print("\033[A                                                                                                                                                                        \033[A")
time.sleep(1)

print("ENCRYPTING MESSAGE...")
time.sleep(1)
print("\033[A                                                                                                          \033[A")

cipher_animation(plaintext, key)           