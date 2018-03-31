import numpy as np
import matplotlib.pyplot as plt

def create_bandits(n):
    sigma = 1.0

    means = np.random.normal(0,sigma,size=(n,1))

    return means, [np.random.normal(mu,sigma) for mu in means]

def initialise_q(optimism,n):
    return [optimism]*n

def softmax_egreedy_policy(q,epsilon):
    if np.random.rand() < epsilon:
        return np.random.choice(np.arange(len(q)),p=np.exp(q - np.max(q)) / np.sum(np.exp(q - np.max(q))))
    else:
        return np.argmax(q)

def egreedy_policy(q,epsilon):
    if np.random.rand() < epsilon:
        return np.random.randint(0,len(q))
    else:
        return np.argmax(q)

def graph(epsilon,optimism,plays,repetitions):
    average_rewards = [0] * plays
    optimal_actions = [0] * plays

    for i in range(repetitions):
        means, bandits = create_bandits(n)

        q = initialise_q(optimism,len(bandits))
        q, average_reward, optimal_action = play(means,bandits,q,epsilon,plays)

        average_rewards = np.add(average_rewards,average_reward)
        optimal_actions = np.add(optimal_actions,optimal_action)

    print(means,q)

    average_rewards = np.true_divide(average_rewards,repetitions)
    optimal_actions = np.true_divide(optimal_actions,repetitions)

    plt.plot(range(plays),average_rewards)
    plt.xlabel('Plays')
    plt.ylabel('Average Reward')
    plt.figure()
    plt.plot(range(plays),optimal_actions)
    plt.xlabel('Plays')
    plt.ylabel('% Optimal Action')
    plt.show()

def play(means,bandits,q,epsilon,plays):
    k = [0]*len(q)

    rewards = [0] * plays
    optimal_actions = [0] * plays

    optimal_action = np.argmax(means)

    previous_reward = 0
    for i in range(plays):
        choice = egreedy_policy(q,epsilon)
        k[choice] += 1
        reward = bandits[choice][0]
        rewards[i] = reward

        if choice == optimal_action:
            optimal_actions[i] = 1

        q[choice] = q[choice] + (1/k[choice])*(reward-q[choice])

    return q, rewards, optimal_actions

# Non-stationary problem.

if __name__ == "__main__":
    n = 10
    optimism = 0
    epsilon = 0.1
    plays = 1000
    repetitions = 2000

    graph(epsilon,optimism,plays,repetitions)
