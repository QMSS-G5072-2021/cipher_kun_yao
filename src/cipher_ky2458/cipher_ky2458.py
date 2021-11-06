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

'''
The function: The Caesar cipher is one of the simplest and most widely known encryption techniques. In short, each letter is replaced by a letter some fixed number of positions down the alphabet. Apparently, Julius Caesar used it in his private correspondence.

Inputs: 'text'(str) means the word or sentence that you want to encrypt. 'shift'(int) means the direction and position you want to encrypt your word or sentence.
Outputs: the text(str) after cipher.

Example: 
>>> text = 'K'
>>> shift = 1
>>> m = cipher(a, b)
>>> print(m)
L
'''