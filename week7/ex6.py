import nxapi_plumbing

nxos1 = nxapi_plumbing.Device(
  api_format="jsonrpc",
  host="nxos1.lasthop.io",
  username="pyclass",
  password="88newclass",
  transport="https",
  port=8443,
  verify=False,
)

intf = nxos1.show('show interface ethernet1/1')['TABLE_interface']['ROW_interface']
print('{} is {} with mtu {}'.format(intf['interface'], intf['state'], intf['eth_mtu']))
