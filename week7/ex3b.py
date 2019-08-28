import xmltodict

def fopen(f):
  with open(f, 'rb') as ff:
    return xmltodict.parse(ff)

print(type(fopen('ex3b_1.xml')['zones-information']))
print(type(fopen('ex3b_1.xml')['zones-information']['zones-security']))
