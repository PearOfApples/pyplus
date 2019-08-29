from pprint import pprint
import ex4abcd_f

conn = ex4abcd_f.nxconn()
conn.open()
ex4abcd_f.cpoint(conn)
conn.load_replace_candidate('ex4abcd_nxos1.cfg')
print(conn.compare_config())
conn.discard_config()
print(conn.compare_config())
conn.close()
