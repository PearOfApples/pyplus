from napalm import get_network_driver
from pprint import pprint
import ex1bcd_dev

def napalm(dev):
  return get_network_driver(dev.pop('platform'))(**dev)

for dev in [ex1bcd_dev.arista1, ex1bcd_dev.cisco3]:
  conn=napalm(dev)
  conn.open()
  print(conn)
  print(conn.get_facts())
  print(conn.platform)
