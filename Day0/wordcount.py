#!/usr/bin/python

import sys

text = sys.argv[1]

lines = len(text.split('\n')) - 1
words = len(text.split(' ')) - lines
chars = len(text)

print('{:>7}{:>8}{:>8}'.format(lines, words, chars))
