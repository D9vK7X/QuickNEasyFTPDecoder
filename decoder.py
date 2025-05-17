#!/usr/bin/env python3 
import argparse
import sys

ALPHABET = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ '

def verifyASCII(message):
    try:
        for letter in message:
            ALPHABET.index(letter)
    except ValueError:
        return False
    return True
        
def encode(message):
    length = len(message)
    cipher = ""
    for i in range(length):
        if i < length//2:
            index = ALPHABET.index(message[i*2+1])
        else:
            index = ALPHABET.index(message[(i-length//2)*2])
        letter = ALPHABET[(index+length+i)%len(ALPHABET)]
        cipher += letter
    return cipher

def decode(cipher):
    length = len(cipher)
    list = [None]*length
    for i in range(length):
        index = ALPHABET.index(cipher[i])
        letter = ALPHABET[(index-length-i)%len(ALPHABET)]
        if i < length//2:
            list[i*2+1] = letter
        else:
            list[(i-length//2)*2] = letter
    message = ''.join(list)
    return message

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="Encode or decode the following message", choices=["encode","decode"])
    parser.add_argument("message", help="String that will be en- or decoded. Must only contain printable ascii characters")
    args = parser.parse_args()
    if not verifyASCII(args.message):
        print("Message contains characters outside the alphabet")
        return 1
    if args.action == "encode":
        print(encode(args.message))
    elif args.action == "decode":
        print(decode(args.message))
    else:
        print(f'Action {args.action} not implemented yet')
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())