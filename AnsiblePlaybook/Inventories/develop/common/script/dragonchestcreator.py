import os
import sys
import pathlib
import fileinput

debug=True

def chestCreator(agrv):
	installClient=[1]
	installServer=[2]
	enablesysrc=[3]
	if debug:
		print(os.getcwd())
	#is system software installed
	if installServer:
		#todo check for version
		os.system('pkg info postgresql96-server >> checker.txt')
		if not pathlib.Path('checker.txt'):
			os.system('/usr/ports/databases/postgresql96-server make install clean')
			if enablesysrc:
				#todo if its start at runtime we need to handle the start time 
				os.system('sysrc postgresql_enable=yes')
			#start service
			os.system('service postgresql start
			os.remove(checker.txt)
			#unlockChest()
	if installClient:
		#todo check for version
		os.system('pkg info postgresql96-server >> checker.txt')
		if not pathlib.Path('checker.txt'):
			#cd and cd - back to previous dir
			os.system('/usr/ports/databases/postgresql96-client make install clean')
			os.remove(checker.txt)
def unlockChest ():
	#text_replace=''
	#remote configuration
	#os.system('/usr/ports/databases/nano make install clean')
	#X_file = fileinput.FileInput('/var/db/postgres/data96/postgresql.conf',inplace=True,bakup='.bak') as file:
	#	for line in file:
	#		print(line.replace())



if __name__ == '__main__':
	sys.exit(chestCreator(sys.argv))