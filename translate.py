#!/usr/bin/env python
import string
import sys


def decide(input):
    """
    Check content type by the first character.
    < - decrypted, return True
    x - encrypted, return False
    """
    decision = {'<': True, 'x': False}
    try:
        first = input[0]
        return decision[first]
    except:
        raise ValueError("Input file is invalid.")


def make_table(do_encrypt=True):
    original = ''.join([chr(i) for i in range(0, 128)])
    encrypted = ''.join([chr(i * 2 % 127) for i in range(0, 128)])
    if do_encrypt:
        return string.maketrans(original, encrypted)
    else:
        return string.maketrans(encrypted, original)


if __name__ == '__main__':
    input = sys.stdin.read()
    output = input.translate(make_table(decide(input)))
    sys.stdout.write(output)
