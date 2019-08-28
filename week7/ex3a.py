import xmltodict

def fopen(f):
  with open(f, 'rb') as ff:
    return xmltodict.parse(ff)

print(fopen('ex3a_1.xml'))
print(fopen('ex3a_2.xml'))
