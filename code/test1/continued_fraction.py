#!/usr/bin/python3


import time


def c_frac(n):
  s = 1
  for i in range(0, n):
    s = 1.0 + 1.0 / s

  return s


start_time = time.time()
print(c_frac(1000000))
print("--- %f seconds ---" % (time.time() - start_time))
