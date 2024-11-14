import random

from adder import *

with open('a.txt', 'w') as f1:
    with open('b.txt', 'w') as f2:
        with open('c.txt', 'w') as f3:
            for i in range(100):
                a = ''.join(random.choice('01') for _ in range(32))
                b = ''.join(random.choice('01') for _ in range(32))
                ans, overflow, underflow = add_floating_points(a, b)
                f1.write(a + '\n')
                f2.write(b + '\n')
                f3.write(ans + '\n')
