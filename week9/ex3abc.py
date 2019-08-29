from pprint import pprint
import ex3abc_f

conns = ex3abc_f.conn()
for conn in conns:
  conn.open()
  conn.load_merge_candidate(filename='ex3abc_{}.cfg'.format(conn.get_facts()['hostname']))
  #conn.load_merge_candidate(filename='ex3abc_arista1.cfg')
  print(conn.compare_config())
  conn.commit_config()
  print(conn.compare_config())
  conn.close()
