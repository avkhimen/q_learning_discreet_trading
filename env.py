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
        self.end_index = random_index
        self.initial_index = self.ts[self.start_index]
        self.state = (np.array(self.ts[self.start_index : self.end_index])/self.initial_index, 0) # 0 own cash; 1 own asset
        self.episode_step = 0
        
        return self.state

    def step(self, action):
        self.start_index += 1
        self.end_index += 1

        asset_state = self.state[1]
        new_asset_state = self.get_new_asset_state(asset_state, action)

        self.new_state = (self.ts[self.start_index : self.end_index], new_asset_state)
        self.episode_step += 1
        reward = self.calculate_reward(action, new_asset_state)
        done = False
        if self.episode_step == self.interval:
            done = True
        info = {}

        self.state = self.new_state

        return self.new_state, reward, done, info

    def calculate_reward(self, action, asset_state, new_asset_state):
        # action = 0 buy asset
        # action = 1 sell asset
        # action = 2 do nothing

        # 0 = own cash
        # 1 = own asset
        reward = 0
        elif action == 0 and new_asset_state == 1 and asset_state == 0:
            reward = self.new_state[0][-1] - self.state[0][-1]

        return reward

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