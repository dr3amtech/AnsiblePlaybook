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
			if os.system('cd /usr/ports/www/nginx/') ==0:
				if os.system('make -DBATCH install') ==0:
					print('Nginx install Successfully')
			else:
				print('Error installing nginx')
				exit()
	else:
		print('File was not found, Nginx Must be installed')
			

def configureNumbus():
	print('Todo')
	


def configureNumnusProxy():
	print('Todo')



	
if __name__=='__main__':
	sys.exit(createNumbus())