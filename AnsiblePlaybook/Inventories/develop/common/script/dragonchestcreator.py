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
	#todo check for version
	os.system('pkg info postgresql96-server >> checker.txt')
	if os.stat('checker.txt').st_size>0:
		if installServer:
			#install and verify
			if os.system('/usr/ports/databases/postgresql96-server && make install clean) == 0:
					print('successful')
					if enablesysrc:
						#todo if its start at runtime we need to handle the start time 
						os.system('sysrc postgresql_enable=yes')
					#start service
					os.system('service postgresql start
			else:
				print('Error installing postgres')
				exit()
			#unlockChest()
		if installClient:
			#cd and cd - back to previous dir
			os.system('cd /usr/ports/databases/postgresql96-client && make install clean')
			os.remove(checker.txt)
	os.remove(checker.txt)
	print('postgres sql already installed')
	exit()
def unlockChest ():
	#text_replace=''
	#remote configuration
	#os.system('/usr/ports/databases/nano make install clean')
	#X_file = fileinput.FileInput('/var/db/postgres/data96/postgresql.conf',inplace=True,bakup='.bak') as file:
	#	for line in file:
	#		print(line.replace())



if __name__ == '__main__':
	sys.exit(chestCreator(sys.argv))