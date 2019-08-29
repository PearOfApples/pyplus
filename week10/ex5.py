import ex5_dev
import ex5_f
from concurrent.futures import ProcessPoolExecutor, wait, as_completed
import time

ts = []

s = time.time()

with ProcessPoolExecutor(16) as p:
  for dev in ex5_dev.devs:
    ts.append(p.submit(ex5_f.ssh, dev, 'show version'))

for t in as_completed(ts):
  print(t.result())
e = time.time()
print(e-s)
