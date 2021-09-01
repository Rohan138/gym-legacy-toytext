import gym

import gym_toytext


def test_envs():
    gym.make("KellyCoinflip-v0")
    gym.make("KellyCoinflipGeneralized-v0")
    gym.make("NChain-v0")
    gym.make("Roulette-v0")
    gym.make("GuessingGame-v0")
    gym.make("HotterColder-v0")
