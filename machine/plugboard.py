#!/usr/bin/env python
# -*- coding: utf-8 -*-

from alphabet_indices import AlphabetIndices


class Plugboard:

    # Example connections
    # AF TV KO BL RW

    def __init__(self, connections):

        self.char2int = AlphabetIndices.char2int
        self.int2char = AlphabetIndices.int2char

        self.wiring = self.decodePlugboard(connections)


    def forward(self, char:int):
        crypt_char = self.wiring[char]
        return crypt_char


    def identityPlugboard(self,):
        mapping = [i for i in range(0,26)]
        return mapping


    def getUnpluggedCharacters(self, plugsettings:str):
        unpluggedCharacters = set([i for i in range(0,26)])
        if plugsettings=='':
            return unpluggedCharacters

        pairings = plugsettings.split(' ')
        pairings = [p for p in pairings if p!='']
        for pair in pairings:
            c1 = self.char2int[pair[0]]
            c2 = self.char2int[pair[1]]
            unpluggedCharacters.remove(c1)
            unpluggedCharacters.remove(c2)

        return unpluggedCharacters


    def decodePlugboard(self, plugsettings:str):
        if plugsettings == None or plugsettings == "":
            mapping = self.identityPlugboard()
            return mapping

        pairings = plugsettings.split(' ')
        pairings = [p for p in pairings if p!='']
        # print(pairings)
        mapping = self.identityPlugboard()
        pluggedCharacters = set()

        for pair in pairings:
            if len(pair) != 2:
                return self.identityPlugboard()

            c1 = self.char2int[pair[0]]
            c2 = self.char2int[pair[1]]

            if c1 in pluggedCharacters or c2 in pluggedCharacters:
                return self.identityPlugboard()

            pluggedCharacters.add(c1)
            pluggedCharacters.add(c2)

            mapping[c1] = c2
            mapping[c2] = c1

        return mapping
