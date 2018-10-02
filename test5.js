##outputs source code of url

from urllib.request import *
import sys

def main(arg):
	try:
		url = str(arg[1])
		
		headers = {}
		headers['user-Agent'] = 'Mozilla/5.0 (X11; Linux i686)'
		
		req = Request(url, headers = headers)
		resp = urlopen(req)	
		respData = resp.read()
		
		## apply re.findall function on respData
		
		saveFile = open('output_file.txt', 'w')
		saveFile.write(str(respData))
		saveFile.close()
		print("output saved in cwd")

	except Exception as e:
		print(str(e))
	
main(sys.argv)
