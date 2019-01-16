import json
from collections import OrderedDict

def Numbus_Header(j,filwwriter):
	for key,value in j.items():
		filewriter.write(key+' '+value+'\n')
def Numbus_events(j,filwwriter):
	print('Numbus_Event')
	filewriter.write('events {\n')
	for key, value in j.items():
		filewriter.write(key+" "+value+'\n')
	filewriter.write('}\n')
def Numbus_http(j,filwwriter):
	print('Numbus_Http')
	filewriter.write('http {\n')
	for key, value in j.items():
		if key == 'servers':
			Servers(value,filewriter)
		if key == 'include':
			print('include')
			include_configuration(value,filewriter)
		if key == 'upstream':
			print('upstream!!!!!!!!!!!')
			upstream(value,filewriter)
		else:
			try:
				print('inside of values that do not have a custom request')
				print(value)
				filewriter.write(key+" "+value+'\n')
			except:
				for x in value:
					print(x)
	filewriter.write('}\n')
def Servers(value,filewriter):
	for l_values in value:
		#print(l_values)
		filewriter.write('server {\n')
		for t_keys,t_values in l_values.items():
			if 'location' in t_keys:
				#print('True')
				include_location(t_values,filewriter)
			else:
				#print(l_values)
				filewriter.write(t_keys+" "+t_values+'\n')
		filewriter.write('}\n')
	#print(value)
def include_location(t_values,filewriter):
	filewriter.write('location{\n')
	#print(t_values)
	#print (type(t_values))
	for l_values in t_values:
		filewriter.write('{\n')
		for key,values in l_values.items():
			filewriter.write(str(key)+" "+str(values)+'\n')
		filewriter.write('}\n')
	filewriter.write('}\n')
def upstream(t_values,filewriter):
	print('upstream')
	print(t_values)
	print(t_values.items())
	for x in t_values:
		print(x)
	for t_keys,t_values in t_values.items():
		if t_keys == 'server_list':
			for th_keys, th_values in t_values[0].items():
				filewriter.write(th_keys+th_values+'\n')
		else:
			filewriter.write(t_keys+" "+t_values+'\n')
def include_configuration(value,filewriter):
	for l_values in value:
		filewriter.write('include'+" "+l_values+"\n")
	
json_loader=open('<Path>')
data=json.load(json_loader)
json_loader.close() #close file

Numbus_Header=data['Numbus_Header']
Numbus_Event=data['Numbus_Event']
Numbus_Http=data['Numbus_HTTP']


print('Numbus Header!!!!!!!!!!!!')
print(Numbus_Header)
print('Numbus Event')
print(Numbus_Event)
print('Numbus_Http')
print(NUmbus_Event)	
#copy old configuration file 
#shutil .copyfile('C:\\users\\joshu\\git\\nginxtest.conf','C:\\users\joshu\\git\\nginctest.conf.bak')

filewriter= open('<Path>','w')


#update file
for i, j in data.items():
	if i == 'Numbus_Header':
		Numbus_Header(j,filewriter)
	if i ==  'Numbus_events':
		Numbus_events(j,filewriter)
	if i == 'Numbus_http':
		Numbus_http(j,filewriter)
		
filewriter.close()