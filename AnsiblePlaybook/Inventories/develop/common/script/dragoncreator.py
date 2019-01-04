import os
import sys
import pathlib

debug=True



def androidConfiguration(argv):
	add_int_conf=True
	createJail=sys.argv[1]
	cloneJail=sys.argv[2]
	ip_adress=sys.argv[3]
	if debug:
		print(os.getcwd()) 
	os.system('cd /')
	os.system('pkg info ezjail >> checker.txt')
	X_file = open('/etc/rc.conf','r')
	print(X_file)
	X_file = X_file.read().split('\n')
	#is ezjail install
	if os.stat('checker.txt').st_stat>0:
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
			WX_file= open('/etc/rc.conf','a')
			WX_file.write('cloned_interfaces=\'l01\'')
			WX_file.close()
		os.system('cd /usr/ports/sysutils/ezjail && make install clean')
		ezjail(createJail,cloneJail)
		os.remove('checker.txt')

def ezjail(createJail,cloneJail,ip_adress):
	print('File Found there is no need to create Jail')
	if createJail:
		print('Creating Jail')
		#should we be creating same services on every server
		if os.system('ezjail-admin create  gohan \'l01|127.0.0.1,em0|{ip_adress}\'') == 0:
			if os.system('service jail start gohan') not 1:
				print('Service did not start')
				exit()
	if cloneJail:
		#create from base jail with zfs
		print('Cloning Jail')
		os.sys('ansible-playbook CloneJailMaker.yml')

if __name__=='__main__':
	sys.exit(androidConfiguration(sys.argv))
	
