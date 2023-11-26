import pandas as pd
import numpy as np
import random

class StockPricesEnv:
    def __init__(self, ts, interval, lookup):
        self.ts = ts
        self.interval = interval
        self.lookup = lookup
    
    def reset(self):
        ts_len = len(self.ts)
        random_index = random.randint(self.lookup, ts_len - self.interval)
        self.start_index = random_index - self.lookup
        self.end_index = random_index + self.interval
        state = (self.ts[self.start_index : self.end_index], 0) # 0 own cash; 1 own asset
        return state

    def step(self, action, state):
        self.start_index += 1
        self.end_index += 1

        asset_state = state[1]
        new_asset_state = self.get_new_asset_state(asset_state, action)
        new_state = (self.ts[self.start_index : self.end_index], new_asset_state)
        reward = self.calculate_reward()
        done = False
        info = {}
        return new_state, reward, done, info

    def calculate_reward(self):
        return 0

    def get_new_asset_state(self, asset_state, action):
        # action = 0 buy asset
        # action = 1 sell asset
        # action = 2 do nothing

        # 0 = own cash
        # 1 = own asset
        if action == 0 and asset_state == 0:
            new_asset_state = 1
        if action == 0 and asset_state == 1:
            new_asset_state = 1
        if action == 1 and asset_state == 0:
            new_asset_state = 0
        if action == 1 and asset_state == 1:
            new_asset_state = 0
        if action == 2 and asset_state == 0:
            new_asset_state = 0
         if action == 2 and asset_state == 1:
            new_asset_state = 1
        
        return new_asset_state