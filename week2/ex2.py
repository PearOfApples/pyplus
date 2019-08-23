from netmiko import ConnectHandler
from datetime import datetime
nxos2 = {
  'host' : 'nxos2.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_nxos',
  'global_delay_factor' : 2
}

conn = ConnectHandler(**nxos2)
print(datetime.now())
print(conn.send_command_timing('show lldp neighbors detail'))
print(datetime.now())

print(datetime.now())
print(conn.send_command_timing('show lldp neighbors detail', delay_factor = 8))
print(datetime.now())
