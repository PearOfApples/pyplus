from lxml import etree

with open('ex1b.xml') as f:
  xml = etree.parse(f)

print(etree.tostring(xml).decode())
