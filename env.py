import pandas as pd
import numpy as np
import random

class StockPricesEnv():
    def __init__(self, ts, interval, lookup):
        self.ts = ts
        self.interval = interval
        self.lookup = lookup
    
    def reset(self):
        ts_len = len(ts)
        random_index = random.randint(lookup, ts_len-interval)
        state = ts[random_index - lookup : random_index + interval]
        return state

    def step(self, action):
        new_state = None
        reward = 0
        done = False
        info = {}
        return new_state, reward, done, info