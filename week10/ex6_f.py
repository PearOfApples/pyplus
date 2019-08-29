from netmiko import ConnectHandler

def ssh(dev, cmd):
  conn = ConnectHandler(**dev)
  out = conn.send_command(cmd)
  conn.disconnect()
  return out

