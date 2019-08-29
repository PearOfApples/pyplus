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

try:
  cfg.lock()
except:
  print('already locked')
