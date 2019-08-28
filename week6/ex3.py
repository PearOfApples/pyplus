import pyeapi
import yaml
import ex3_fun
from pprint import pprint

conn = pyeapi.client.Node(pyeapi.client.connect(**ex3_fun.load_dev('ex3.yml', 'arista4')))

pprint(ex3_fun.output(conn))

#print(conn.enable('show ip route'))
