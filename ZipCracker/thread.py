#The 'thread' feature is not stabil#

import zipfile
from threading import Thread

def extractFile(file, password):
	try:
		file.extractall(pwd=password)
		print '[+] Password = ' + password + '\n'
		
	except:
		pass
def main():
	file = zipfile.ZipFile("saveme.zip")
	passFile = open('rockyou.txt')
	for line in passFile.readlines():
		password = line.strip('\n')
		global t
		t = Thread(target=extractFile, args=(file, password))
		t.start()
		
if __name__ == '__main__':
	main()
	