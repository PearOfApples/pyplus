from lxml import etree

with open('ex1e.xml') as f:
  xml = etree.parse(f)

print(xml.getroot()[0][0].text)
