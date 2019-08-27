import jinja2
from jinja2.environment import Environment

var = {
  "ntp1" : "130.126.24.24",
  "ntp2" : "152.2.21.1",
  "timezone" : "PST",
  "timezone_offset" : "-8",
  "timezone_dst" : "PDT"
}

env = Environment()
env.loader = jinja2.FileSystemLoader('.')
tmpl = env.get_template('ex5.j2')
print(tmpl.render(**var))

