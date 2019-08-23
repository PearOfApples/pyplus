from netmiko import ConnectHandler
from datetime import datetime
from time import sleep
cisco4 = {
  'host' : 'cisco4.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_ios',
  'secret' : '88newclass',
  'session_log' : 'ex6.log'
}

conn = ConnectHandler(**cisco4)

print(conn.find_prompt())

print(conn.config_mode())
print(conn.find_prompt())

print(conn.exit_config_mode())
print(conn.find_prompt())

print(conn.write_channel('disable\n'))

sleep(2)
print(conn.read_channel())

print(conn.enable())
print(conn.find_prompt())

conn.disconnect()
