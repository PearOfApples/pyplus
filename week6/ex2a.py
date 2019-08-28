import pyeapi
import yaml

with open('ex2.yml') as f:
  arista4 = yaml.safe_load(f)['arista4']

conn  = pyeapi.client.Node(pyeapi.client.connect(**arista4))

table = {}
arp = conn.enable('show ip arp')
for item in arp[0]['result']['ipV4Neighbors']:
  table[item['address']] = item['hwAddress']

print(table)
