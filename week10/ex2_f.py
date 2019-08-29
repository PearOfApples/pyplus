import time
from netmiko import ConnectHandler

def ssh(dev, cmd, queue):
  st = time.time()
  conn = ConnectHandler(**dev)
  conn.send_command(cmd)
  conn.disconnect()
  end = time.time()
  queue.put(end-st)
  return

