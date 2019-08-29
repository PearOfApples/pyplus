import ex1ab_dev
import time
from netmiko import ConnectHandler

for dev in ex1ab_dev.devs:
  st = time.time()
  conn = ConnectHandler(**dev)
  conn.send_command('show version')
  conn.disconnect()
  end = time.time()
  print(end-st)

