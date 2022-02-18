#!/usr/bin/env python
# -*- coding: utf-8 -*-

from alphabet_indices import AlphabetIndices


class Rotor:

    def __init__(self,
                 rotor_name=None,
                 rotor_position=0,
                 ring_setting=0):
        if rotor_name == 'I':
            encoding = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
            notch_position = 16
        elif rotor_name == 'II':
            encoding = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
            notch_position = 4
        elif rotor_name == 'III':
            encoding = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
            notch_position = 21
        elif rotor_name == 'IV':
            encoding = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
            notch_position = 9
        elif rotor_name == 'V':
            encoding = 'VZBRGITYUPSDNHLXAWMJQOFECK'
            notch_position = 25

        self.char2int = AlphabetIndices.char2int
        self.int2char = AlphabetIndices.int2char

        self.rotor_name = rotor_name
        self.encoding = encoding
        self.notch_position = notch_position
        self.rotor_position = rotor_position
        self.ring_setting = ring_setting
        self.forwardWiring = self.decodeWiring()
        self.backwardWiring = self.inverseWiring(self.forwardWiring)


    def getName(self,):
        return self.rotor_name


    def getPosition(self,):
        return self.rotor_position


    def decodeWiring(self,):
        character_wiring = list(self.encoding)
        wiring = [self.char2int[c] for c in character_wiring]
        return wiring


    def inverseWiring(self, wiring):
        inverse = [None] * 26
        for i in range(len(wiring)):
            forward = wiring[i]
            inverse[forward] = i
        return inverse


    def encipher(self, char:int, position:int, ring:int, mapping:list):
        # mapping refers to a wiring array
        shift = position - ring
        crypt_char = (mapping[(char + shift + 26) % 26] - shift + 26) % 26
        return crypt_char


    def forward(self, char:int):
        crypt_char = self.encipher(char, self.rotor_position, self.ring_setting, self.forwardWiring)
        return crypt_char


    def backward(self, char:int):
        crypt_char = self.encipher(char, self.rotor_position, self.ring_setting, self.backwardWiring)
        return crypt_char


    def isAtNotch(self,):
        return self.notch_position == self.rotor_position


    def turnover(self,):
        self.rotor_position = (self.rotor_position + 1) % 26
