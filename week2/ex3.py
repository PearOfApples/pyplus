from netmiko import ConnectHandler
from datetime import datetime
cisco3 = {
  'host' : 'cisco3.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_ios'
}

conn = ConnectHandler(**cisco3)
for cmd in ['show version', 'show lldp neighbors']:
  print(conn.send_command(cmd, use_textfsm=True))
conn.disconnect()
