import pyeapi
import yaml
import ex2b_fun

conn = pyeapi.client.Node(pyeapi.client.connect(**ex2b_fun.load_dev('ex2b.yml', 'arista4')))

print(ex2b_fun.output(conn))
