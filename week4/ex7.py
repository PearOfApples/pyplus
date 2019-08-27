import textfsm
from pprint import pprint

with open("ex7.txt") as f:
  text = f.read()

with open("ex7.template") as f:
  parser = textfsm.TextFSM(f)
  parsed_data = parser.ParseText(text)

parsed_list = []
for i in range(len(parsed_data)):
  d = {}
  for j in range(len(parser.header)):
    d[parser.header[j]] = parsed_data[i][j]
  parsed_list.append(d)

pprint(parsed_list)
