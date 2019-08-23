from netmiko import ConnectHandler
from datetime import datetime
from pprint import pprint
import yaml
import json
from ciscoconfparse import CiscoConfParse

f = open('../../../.netmiko.yml', 'r')
yaml_data = yaml.load(f)
f.close()

conn = ConnectHandler(**yaml_data['cisco4'])
run = conn.send_command('show run')
conn.disconnect()

conf = CiscoConfParse(run.splitlines())
intfs = conf.find_objects_w_child(parentspec=r'^interface', childspec=r'^\s+ip address')
for intf in intfs:
  print(intf.text)
  print(intf.re_search_children('ip address')[0].text)
