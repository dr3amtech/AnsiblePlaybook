import os
import sys
import pathlib
import fileinput
import json

debug=True


def main(argv):
	chestCreator(agrv)
	schemacreation(agrv)

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
		#todo size may be updating txt file
		if os.stat('checker.txt').st_size==0:
			if installServer  == 'True':
				#install and verify
				os.chdir('/usr/ports/databases/postgresql96-server')
				if os.system(' make -DBATCH install') == 0:
					print('Server installed successful')
					if enablesysrc:
						#todo if its start at runtime we need to handle the start time 
						os.system('sysrc postgresql_enable=yes')
					#start service
					if os.system('service postgresql start') == 0:
						print('Postgresql service started')
					else:
						print('Error starting service')
						exit()
				else:
					print('Error installing postgres')
					sys.exit()
			#unlockChest()
			if installClient == 'True':
				#cd and cd - back to previous dir
				os.chdir('cd /usr/ports/databases/postgresql96-client')
				if os.system('make -DBATCH install') == 0:
					print('Client installed successful')
				else:
					unlockChest ()
					print('Error installing Client')
					exit()
		else:
			unlockChest ()
			print('postgres sql already installed')


def schemacreation():
	os.system('psql -f /usr/home/jenkins/functions.sql -d <database>')
			
def unlockChest ():
	print('Not unlocked yet')
	os.remove('checker.txt')
	#text_replace=''
	#remote configuration
	#os.system('/usr/ports/databases/nano make install clean')
	#X_file = fileinput.FileInput('/var/db/postgres/data96/postgresql.conf',inplace=True,bakup='.bak') as file:
	#	for line in file:
	#		print(line.replace())
	
	


if __name__ == '__main__':
	sys.exit(main(sys.argv))

