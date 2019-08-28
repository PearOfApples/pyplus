import pyeapi
import yaml
import jinja2

env = jinja2.environment.Environment()
env.loader = jinja2.FileSystemLoader('.')
tmpl = env.get_template('ex4.j2')

with open('ex4.yml') as f:
  devs = yaml.safe_load(f)
 
for _, dev in devs.items():
  conn  = pyeapi.client.Node(pyeapi.client.connect(**dev))
  print(conn.config(tmpl.render(**dev['data']).splitlines()))
  print(conn.enable('show ip interface brief'))
   
