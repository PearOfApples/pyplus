import ex4abcd_dev
from napalm import get_network_driver

def napalm(dev):
  return get_network_driver(dev.pop('platform'))(**dev)

def conn():
  l = []
  for dev in [ex4abcd_dev.arista1, ex4abcd_dev.cisco3]:
    l.append(napalm(dev))
  return l

def nxconn():
  return napalm(ex4abcd_dev.nxos1)

def g_cfg(conn):
  cfg = conn.get_config()
  with open(conn.get_facts()['hostname'], 'w') as f:
    f.write(cfg['running'])
  return

def cpoint(conn):
  with open('ex4abcd_{}.cp'.format(conn.get_facts()['hostname']), 'w') as f:
    f.write(conn._get_checkpoint_file())
  return

if __name__ == '__main__':
  print(conn())
