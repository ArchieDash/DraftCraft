from itertools import count
from itertools import islice
import time


for i in islice(count(10, -1), 10):
    print(i)
    time.sleep(1)
    i += 1
print('BANG!')
