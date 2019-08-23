from netmiko import ConnectHandler
from datetime import datetime
from pprint import pprint
import yaml
import json
from ciscoconfparse import CiscoConfParse

f = open('ex7.cfg', 'r')
conf = CiscoConfParse(f)
f.close()

info = []
peers = conf.find_objects_w_parents(parentspec=r'^router', childspec='^\s+neighbor')
for peer in peers:
  for asnum in peer.children:
    if 'remote-as' in asnum.text:
      info.append((peer.text.split()[1], asnum.text.split()[1]))
print(info)
