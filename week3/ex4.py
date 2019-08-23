from netmiko import ConnectHandler
from datetime import datetime
from pprint import pprint
import yaml
import json

json_data = json.load(open('ex4.json', 'r'))
pprint(json_data)

arp = {}
for entry in json_data['ipV4Neighbors']:
  arp[entry['address']] = entry['hwAddress']
print(arp)
