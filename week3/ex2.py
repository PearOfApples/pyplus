from netmiko import ConnectHandler
from datetime import datetime
from pprint import pprint
import yaml
cisco3 = {
  'host' : 'cisco3.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_ios'
}
cisco4 = {
  'host' : 'cisco4.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'cisco_ios'
}
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

devlist = [cisco3, cisco4, nxos1, nxos2]
pprint(devlist)
yaml.dump(devlist, open('ex2.yml', 'w'))
