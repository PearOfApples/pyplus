from netmiko import ConnectHandler

cisco4 = {
  'host' : 'cisco4.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_ios'
}

conn = ConnectHandler(**cisco4)
out = conn.send_command_timing('ping')
out += conn.send_command_timing('\n')
out += conn.send_command_timing('8.8.8.8')
out += conn.send_command_timing('\n')
out += conn.send_command_timing('\n')
out += conn.send_command_timing('\n')
out += conn.send_command_timing('\n')
out += conn.send_command_timing('\n')
conn.disconnect()

print(out)
