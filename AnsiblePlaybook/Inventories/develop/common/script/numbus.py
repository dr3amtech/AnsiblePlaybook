import os
import pathlib
import sys



debug=True







def createNumbus():
	print('creating  Numbus')
	
	os.system('pkg info nginx >> checker.txt')
	if pathlib.Path('checker.txt').is_file():
		print('File was found')
		if os.stat('checker.txt').st_size==0:
		#install Nginx
			print('Install Nginx')
			os.chdir('/usr/ports/www/nginx/')
			if debug:
				print(os.getcwd())
			if os.system('make -DBATCH install') ==0:
				print('Nginx install Successfully')
			else:
				print('Error installing nginx')
				exit()
		else:
			print('Nginx Already installed')
	else:
		print('File not found')

def configureNumbus():
	print('Todo')
	


def configureNumnusProxy():
	print('Todo')



	
if __name__=='__main__':
	sys.exit(createNumbus())