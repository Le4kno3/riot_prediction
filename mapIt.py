import sys
import pyperclip
import webbrowser
import requests

#demo requests and execption handling is the page is non found
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

#var = raw_input("")
#print "you entered this text: ", var

#test
#print sys.argv[1:]

if len(sys.argv) > 1:
	#join a list, omiting the first element argv[0] it is the file name
	address = ' '.join(sys.argv[1:])
else:
	#get the arguments from clipboard
	address = pyperclip.paste()	

#temp_list = list(sys.argv)
#del temp_list[0]
#myList = '+'.join(map(str, temp_list)) 



