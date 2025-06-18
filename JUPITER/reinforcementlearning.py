#REINFORCEMENT LEARNING
#Where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward.
#it is a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward.
#it involves an agent, environment, actions, states, and rewards.
import numpy as np
import random

# Define the environment parameters
actions=2# Number of actions the agent can take
position=5


#initiLize the Q-table
Q_table = np.zeros((position, actions))

#define the learning parameters
episodes = 1000  # Number of episodes to train the agent
learning_rate = 0.1  # Learning rate
gama = 0.9  # Discount factor
epislon=0.3#probability of taking a random action (exploration)

#training loop
for episode in range(episodes):
    state =random.randint(0, position - 1)  # Randomly initialize the state

    #action selection
    if random.uniform(0, 1) < epislon:
        action = random.randint(0, actions - 1)  # Explore: choose a random action
    else:
        action = np.argmax(Q_table[state])  # Exploit: choose the best action based on Q-table
        