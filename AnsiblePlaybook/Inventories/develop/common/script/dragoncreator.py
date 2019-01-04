import os
import sys
import pathlib

debug=True



def androidConfiguration(argv):
	add_int_conf=True
	createJail=sys.argv[1]
	cloneJail=sys.argv[2]
	if debug:
		print(os.getcwd()) 
	os.system('cd /')
	os.system('pkg info ezjail >> ezjail.txt')
	if debug:
		os.system('echo /etc/rc.conf')
		os.system('')
	X_file = open('/etc/rc.conf','r')
	print(X_file)
	X_file = X_file.read().split('\n')
	#is ezjail install
	if not pathlib.Path("ezjail.txt").is_file() :
		#Check configuration and add configuration
		print('Install ezjail and create first Jail')
		for i in X_file:
			if 'cloned_interface'in i :
				print(i) 
				print('Configuration Already Completed')
				add_int_conf=False
				break
		if add_int_conf:
			print('Adding configuration')
			WX_file= open('/etc/rc.conf','a')
			WX_file.write('cloned_interfaces=\'l01\'')
			WX_file.close()
		os.system('/usr/ports/sysutils/ezjail make install')
		ezjail(createJail,cloneJail)

def ezjail(createJail,cloneJail):
	if pathlib.Path("ezjail.txt").is_file() :
		print('File Found there is no need to create Jail')
		if createJail:
			print('Creating Jail')
			os.system('Ansible-playbook JailMaker2.yml')
		if cloneJail:
			print('Cloning Jail')
			os.sys('ansible-playbook CloneJailMaker.yml')

if __name__=='__main__':
	sys.exit(androidConfiguration(sys.argv))
	
