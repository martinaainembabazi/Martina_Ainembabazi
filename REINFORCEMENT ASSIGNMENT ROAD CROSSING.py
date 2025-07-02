import numpy as np
import random

# Road has 5 positions: [0, 1, 2, 3, 4]
goal = 4
Q = np.zeros((5, 3))  # states x actions

# Parameters
episodes = 200
alpha = 0.1
gamma = 0.9
epsilon = 0.3

# Actions: 0=Left, 1=Right, 2=Wait
for ep in range(episodes):
    pos = 0  # start
    while pos != goal:
        if random.random() < epsilon:
            a = random.choice([0, 1, 2])  # explore
        else:
            a = np.argmax(Q[pos])         # exploit

        # Take action
        if a == 0:
            next_pos = max(pos - 1, 0)
        elif a == 1:
            next_pos = min(pos + 1, goal)
        else:
            next_pos = pos

        # Reward
        r = 10 if next_pos == goal else -0.1

        # Q update
        Q[pos, a] += alpha * (r + gamma * np.max(Q[next_pos]) - Q[pos, a])
        pos = next_pos

# Test the learned policy
pos = 0
path = [pos]
while pos != goal:
    a = np.argmax(Q[pos])
    if a == 0:
        pos = max(pos - 1, 0)
    elif a == 1:
        pos = min(pos + 1, goal)
    else:
        pos = pos
    path.append(pos)

print("Best path to cross the road:", path)
print("Q-table:\n", Q)
