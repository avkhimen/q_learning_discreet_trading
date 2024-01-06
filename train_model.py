import numpy as np
from collections import deque
import random

def main():
    de = deque()
    de.append([1])
    de.append([2])
    de.append([3])
    print(de)
    print(random.sample(de, 2))

if __name__ == '__main__':
    main()