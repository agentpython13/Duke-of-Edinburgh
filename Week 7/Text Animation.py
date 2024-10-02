import string
import time

text = 'ENCODED'

def text_animation(text):
    characters = string.printable
    text = list(text)
    
    counter = 0
    for letter in text:
        for ch in characters:
            text[counter] = ch
            print("".join(text), end='\r')
            time.sleep(0.02)
            if letter == ch:
                break
        if counter == len(text)-1:
            print("".join(text))
        counter += 1

text_animation(text)
            