import yaml

def load_dev(yml, dev):
  with open(yml) as f:
    return  yaml.safe_load(f)[dev]

def output(conn):
  table = {}
  arp = conn.enable('show ip arp')
  for item in arp[0]['result']['ipV4Neighbors']:
    table[item['address']] = item['hwAddress']
  return table
