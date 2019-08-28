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

lo100 = ['interface loopback100', 'description loopback100']
lo101 = ['interface loopback101', 'description loopback101']

nxos1.config_list([x[i] for x in [lo100, lo101] for i in range(len(lo100))])
for i in nxos1.show_list(['show interface loopback100', 'show interface loopback101']):
  print(etree.tostring(i).decode())
