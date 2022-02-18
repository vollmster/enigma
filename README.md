# enigma
Python implementation of the enigma machine

This is a Python implementation of Prof. Mike Pound's Java based project as featured on the Computerphile YouTube channel: https://github.com/mikepound/enigma

To run the program from the command line use ```python enigma.py```. This will initialize the enigma machine with default settings for you to test.
To try out additional options, use ```python enigma.py --help``` to get the full range of user configurable settings. As a basic example, you can set rotors, rotor positions, ring settings, reflector, and the plugboard using the appropriate command line flags: 

```python enigma.py -rot "II V III" -pos "7 4 19" -ring "12 2 20" -plug "AF TV KO BL RW" -ref B```

Pay attention to the quoting as it's necessary for parsing the entered strings into lists for the program.
