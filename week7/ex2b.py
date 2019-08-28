import xmltodict

with open('ex2a.xml', 'rb') as f:
  xml = xmltodict.parse(f)

for i in xml['zones-information']['zones-security']:
  print(i['zones-security-zonename'])
