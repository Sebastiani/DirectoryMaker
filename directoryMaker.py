import os
import shutil
import sys

files = sys.argv[1]

f = open( files, 'r')

for line in f:

	#Process the line to make name of directory, and make directory
	title = line.replace('http://', '')
	title  =  title.split('/')
	
	os.mkdir(title[0])

	#Write the line on the file
	open('file.txt', 'w').write(title[0])
	

	#Duplicate the file above on the current path.
	shutil.copy('file.txt', title[0])
	shutil.copy('imageScraper.py', title[0])
