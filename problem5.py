import urllib.request
import re

nothing = "12345"

while True:

	response = (urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % nothing)).read()
	print(response)

	nothing = "".join(re.findall("[\d?]", str(response)))

