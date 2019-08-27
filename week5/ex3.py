import jinja2
from jinja2.environment import Environment

vrf = {
  "name" : "blue",
  "rd" : "100:1",
  "ipv4" : True,
  "ipv6": True
}

env = Environment()
env.loader = jinja2.FileSystemLoader('.')
tmpl = env.get_template('ex3.j2')
for var in [vrf]:
  print(tmpl.render(**var))

