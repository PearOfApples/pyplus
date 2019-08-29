import ex3ab_dev
import ex3ab_f
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import time

ts = []

s = time.time()

p = ThreadPoolExecutor(16)
for dev in ex3ab_dev.devs:
  ts.append(p.submit(ex3ab_f.ssh, dev, 'show version'))
wait(ts)

for t in ts:
  print(t.result())
e = time.time()
print(e-s)

s = time.time()
ts = []
for dev in ex3ab_dev.devs:
  ts.append(p.submit(ex3ab_f.ssh, dev, 'show version'))

for t in as_completed(ts):
  print(t.result())
e = time.time()
print(e-s)
