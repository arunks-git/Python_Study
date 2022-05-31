from netmiko import ConnectHandler

device_test = {
	'device_type': 'juniper',
	'host':   '10.219.38.6',
	'username': 'labroot',
	'password': 'lab123',
	'port' : 22,
}


net_connect = ConnectHandler(**device_test)
output = net_connect.send_command('show version')
print(output)

con = True
while con:
	next_command = input("Enter the command" )
	print(next_command)
	try:
		if next_command != 'exit':
			output = net_connect.send_command(next_command)
			print(output)
		else:
			net_connect.disconnect()
			con = False
	except:
		print("Invalid command")

