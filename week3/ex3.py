from netmiko import ConnectHandler
from datetime import datetime
from pprint import pprint
import yaml
import json

json_data = json.load(open('ex3.json', 'r'))
pprint(json_data)

ip4 = []
ip6 = []

for intf, intf_val in json_data.items():
  for proto, proto_val in intf_val.items():
    for ip, ip_val in proto_val.items():
      val = '{}/{}'.format(ip, ip_val['prefix_length'])
      if proto == 'ipv4':
        ip4.append(val)
      else:
        ip6.append(val)
print(ip4)
print(ip6)
