# programm for detecting rare symbols in the mass from 'view-source:http://www.pythonchallenge.com/pc/def/ocr.html'

import re

mass = ...  # by that I mean these huge block of symbols

pattern = re.compile('[a-z]')
matches = pattern.findall(mass)

print "".join(matches)
