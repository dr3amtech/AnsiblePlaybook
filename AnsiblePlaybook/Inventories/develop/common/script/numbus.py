import os
import pathlib
import sys
import json
import shutil



debug=True



def main():
	print('Creating  Numbus')
	createRedmine()
	createNumbus()
	

def createNumbus():
	print('Installing  Nginx')
	installRequest('nginx')
	installRedmine
	configureNginxOnStart()
	configureNumbus()
	
def createRedmine():
	print('Installing Redmine')
	installRequest('redmine')
	
def installRequest(tech):
	tech()
	if os.system('pkg info '+tech+'>> checker.txt') == 0:
		if pathlib.Path('checker.txt').is_file():
			print('File was found')
			if os.stat('checker.txt').st_size==0:
			#install Nginx
				print('Install '+tech)
				os.chdir('/usr/ports/www/'+tech+'/')
				if debug:
					print(os.getcwd())
				if os.system('make -DBATCH install') ==0:
					print(tech+' install Successfully')
				else:
					print('Error installing '+tech)
					sys.exit()
			else:
				print(tech+' Already Installed')
		else:
			print('File not found')
	else:
		print('Issue writing to checker file')
	

def configureNumbus():
	#Collect Json proxy configuration from numusproxy.conf
	json_loader=open('/home/jenkins/Configure_Jenkins_Agent/AnsiblePlaybook/development/AnsiblePlaybook/AnsiblePlaybook/Inventories/develop/common/script/Prop/numbus.json')
	data=json.load(json_loader)
	json_loader.close() #close file
	
	#copy old configuration file 
	shutil .copyfile('/usr/local/etc/nginx/nginx.conf','/usr/local/etc/nginx/nginx.conf.bak')
	 

	#Go to /usr/local/etc/nginx/nginx.conf:
	os.chdir('/usr/local/etc/nginx/')


	#open file
	filewriter=  open('/usr/local/etc/nginx/nginx.conf','w')
	fileWriter_proxy= open('C:\\Users\joshu\\git\\proxy.conf','w')
	
	Numbus_Headers=data['Numbus_Header']
	Numbus_Events=data['Numbus_Events']
	Numbus_HTTP=data['Numbus_HTTP']

	json_loader=open('/home/jenkins/Configure_Jenkins_Agent/AnsiblePlaybook/development/AnsiblePlaybook/AnsiblePlaybook/Inventories/develop/common/script/Prop/numbus.jsonproxy.json')
	data_proxy =json.load(json_loader)
	json_loader.close()
	
	configureProxy(data_proxy,fileWriter_proxy)
	handleNumbusHeaderrequest(Numbus_Headers,fileWriter)
	handleNumbusEvents(Numbus_Events,fileWriter)
	handleNumbusHeaderHTTPrequest(Numbus_HTTP,fileWriter)
	
	#close filewriter:
	filewriter.close()
	
	#reload nginx. nginx -s reload
	if os.system('service nginx start')== 0:
		print('Nginx Started Successfully')
	else:
		print(Error Starting Nginx)
		sys.exit()


def handleNumbusHeaderrequest(Numbus_Headers,fileWriter):
	#print(Numbus_Headers)
	for l_headers,l_values in Numbus_Headers.items():
		fileWriter.write(l_headers+' '+l_values+'\n')

		
def handleNumbusEvents(Numbus_Events,fileWriter):
	#print(Numbus_Events)
	fileWriter.write('events {\n')
	for l_events,l_values in Numbus_Events.items():
		fileWriter.write(l_events+' '+l_values)
	fileWriter.write('\n}')
	
	
def handleNumbusHeaderHTTPrequest(Numbus_HTTP,fileWriter):
	#print(Numbus_HTTP)
	#doing this to keep in order for configuration file to exact i do not want to restrcure the code to fit my needs
	fileWriter.write('http {\n')
	upstream=Numbus_HTTP['upstream']
	servers=Numbus_HTTP['servers']
	lib_conf=Numbus_HTTP['include']
	Numbus_HTTP.pop('upstream')
	Numbus_HTTP.pop('servers')
	Numbus_HTTP.pop('access_log')
	Numbus_HTTP.pop('include')
	
	for l_include in lib_conf:
		fileWriter.write('include '+l_include+'\n')
	
	
	for keys, values in Numbus_HTTP.items():
		fileWriter.write('\n'+keys+' '+values+'\n')
	
	for keys,values in upstream.items():
		fileWriter.write(keys+' {\n')
		for t_values in values:
			for th_keys ,th_values in t_values.items():
				fileWriter.write(th_keys+th_values+'\n')
	fileWriter.write('}')		
	
	for l_servers in servers:
		fileWriter.write('server {\n')
		for keys,values in l_servers.items():
			print('Keys :'+ keys)
			if 'location' in keys:
				fileWriter.write( keys+ '{\n')
				for i in values:
					for t_keys, t_values in i.items():
						fileWriter.write(t_keys+' '+t_values+'\n')
				fileWriter.write('}\n')	
			else:
				fileWriter.write(keys+' '+values+'\n')
		fileWriter.write('}')
		
	
	fileWriter.write('}')
	
	
def configureProxy(data_proxy,fileWriter_proxy):
	configuration = data_proxy['proxy_configuration']
	for keys,values in configuration.items():
		fileWriter_proxy.write(keys+' '+str(values)+'\n')
	
	fileWriter_proxy.close()

def configureNginxOnStart():
	#open file
	filewriter=  open('/etc/rc.conf','a')
	filewriter.write('nginx_enable=YES')
	
if __name__=='__main__':
	sys.exit(main())