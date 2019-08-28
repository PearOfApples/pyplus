from lxml import etree

with open('ex1a.xml') as f:
  xml = etree.parse(f)

print(xml.getroot())
print(type(xml))
