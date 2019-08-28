from lxml import etree

with open('ex1d.xml') as f:
  xml = etree.parse(f)

print(xml.getroot()[0].tag)
print(xml.getroot().getchildren()[0].tag)
