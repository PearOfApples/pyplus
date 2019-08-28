from lxml import etree

with open('ex5a.xml', 'rb') as f:
  xml = etree.fromstring(f.read())

print(xml.nsmap)
