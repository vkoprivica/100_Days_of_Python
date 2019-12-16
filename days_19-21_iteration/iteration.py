import itertools
from itertools import product
import sys
import time



# symbols = itertools.cycle("-\|/")

# while True:
#     sys.stdout.write(f"\r {next(symbols)}")
#     sys.stdout.flush()
#     time.sleep(1)

for letter in product("Vule", repeat=2):
    print(letter)