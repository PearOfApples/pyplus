import ex2_dev
import ex2_f
import threading
import time
import queue

ts = []

s = time.time()

queue = queue.Queue()

for dev in ex2_dev.devs:
  t = (threading.Thread(target=ex2_f.ssh, args=(dev, 'show version', queue)))
  t.start()
  ts.append(t)
for t in ts:
  t.join()

while queue.qsize() != 0:
  print(queue.get())
e = time.time()

print(e-s)
