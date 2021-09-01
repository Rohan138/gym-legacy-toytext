from gym.envs.registration import register

from gym_toytext.roulette import RouletteEnv
from gym_toytext.nchain import NChainEnv
from gym_toytext.hotter_colder import HotterColder
from gym_toytext.guessing_game import GuessingGame
from gym_toytext.kellycoinflip import KellyCoinflipEnv, KellyCoinflipGeneralizedEnv

register(
    id="KellyCoinflip-v0",
    entry_point="gym_toytext:KellyCoinflipEnv",
    reward_threshold=246.61,
)

register(
    id="KellyCoinflipGeneralized-v0",
    entry_point="gym_toytext:KellyCoinflipGeneralizedEnv",
)


register(
    id="NChain-v0",
    entry_point="gym_toytext:NChainEnv",
    max_episode_steps=1000,
)

register(
    id="Roulette-v0",
    entry_point="gym_toytext:RouletteEnv",
    max_episode_steps=100,
)


register(
    id="GuessingGame-v0",
    entry_point="gym_toytext:GuessingGame",
    max_episode_steps=200,
)

register(
    id="HotterColder-v0",
    entry_point="gym_toytext:HotterColder",
    max_episode_steps=200,
)
