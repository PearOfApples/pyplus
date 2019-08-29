import ex2a_dev
from napalm import get_network_driver

def napalm(dev):
  return get_network_driver(dev.pop('platform'))(**dev)

def conn():
  l = []
  for dev in [ex2a_dev.arista1, ex2a_dev.cisco3]:
    l.append(napalm(dev))
  return l

if __name__ == '__main__':
  print(conn())
