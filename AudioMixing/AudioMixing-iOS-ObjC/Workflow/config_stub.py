import re
import sys
import os

APP_CONFIG_FILE = sys.argv[1]
APP_KEY = sys.argv[2]
STREAM_URL = sys.argv[3]

# Stub a string with a evironment variable
def stubString(searchPattern,rejectPattern,searchtText,replacement,desc):
	searchRet = re.search(searchPattern,searchtText).group()
	if re.search("\"{}\"".format(rejectPattern), searchRet) is not None:
		print "A valid {} is submitted!".format(desc)
		sys.exit(1)

	# Stub valid key and write back
	ret = re.sub('\"\S+\"', "\"{}\"".format(replacement), searchRet)
	ret = re.sub(searchPattern, ret, searchtText)
	return ret

# Read heaer file

io = open(APP_CONFIG_FILE, "r+")
text = io.read()

ret = stubString("kAppKey\s@\"\S*\"", "^[a-f0-9]{32}$", text, APP_KEY, 'APP_KEY')
ret = stubString("kStreamURL\s@\"\S*\"", "(?:rtmp:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+", ret, STREAM_URL, 'STREAM_URL')

io.seek(0)
io.write(ret)
io.truncate()

io.close()
