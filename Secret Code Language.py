'''
Use the rules below to translate normal English into secret code language

Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end
now append three random characters at the starting and the end
else:
simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it
else:
remove 3 random characters from start and end. Now remove the last letter and append it to
the beginning

Your program should ask whether you want to code or decode
'''

import random
import string

# Ask user whether to encode or decode
code_or_decode = int(input("Enter 1 for encode and 0 for decode: "))
message = input("Enter your message: ") # Get the user's message to encode or decode
words = message.split()  # Split the message into words

if code_or_decode == 1:
    coded = []
    for word in words:
        if len(word) >= 3:
            # Add 3 random characters at the beginning and end of the word
            r1 = ''.join(random.choices(string.ascii_letters, k=3)) 
            r2 = ''.join(random.choices(string.ascii_letters, k=3))
            stnew = r1 + word[1:] + word[0] + r2 # Form the encoded word
            coded.append(stnew)
        else: 
            # Reverse short words (less than 3 characters)
            coded.append(word[::-1])
    print(" ".join(coded)) # Print the encoded message
    
else: 
    decoded = []
    for word in words:
        if len(word) >= 3:
            # Remove 3 characters from both ends and shift the last letter to the beginning
            stnew = word[3:-3] 
            stnew = stnew[-1] + stnew[:-1] # Form the decoded word
            decoded.append(stnew)
        else: 
            # Reverse short words (less than 3 characters)
            decoded.append(word[::-1])
    print(" ".join(decoded)) # Print the decoded message










































