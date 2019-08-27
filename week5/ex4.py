import jinja2
from jinja2.environment import Environment

vrf1 = {
  "name" : "blue",
  "rd" : "100:1",
  "ipv4" : True,
  "ipv6": True
}
vrf2 = {
  "name" : "red",
  "rd" : "200:2",
  "ipv4" : True,
  "ipv6": True
}
vrf3 = {
  "name" : "green",
  "rd" : "300:3",
  "ipv4" : True,
  "ipv6": True
}
vrf4 = {
  "name" : "orange",
  "rd" : "400:4",
  "ipv4" : True,
  "ipv6": True
}
vrf5 = {
  "name" : "purple",
  "rd" : "500:5",
  "ipv4" : True,
  "ipv6": True
}

d = {"vrfs": [vrf1, vrf2, vrf3, vrf4, vrf5]}
env = Environment()
env.loader = jinja2.FileSystemLoader('.')
tmpl = env.get_template('ex4.j2')
print(tmpl.render(**d))

