from netmiko import ConnectHandler

cisco3 = { 'host' : 'cisco3.lasthop.io', 'username' : 'pyclass', 'password' : '88newclass', 'device_type' : 'cisco_ios', 'session_log' : 'cisco3.log' }

conn = ConnectHandler(**cisco3)
print(conn.send_command('show version'))
