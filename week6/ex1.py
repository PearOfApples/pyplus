import pyeapi

arista3 = {
  'host' :  'arista3.lasthop.io',
  'username' : 'pyclass',
  'password' : '88newclass',
  'device_type' : 'arista_eos'
}

conn  = pyeapi.client.Node(pyeapi.client.connect(**arista3))

table = {}
arp = conn.enable('show ip arp')
for item in arp[0]['result']['ipV4Neighbors']:
  table[item['address']] = item['hwAddress']

print(table)
