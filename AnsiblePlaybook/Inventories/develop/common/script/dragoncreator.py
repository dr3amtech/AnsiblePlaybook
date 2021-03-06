import os
import sys
import pathlib
import json

debug=True

def  configurationCollections():
	print(os.getcwd())
	script_dit=os.path.dirname(__file__)
	absfile=os.path.join(script_dit,'Prop/jail.json')
	with open(absfile) as json_data_file:
		data = json.load(json_data_file)
	return data
	

def androidConfiguration(argv,data):
	"""
	createJail=bool
	clonejail=bool
	ip_address=string

	"""
	add_int_conf=True
	createJail=True
	cloneJail=False
	ip_adress='okay'
	if debug:
		print(data['Jails_file_locations']['config'])
		print(os.getcwd()) 
		print(createJail)
		print(cloneJail)
		print(ip_adress)
	os.system('pkg info ezjail >> checker.txt')
	X_file = open(data['Jails_file_locations']['config'],'r')
	if debug:
		print(X_file)
	X_file = X_file.read().split('\n')
	if pathlib.Path("checker.txt").is_file() :
		#is ezjail install
		if os.stat('checker.txt').st_size==0:
			#Check configuration and add configuration
			print('Install ezjail and create first Jail')
			for i in X_file:
				if 'cloned_interface'in i :
					if debug:
						print(i) 
					print('Configuration Already Completed')
					add_int_conf=False
					break
			if add_int_conf:
				print('Adding configuration')
				WX_file= open(data['Jails_file_locations']['config'],'a')
				WX_file.write('cloned_interfaces=\'l01\'')
				WX_file.close()
			os.chdir('/usr/ports/sysutils/ezjail')
			if os.system('make -DBATCH install')==0:
				print("Successful")
			else:
				print('Error installing ezjail')
				exit(1)
			ezjail(createJail,cloneJail,ip_adress)
		else:
			print('ezjail may already be installed')


def ezjail(createJail,cloneJail,ip_adress):
	print('Creating File')
	if createJail =='True':
		print('Creating Jails')
		#should we be creating same services on every server
		if os.system('ezjail-admin create  gohan \'l01|127.0.0.1,em0|192.168.1.113\'') == 0:
			if os.system('service jail start gohan') == 1:
				print('Service did not start')
				exit()
			else:
				print('Succcessful')
		else:
			print('Error creating jail')
	if cloneJail=='True':
		#create from base jail with zfs
		print('Cloning Jail')
		os.system('ansible-playbook CloneJailMaker.yml')

if __name__=='__main__':
	sys.exit(androidConfiguration(sys.argv,configurationCollections()))
	
