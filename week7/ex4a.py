from lxml import etree

with open('ex4a.xml') as f:
  xml = etree.parse(f)

print(xml.find('zones-security').tag)
for child in xml.find('zones-security').getchildren():
  print(child.tag)
