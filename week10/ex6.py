import ex6_dev
import ex6_f
from concurrent.futures import ProcessPoolExecutor, wait, as_completed
import time

ts = []

s = time.time()

with ProcessPoolExecutor(16) as p:
  cmds = []
  for dev in ex6_dev.devs:
    if 'juniper' in dev['device_type']:
      cmds.append('show arp')
    else:
      cmds.append('show ip arp')
  ts = p.map(ex6_f.ssh, ex6_dev.devs, cmds)

for t in ts:
  print(t)
e = time.time()
print(e-s)
