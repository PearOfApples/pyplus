from netmiko import ConnectHandler

nxos1 = { 'host' : 'nxos1.lasthop.io', 'username' : 'pyclass', 'password' : '88newclass', 'device_type' : 'cisco_nxos' }
nxos2 = { 'host' : 'nxos2.lasthop.io', 'username' : 'pyclass', 'password' : '88newclass', 'device_type' : 'cisco_nxos' }

for device in [nxos1, nxos2]:
  conn = ConnectHandler(**device)
  print(conn.find_prompt())

