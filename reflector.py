#!/usr/bin/env python
# -*- coding: utf-8 -*-

from alphabet_indices import AlphabetIndices


class Reflector:

    def __init__(self, name=None):
        if name == 'B':
            encoding = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

        elif name == 'C':
            encoding = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

        else:
            encoding = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

        self.char2int = AlphabetIndices.char2int
        self.int2char = AlphabetIndices.int2char

        self.forwardWiring = self.decodeWiring(encoding)


    def decodeWiring(self, encoding:str):
        charWiring = list(encoding)
        # wiring = [self.char2int[c] for c in character_wiring]
        wiring = [self.char2int[c] for c in charWiring]
        return wiring


    def forward(self, char:int):
        crypt_char = self.forwardWiring[char]
        return crypt_char
