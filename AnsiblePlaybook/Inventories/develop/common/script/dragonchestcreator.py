import os
import sys
import pathlib
import fileinput
import json

debug=True
#Change to Configuration
installClient=True
installServer=True
enablesysrc=True

def main():
	chestCreator()
	schemacreation()
	neo4jCreation()
	sys.exit(0)

def chestCreator():
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
						sys.exit(1)
				else:
					print('Error installing postgres')
					sys.exit(1)
			#unlockChest()
			if installClient == True:
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
	#os.system('psql db lucille')
	#os.system('psql create user lucille')
	#os.system('psql create user mothership')
	#os.system('grant all privileges on database lucille to lucille')
	os.system('psql -f /usr/home/jenkins/lucille.sql -d lucille')
	os.system('psql -f /usr/home/jenkins/functions.sql -d lucille')
			
def unlockChest ():
	print('Not unlocked yet')
	os.remove('checker.txt')
	#text_replace=''
	#remote configuration
	#os.system('/usr/ports/databases/nano make install clean')
	#X_file = fileinput.FileInput('/var/db/postgres/data96/postgresql.conf',inplace=True,bakup='.bak') as file:
	#	for line in file:
	#		print(line.replace())
	
	
def neo4jCreation():
	os.system('pkg info neo4j >> checker.txt')
	if pathlib.Path("checker.txt").is_file() :
		#todo size may be updating txt file
		if os.stat('checker.txt').st_size==0:
			if installServer  == True:
				#install and verify
				os.chdir('/usr/ports/databases/neo4j')
				if os.system(' make -DBATCH install') == 0:
					print('Server installed successful')
				else:
					print('Error installing neo4j')
					sys.exit(1)

if __name__ == '__main__':
	sys.exit(main())

