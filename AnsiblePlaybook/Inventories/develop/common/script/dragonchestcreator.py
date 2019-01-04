import os
import sys
import pathlib
import fileinput

debug=True

def chestCreator(agrv):
	installClient=sys.argv[1]
	installServer=sys.argv[2]
	enablesysrc=sys.argv[3]
	if debug:
		print(installClient)
		print(installServer)
		print(enablesysrc)
		print(os.getcwd())
	#is system software installed
	#todo check for version
	os.system('pkg info postgresql96-server >> checker.txt')
	if pathlib.Path("checker.txt").is_file() :
		if os.stat('checker.txt').st_size>0:
			#TOdo
			if installServer is 'True':
				#install and verify
				if os.system('cd /usr/ports/databases/postgresql96-server && make install clean') == 0:
					print('Server installed successful')
					if enablesysrc:
						#todo if its start at runtime we need to handle the start time 
						os.system('sysrc postgresql_enable=yes')
					#start service
					if os.system('service postgresql start') == 0:
						print('Postgresql service started')
					else:
						print('Error starting service')
						unlockChest ()
						exit()
				else:
					print('Error installing postgres')
					unlockChest ()
					exit()
			#unlockChest()
			if installClient is True:
				#cd and cd - back to previous dir
				if os.system('cd /usr/ports/databases/postgresql96-client && make install clean') == 0:
					print('Client installed successful')
				else:
					unlockChest ()
					print('Error installing Client')
					exit()
		print('postgres sql already installed')
def unlockChest ():
	print('Not unlocked yet')
	os.remove(checker.txt)
	#text_replace=''
	#remote configuration
	#os.system('/usr/ports/databases/nano make install clean')
	#X_file = fileinput.FileInput('/var/db/postgres/data96/postgresql.conf',inplace=True,bakup='.bak') as file:
	#	for line in file:
	#		print(line.replace())


if __name__ == '__main__':
	sys.exit(chestCreator(sys.argv))

