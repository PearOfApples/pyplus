from lxml import etree

with open('ex1f.xml') as f:
  xml = etree.parse(f)

for child in xml.getroot()[0].getchildren():
  print(child.tag)
