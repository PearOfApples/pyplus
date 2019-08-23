from netmiko import ConnectHandler
from datetime import datetime
import re
from pprint import pprint
arp = '''
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''.strip()

arplist = []
for line in arp.splitlines()[1:]:
  _, ip, _, mac, _ , intf = line.split() 
  arplist.append({'mac_addr' : mac, 'ip_addr' : ip, 'interface' : intf})
pprint(arplist)
