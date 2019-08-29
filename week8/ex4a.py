from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.op.routes import RouteTable

srx2 = {
  'host' : 'srx2.lasthop.io',
  'user' : 'pyclass',
  'password' : '88newclass'
}

dev = Device(**srx2)
dev.open()

print(RouteTable(dev).get().items())
