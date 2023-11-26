import numpy as np
import random
import gymnasium as gym

enviroment = gym.make("Taxi-v3").env

alpha = 0.1
gamma = 0.6
epsilon = 0.1
q_table = np.zeros([enviroment.observation_space.n, enviroment.action_space.n])

num_of_episodes = 50000

for episode in range(0, num_of_episodes):
    # Reset the environment
    state = enviroment.reset()[0]

    # Initialize variables
    reward = 0
    terminated = False
    
    while not terminated:
        # Take learned path or explore new actions based on the epsilon
        if random.uniform(0, 1) < epsilon:
            action = enviroment.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        # Take action
        next_state, reward, terminated, info, _ = enviroment.step(action) 
        
        # Recalculate
        q_value = q_table[state, action]
        max_value = np.max(q_table[next_state])
        new_q_value = (1 - alpha) * q_value + alpha * (reward + gamma * max_value)
        
        # Update Q-table
        q_table[state, action] = new_q_value
        state = next_state
        
    if (episode + 1) % 100 == 0:
        print("Episode: {}".format(episode + 1))

total_epochs = 0
total_penalties = 0
num_of_episodes = 100

for _ in range(num_of_episodes):
    state = enviroment.reset()[0]
    epochs = 0
    penalties = 0
    reward = 0
    
    terminated = False
    
    while not terminated:
        action = np.argmax(q_table[state])
        state, reward, terminated, info, _ = enviroment.step(action)

        if reward == -10:
            penalties += 1

        epochs += 1

    total_penalties += penalties
    total_epochs += epochs

print("**********************************")
print("Results")
print("**********************************")
print("Epochs per episode: {}".format(total_epochs / num_of_episodes))
print("Penalties per episode: {}".format(total_penalties / num_of_episodes))