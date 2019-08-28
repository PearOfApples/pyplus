import yaml

def load_dev(yml, dev):
  with open(yml) as f:
    return  yaml.safe_load(f)[dev]

def output(conn):
  table = {}
  routes = conn.enable('show ip route')
  for ip, route in routes[0]['result']['vrfs']['default']['routes'].items():
    table[ip] = {}
    table[ip]['type'] = route['routeType']
    if route['routeType'] == 'static':
      table[ip]['nexthop'] = route['vias'][0]['nexthopAddr']
  return table
