from pprint import pprint
import ex2bcd_dev
import ex2bcd_f

conns = ex2bcd_f.conn()
for conn in conns:
  conn.open()
  pprint(conn.get_arp_table())
  try:
    pprint(conn.get_ntp_peers())
  except:
    print('no ntp peers for you from {}'.format(conn.platform))
  ex2bcd_f.g_cfg(conn) 
