import ex4_dev
import ex4_f
from concurrent.futures import ProcessPoolExecutor, wait, as_completed
import time

ts = []

s = time.time()
p = ProcessPoolExecutor(16)
for dev in ex4_dev.devs:
  ts.append(p.submit(ex4_f.ssh, dev, 'show version'))

for t in as_completed(ts):
  print(t.result())
e = time.time()
print(e-s)
