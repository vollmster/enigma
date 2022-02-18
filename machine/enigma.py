#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from alphabet_indices import AlphabetIndices
from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard



class Enigma:

    def __init__(self,
                 rotors=None,
                 rotorPositions=None,
                 ringSettings=None,
                 plugboardConnections=None,
                 reflector_name=None):

        self.char2int = AlphabetIndices.char2int
        self.int2char = AlphabetIndices.int2char

        if rotors == None:
            rotors=['I','II','III']

        if rotorPositions == None:
            rotorPositions=[0,0,0]

        if ringSettings == None:
            ringSettings=[0,0,0]

        if plugboardConnections == None:
            plugboardConnections = 'AF TV KO BL RW'

        self.leftRotor = Rotor(rotor_name=rotors[0],
                               rotor_position=rotorPositions[0],
                               ring_setting=ringSettings[0])

        self.middleRotor = Rotor(rotor_name=rotors[1],
                                 rotor_position=rotorPositions[1],
                                 ring_setting=ringSettings[1])

        self.rightRotor = Rotor(rotor_name=rotors[2],
                                rotor_position=rotorPositions[2],
                                ring_setting=ringSettings[2])

        self.reflector = Reflector(name=reflector_name)
        self.plugboard = Plugboard(plugboardConnections)


    def rotate(self,):
        if self.middleRotor.isAtNotch():
            self.middleRotor.turnover()
            self.leftRotor.turnover()

        elif self.rightRotor.isAtNotch():
            self.middleRotor.turnover()

        self.rightRotor.turnover()


    def encrypt(self, char:int):
        self.rotate()
        # Plugboard in
        c1 = self.plugboard.forward(char)

        # Right to left
        c2 = self.rightRotor.forward(c1)
        c3 = self.middleRotor.forward(c2)
        c4 = self.leftRotor.forward(c3)

        # Reflector
        c5 = self.reflector.forward(c4)

        # Left to right
        c6 = self.leftRotor.backward(c5)
        c7 = self.middleRotor.backward(c6)
        c8 = self.rightRotor.backward(c7)

        # Plugboard out
        c9 = self.plugboard.forward(c8)
        return c9


def loadTxtDoc(path):
    with open(path, 'r', encoding='utf8') as f:
        lines = f.read().splitlines()
    line = ''.join(lines)
    return line


def main():
    parser = argparse.ArgumentParser(description="Run fine-grained NER over a txt document collection")
    parser.add_argument('-rot','--rotors',
                        default='II V III',
                        help='Three rotors to use from numerals I to V, install left to right e.g "II V III"',)
    parser.add_argument('-pos','--positions',
                        default='7 4 19',
                        help='Three initial positions for rotors, left to right e.g. "7 4 19" ')
    parser.add_argument('-ring', '--ring_setting',
                        default='12 2 20',
                        help='Ring settings for rotors (causes an index shift) left to right e.g. "12 2 20" ')
    parser.add_argument('-plug', '--plugboard',
                        default='AF TV KO BL RW',
                        help='Plugboard letter pairs to swap e.g. "AF TV KO BL RW" ')
    parser.add_argument('-ref', '--reflector',
                        choices={'A', 'B', 'C',},
                        default='B',
                        help='Rotor reflector to use. "A" is a non-shifted default that doesn\'t improve encyption.')
    parser.add_argument('-f','--file_input',
                        action='store_true',
                        help='If passed, user can enter a text file to load and encrypt/decrypt e.g. "./my_message.txt" ')
    args = parser.parse_args()


    rotors = args.rotors.split(' ')
    # positions = args.positions.split(' ')
    positions = [int(p) for p in args.positions.split(' ')]
    # ring_setting = args.ring_setting.split(' ')
    ring_setting = [int(s) for s in args.ring_setting.split(' ')]
    plugboard = args.plugboard
    reflector = args.reflector


    settings_message = ('\nEnigma Settings: \n'
                        '=========================\n'
                        'Rotors: {}\n'
                        'Rotor Positions: {}\n'
                        'Ring Settings: {}\n'
                        'Plugboard Connections: {}\n'
                        'Reflector: {}\n').format(rotors,
                                                  positions,
                                                  ring_setting,
                                                  plugboard,
                                                  reflector)

    print(settings_message)


    enigma = Enigma(rotors=rotors,
                    rotorPositions=positions,
                    ringSettings=ring_setting,
                    plugboardConnections=plugboard,
                    reflector_name=reflector)

    if args.file_input:
        input_file = input('Please enter a text file to load and encrypt/decrypt e.g. "./my_message.txt": ')
        input_text = loadTxtDoc(input_file)

    else:
        input_text = input('Please input a message to encrypt/decrypt (all uppercase and no spaces): ')

    input_text = input_text.upper()
    input_text = input_text.replace(' ','')
    print('\nYour input to encrypt/decrypt: {}\n'.format(input_text))

    input_text = list(input_text)
    # print(message_text)
    input_text = [enigma.char2int[c] for c in input_text]
    print('\nYour input message in integer array format (0 indexed): {}'.format(input_text))

    output_text = []
    for char in input_text:
        out_char = enigma.encrypt(char)
        output_text.append(out_char)

    print('\nThe encrypted/decrypted message in integer array format: {}'.format(output_text))

    output_text = [enigma.int2char[c] for c in output_text]
    output_text = ''.join(output_text)
    print('\nYour encrypted/decrypted output: {}\n'.format(output_text))


if __name__ == "__main__":
    main()
