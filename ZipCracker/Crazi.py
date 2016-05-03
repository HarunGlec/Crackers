import zipfile
import optparse

def extractFile(file, password):
	try:
		file.extractall(pwd=password)
		return password
	except:
		return
def main():
	parser = optparse.OptionParser("usage "+"-f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest='zname', type='string',help='specify zip file')
	parser.add_option('-d', dest='dname', type='string',help='specify dictionary file')
	(options, args) = parser.parse_args()

	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		dname = options.dname

	file = zipfile.ZipFile(zname)
	passFile = open(dname)
	for line in passFile.readlines():
		password = line.strip('\n')
		guess = extractFile(file,password)
		if guess:
			print '[+] Password = ' + password + '\n'
			exit(0)
if __name__ == '__main__':
	main()