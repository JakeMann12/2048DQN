from gym.envs.registration import register

register(
    id='2048-3x3',
    entry_point='dqn2048.envs:Env2048',
)