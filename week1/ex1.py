from netmiko import ConnectHandler

nxos1 = { 'host' : 'nxos1.lasthop.io', 'username' : 'pyclass', 'password' : '88newclass', 'device_type' : 'cisco_nxos' }

conn = ConnectHandler(**nxos1)
print(conn.find_prompt())
