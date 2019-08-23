from netmiko import ConnectHandler
from datetime import datetime
cisco3 = {
  'host' : 'cisco3.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_ios'
}

cisco3_fast = {
  'host' : 'cisco3.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_ios',
  'fast_cli' : True
}
for dev in [cisco3, cisco3_fast]:
  conn = ConnectHandler(**dev)
  print(datetime.now())
  for cmd in ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']:
    print(conn.send_config_set(cmd))
  print(conn.send_command('ping google.com'))
  conn.disconnect()
  print(datetime.now())
