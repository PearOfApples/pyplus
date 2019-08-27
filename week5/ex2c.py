import jinja2
from jinja2.environment import Environment
from netmiko import ConnectHandler
from time import sleep

nxos1_dev = {
  'host' : 'nxos1.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_nxos'
}
nxos2_dev = {
  'host' : 'nxos2.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_nxos'
}
 
nxos1 = {
  "interface" : "Ethernet1/1",
  "ip_address" : "10.1.100.1",
  "netmask" : 24,
  "neighbor" : "10.1.100.2",
  "as" : 22
}
nxos2 = {
  "interface" : "Ethernet1/1",
  "ip_address" : "10.1.100.2",
  "netmask" : 24,
  "neighbor" : "10.1.100.1",
  "as" : 22
}

devs = [nxos1_dev, nxos2_dev]
cfg = [nxos1, nxos2]

env = Environment()
env.loader = jinja2.FileSystemLoader('.')
tmpl = env.get_template('ex2c.j2')
for i in range(2):
  conn = ConnectHandler(**devs[i])
  print(conn.send_config_set(tmpl.render(**cfg[i])))
conn = ConnectHandler(**devs[1])
sleep(10)
print(conn.send_command('show ip bgp summary | include {}'.format(cfg[i]['neighbor'])))  
print(conn.send_command('ping {}'.format(cfg[1]['neighbor'])))
