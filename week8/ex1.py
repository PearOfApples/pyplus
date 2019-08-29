from jnpr.junos import Device
from pprint import pprint

srx2 = {
  'host' : 'srx2.lasthop.io',
  'user' : 'pyclass',
  'password' : '88newclass'
}

dev = Device(**srx2)
dev.open()
pprint(dev.facts)
print(dev.facts['hostname'])
