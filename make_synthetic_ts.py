import numpy as np
from env import StockPricesEnv
import random

def generate_synthetic_ts():
    ts = np.random.random((100,)).tolist()
    return ts

ts = generate_synthetic_ts()

env = StockPricesEnv(ts, 10, 4)

state = env.reset()
for i in range(10):
    action = random.randint(0,2)
    new_state, reward, done, info = env.step(action)
    state = new_state
    print(i, new_state, reward, done, info)