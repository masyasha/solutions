# programm of translating text from 'http://www.pythonchallenge.com/pc/def/map.html'

import string

letters = list(string.ascii_lowercase)
alphabetLen = len(string.ascii_lowercase)
shift = 2

inputString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
outputString = ""

for inputChar in inputString:
	try:
		if letters.index(inputChar) + shift > alphabetLen - 1:
			shift = shift - alphabetLen
		outputChar = letters[letters.index(inputChar) + shift]
	except:
		outputChar = inputChar

	outputString += outputChar

print '\n\n', outputString, '\n\n'
