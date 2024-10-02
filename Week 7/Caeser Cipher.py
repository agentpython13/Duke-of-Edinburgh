plaintext = 'BINCE THOMAS' # or input("Type plaintext: ")
key = int(input())

def caeser_cipher(plaintext, key):
    plaintext = list(plaintext)
    
    counter = 0
    
    while counter != len(plaintext):
        letter = plaintext[counter]
        
        if letter == ' ':
            pass
        else:
            case = letter.isupper()
            letter = letter.lower()
            if key >= 0:
                if ord(letter) + (key%26) <= 122:
                    plaintext[counter] = chr(ord(letter) + (key%26))
                else:
                    plaintext[counter] = chr(97 + ord(letter) + (key%26) - 122)
            else:
                if ord(letter) - (abs(key)%26) >= 97:
                    plaintext[counter] = chr(ord(letter) - (abs(key)%26))
                else:
                    plaintext[counter] = chr(123 - (97 - (ord(letter) - (abs(key)%26))))
        
        if case:
            plaintext[counter] = plaintext[counter].upper()
        
        counter += 1
        
    plaintext = "".join(plaintext)
    return plaintext

        
        
    