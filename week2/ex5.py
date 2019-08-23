from netmiko import ConnectHandler
from datetime import datetime
nxos1 = {
  'host' : 'nxos1.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_nxos'
}
nxos2 = {
  'host' : 'nxos2.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_nxos'
}

for dev in [nxos1, nxos2]:
  conn = ConnectHandler(**dev)
  print(conn.send_config_from_file('ex5.txt'))
  conn.disconnect()
