import xmltodict

with open('ex2a.xml', 'rb') as f:
  xml = xmltodict.parse(f)

print(xml)
print(type(xml))
