from lxml import etree

with open('ex1c.xml') as f:
  xml = etree.parse(f)

for e in xml.findall('.//zones-security'):
  print(e.find('./zones-security-zonename').text)
