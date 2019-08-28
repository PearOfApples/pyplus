import nxapi_plumbing
from lxml import etree

nxos1 = nxapi_plumbing.Device(
  api_format="xml",
  host="nxos1.lasthop.io",
  username="pyclass",
  password="88newclass",
  transport="https",
  port=8443,
  verify=False,
)

intf = nxos1.show('show interface ethernet1/1')
print('{} is {} with mtu {}'.format(intf.find('.//interface').text, intf.find('.//state').text, intf.find('.//eth_mtu').text))

