import xmltodict

def fopen(f):
  with open(f, 'rb') as ff:
    return xmltodict.parse(ff)
def fopen_list(f):
  with open(f, 'rb') as ff:
    return xmltodict.parse(ff,force_list={'zones-security'})

print(type(fopen('ex3b_2.xml')['zones-information']['zones-security']))
print(type(fopen_list('ex3b_2.xml')['zones-information']['zones-security']))
