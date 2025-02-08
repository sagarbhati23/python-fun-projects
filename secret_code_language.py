import random
import string

'''
Use the rules below to translate normal English into secret code language:
Encoding:
1. If the word contains atleast 3 characters, remove the first letter and append it at the end
    now append three random characters at the starting and the end.
2. If the word contains less than 3 characters, simply reverse the string

Decoding:
1. If the word contains less than 3 characters, reverse it.
2. If the word contains atleast 3 characters, remove 3 random characters from start and end.
    Now remove the last letter and append it to the beginning.

User will be asked whether to encode or decode the message.
'''

def encode_message(message):
    words = message.split()
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
    return " ".join(coded) # Return the encoded message

def decode_message(message):
    words = message.split()
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
    return " ".join(decoded) # Return the decoded message

def main():
    # Ask user whether to encode or decode
    code_or_decode = int(input("Enter 1 for encode and 0 for decode: "))
    message = input("Enter your message: ") # Get the user's message to encode or decode
    
    if code_or_decode == 1:
        print(encode_message(message))
    else:
        print(decode_message(message))

if __name__ == "__main__":
    main()










































