from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.utils.config import Config

srx2 = {
  'host' : 'srx2.lasthop.io',
  'user' : 'pyclass',
  'password' : '88newclass'
}

dev = Device(**srx2)
dev.open()

cfg = Config(dev)
cfg.lock()

cfg.load('set system host-name newname', format='set', merge='true')
print(cfg.diff())
cfg.rollback(0)
print(cfg.diff())
