import sys
from heapq import heappush, heappop


N = int(sys.stdin.readline())
# num_list = []
heap = []
# cnt = 0

for i in range(N):
  num = int(sys.stdin.readline())
  if num == 0:
    # cnt += 1
    if heap:
      print(heappop(heap))
    else:
      print(0)
  else:
    heappush(heap, num)