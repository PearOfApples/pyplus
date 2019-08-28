from lxml import etree

with open('ex5a.xml', 'rb') as f:
  xml = etree.fromstring(f.read())

print(xml.find('.//proc_board_id', namespaces=xml.nsmap).text)
