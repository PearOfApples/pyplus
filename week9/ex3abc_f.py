import ex3abc_dev
from napalm import get_network_driver

def napalm(dev):
  return get_network_driver(dev.pop('platform'))(**dev)

def conn():
  l = []
  for dev in [ex3abc_dev.arista1, ex3abc_dev.cisco3]:
    l.append(napalm(dev))
  return l

def g_cfg(conn):
  cfg = conn.get_config()
  with open(conn.get_facts()['hostname'], 'w') as f:
    f.write(cfg['running'])
  return

if __name__ == '__main__':
  print(conn())
