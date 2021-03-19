import lib 
import sys

version = 1.0
platform = sys.platform

if len(sys.argv) == 2:
	if sys.argv[1] in ('-v', '--version'):
		print('MFPL {}\nPlatform: {}\nMFPL location = {}\nPython location = {}'.format(version, platform, sys.path[0], sys.path[2]))
	else:
		file = open(sys.argv[1], 'r')
		content = ''
		for i in file:
			content += i
		lib.Interpreter(content).interpret()
elif len(sys.argv) == 1:
	print('MFPL version {}'.format(version))
	while(True):
		content = input('MFPL>> ')
		if content == 'exit()':
			break
		lib.Interpreter(content).interpret()
