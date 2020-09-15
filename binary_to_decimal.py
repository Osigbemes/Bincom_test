## Q. 8
## coversion of binary to decimal

import random
from random import sample
from string import digits


binary_num = "".join(sample(bin(int(digits)), 4))
print(int(binary_num, 2))
