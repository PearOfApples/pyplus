from lxml import etree

with open('ex1c.xml') as f:
  xml = etree.parse(f)

print(xml.getroot().tag)
print(len(xml.getroot().getchildren()))
