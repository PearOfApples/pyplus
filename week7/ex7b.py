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

out = nxos1.show_list(['show system uptime', 'show system resources'])
print(etree.tostring(out[0]).decode())
print(etree.tostring(out[1]).decode())
