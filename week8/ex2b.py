from pprint import pprint
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
import ex2b_srx2

def cc(dev):
  if dev.connected:
    return True
  return False

def route(dev):
  return RouteTable(dev).get()

def arp(dev):
  return ArpTable(dev).get()

def p(dev, route, arp):
  print('{}@{}:{}'.format(dev.user, dev.hostname, dev.port))
  print(route.items())
  print(arp.items())

if __name__ == '__main__':
  
  dev = ex2b_srx2.dev
  dev.open()

  if cc(dev):
    p(dev, route(dev), arp(dev))

