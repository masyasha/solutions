# channel.zip using here can be found here: 'www.pythonchallenge.com/pc/def/channel.zip'

import re
import zipfile

nothingCounter = "90052"
comments = []

with zipfile.ZipFile("channel.zip") as zpfile:

	timer = len(zpfile.infolist())

	for i in range(timer - 1):

		data = zpfile.read(nothingCounter + ".txt").decode("utf-8")

		comments.append((zpfile.getinfo(nothingCounter + ".txt").comment).decode("utf-8"))
	
		nothingCounter = "".join(re.findall("[\d?]", data))

		if nothingCounter == '':
			break

		print(data)
	print("".join(comments))
	
