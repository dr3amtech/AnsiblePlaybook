import os
import sys
import pathlib

debug=True



def androidConfiguration(argv):
"""
createJail=bool
clonejail=bool
ip_address=string

"""
	add_int_conf=True
	createJail=sys.argv[1]
	cloneJail=sys.argv[2]
	ip_adress=sys.argv[3]
	if debug:
		print(os.getcwd()) 
		print(createJail)
		print(cloneJail)
		print(ip_adress)
	#navigate to base directory
	os.system('cd /')
	os.system('pkg info ezjail >> checker.txt')
	X_file = open('/etc/rc.conf','r')
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
				WX_file= open('/etc/rc.conf','a')
				WX_file.write('cloned_interfaces=\'l01\'')
				WX_file.close()
			if os.system('cd /usr/ports/sysutils/ezjail && make install clean') ==0:
				print("Successful")
			else:
				print('Error installing ezjail')
				exit(1)
			ezjail(createJail,cloneJail,ip_adress)
		else:
			print('ezjail may already be installed')
		os.remove('checker.txt')

def ezjail(createJail,cloneJail,ip_adress):
	print('Creating File')
	if createJail =='True':
		print('Creating Jail')
		#should we be creating same services on every server
		if os.system('ezjail-admin create  gohan \'l01|127.0.0.1,em0|{ip_adress}\'') == 0:
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
	sys.exit(androidConfiguration(sys.argv))
	
