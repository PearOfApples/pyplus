from lxml import etree

with open('ex4b.xml') as f:
  xml = etree.parse(f)

print(xml.find('.//zones-security-zonename').text)
