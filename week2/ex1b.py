from netmiko import ConnectHandler

cisco4 = {
  'host' : 'cisco4.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_ios'
}

conn = ConnectHandler(**cisco4)
out = conn.send_command('ping', expect_string='Protocol')
out += conn.send_command('\n', expect_string='Target IP')
out += conn.send_command('8.8.8.8', expect_string='Repeat')
out += conn.send_command('\n', expect_string='Datagram')
out += conn.send_command('\n', expect_string='Timeout')
out += conn.send_command('\n', expect_string='Extended')
out += conn.send_command('\n', expect_string='Sweep')
out += conn.send_command('\n', expect_string='#')
conn.disconnect()

print(out)
