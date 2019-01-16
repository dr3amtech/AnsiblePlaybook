import json








def testOne():
	json_loader=open('C:\\Users\\joshu\\git\\AnsiblePlaybook\\development\\AnsiblePlaybook\\AnsiblePlaybook\\Inventories\\develop\\common\\script\\Prop\\numbus.json')
	data=json.load(json_loader)
	json_loader.close() #close file
	
	
	Numbus_Headers=data['Numbus_Header']
	Numbus_Events=data['Numbus_Events']
	Numbus_HTTP=data['Numbus_HTTP']

	json_loader=open('C:\\Users\\joshu\\git\\AnsiblePlaybook\\development\\AnsiblePlaybook\\AnsiblePlaybook\\Inventories\\develop\\common\\script\\Prop\\proxy.json')
	data_proxy =json.load(json_loader)
	json_loader.close()
	
	fileWriter= open('C:\\Users\joshu\\git\\nginxtest.conf','w')
	fileWriter_proxy= open('C:\\Users\joshu\\git\\proxy.conf','w')
	configureProxy(data_proxy,fileWriter_proxy)
	handleNumbusHeaderrequest(Numbus_Headers,fileWriter)
	handleNumbusEvents(Numbus_Events,fileWriter)
	handleNumbusHeaderHTTPrequest(Numbus_HTTP,fileWriter)













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
	



if __name__=='__main__':
	testOne()