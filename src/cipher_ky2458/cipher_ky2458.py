'''
The function:
-------------
Each letter is replaced by a letter some fixed number of positions down the alphabet.

Inputs:
-------------
'text': str. The word or sentence that you want to encrypt. 
'shift': int. It means the direction and position you want to encrypt your word or sentence.

Outputs:
-------------
The text(str) after cipher.

Example:
-------------
>>> text = 'K'
>>> shift = 1
>>> m = cipher(a, b)
>>> print(m)
L
'''

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

