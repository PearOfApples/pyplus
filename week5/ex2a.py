import jinja2
from jinja2.environment import Environment

nxos1 = {
  "interface" : "Ethernet1/1",
  "ip_address" : "10.1.100.1",
  "netmask" : 24
}
nxos2 = {
  "interface" : "Ethernet1/1",
  "ip_address" : "10.1.100.2",
  "netmask" : 24
}

env = Environment()
env.loader = jinja2.FileSystemLoader('.')
tmpl = env.get_template('ex2a.j2')
for var in [nxos1, nxos2]:
  print(tmpl.render(**var))

