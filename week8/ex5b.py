from jnpr.junos import Device
from pprint import pprint
from lxml import etree

srx2 = {
  'host' : 'srx2.lasthop.io',
  'user' : 'pyclass',
  'password' : '88newclass'
}

dev = Device(**srx2)
dev.open()

print(etree.tostring(dev.rpc.get_interface_information(terse=True)).decode())

