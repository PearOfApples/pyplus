from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.utils.config import Config
from jnpr.junos.op.routes import RouteTable

srx2 = {
  'host' : 'srx2.lasthop.io',
  'user' : 'pyclass',
  'password' : '88newclass'
}

dev = Device(**srx2)
dev.open()

routeold = RouteTable(dev).get().items()

cfg = Config(dev)
cfg.lock()
cfg.load(path='ex4bcd.cfg', format='text', merge='true')
print(cfg.diff())
cfg.commit()

routenew = RouteTable(dev).get().items()
for route in routenew:
  if route[0] not in [r[0] for r in routeold]:
    print(route)

cfg.rollback(1)
cfg.commit()
