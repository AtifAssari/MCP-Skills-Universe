---
rating: ⭐⭐⭐
title: stable-baselines3
url: https://skills.sh/davila7/claude-code-templates/stable-baselines3
---

# stable-baselines3

skills/davila7/claude-code-templates/stable-baselines3
stable-baselines3
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill stable-baselines3
SKILL.md
Stable Baselines3
Overview

Stable Baselines3 (SB3) is a PyTorch-based library providing reliable implementations of reinforcement learning algorithms. This skill provides comprehensive guidance for training RL agents, creating custom environments, implementing callbacks, and optimizing training workflows using SB3's unified API.

Core Capabilities
1. Training RL Agents

Basic Training Pattern:

import gymnasium as gym
from stable_baselines3 import PPO

# Create environment
env = gym.make("CartPole-v1")

# Initialize agent
model = PPO("MlpPolicy", env, verbose=1)

# Train the agent
model.learn(total_timesteps=10000)

# Save the model
model.save("ppo_cartpole")

# Load the model (without prior instantiation)
model = PPO.load("ppo_cartpole", env=env)


Important Notes:

total_timesteps is a lower bound; actual training may exceed this due to batch collection
Use model.load() as a static method, not on an existing instance
The replay buffer is NOT saved with the model to save space

Algorithm Selection: Use references/algorithms.md for detailed algorithm characteristics and selection guidance. Quick reference:

PPO/A2C: General-purpose, supports all action space types, good for multiprocessing
SAC/TD3: Continuous control, off-policy, sample-efficient
DQN: Discrete actions, off-policy
HER: Goal-conditioned tasks

See scripts/train_rl_agent.py for a complete training template with best practices.

2. Custom Environments

Requirements: Custom environments must inherit from gymnasium.Env and implement:

__init__(): Define action_space and observation_space
reset(seed, options): Return initial observation and info dict
step(action): Return observation, reward, terminated, truncated, info
render(): Visualization (optional)
close(): Cleanup resources

Key Constraints:

Image observations must be np.uint8 in range [0, 255]
Use channel-first format when possible (channels, height, width)
SB3 normalizes images automatically by dividing by 255
Set normalize_images=False in policy_kwargs if pre-normalized
SB3 does NOT support Discrete or MultiDiscrete spaces with start!=0

Validation:

from stable_baselines3.common.env_checker import check_env

check_env(env, warn=True)


See scripts/custom_env_template.py for a complete custom environment template and references/custom_environments.md for comprehensive guidance.

3. Vectorized Environments

Purpose: Vectorized environments run multiple environment instances in parallel, accelerating training and enabling certain wrappers (frame-stacking, normalization).

Types:

DummyVecEnv: Sequential execution on current process (for lightweight environments)
SubprocVecEnv: Parallel execution across processes (for compute-heavy environments)

Quick Setup:

from stable_baselines3.common.env_util import make_vec_env

# Create 4 parallel environments
env = make_vec_env("CartPole-v1", n_envs=4, vec_env_cls=SubprocVecEnv)

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=25000)


Off-Policy Optimization: When using multiple environments with off-policy algorithms (SAC, TD3, DQN), set gradient_steps=-1 to perform one gradient update per environment step, balancing wall-clock time and sample efficiency.

API Differences:

reset() returns only observations (info available in vec_env.reset_infos)
step() returns 4-tuple: (obs, rewards, dones, infos) not 5-tuple
Environments auto-reset after episodes
Terminal observations available via infos[env_idx]["terminal_observation"]

See references/vectorized_envs.md for detailed information on wrappers and advanced usage.

4. Callbacks for Monitoring and Control

Purpose: Callbacks enable monitoring metrics, saving checkpoints, implementing early stopping, and custom training logic without modifying core algorithms.

Common Callbacks:

EvalCallback: Evaluate periodically and save best model
CheckpointCallback: Save model checkpoints at intervals
StopTrainingOnRewardThreshold: Stop when target reward reached
ProgressBarCallback: Display training progress with timing

Custom Callback Structure:

from stable_baselines3.common.callbacks import BaseCallback

class CustomCallback(BaseCallback):
    def _on_training_start(self):
        # Called before first rollout
        pass

    def _on_step(self):
        # Called after each environment step
        # Return False to stop training
        return True

    def _on_rollout_end(self):
        # Called at end of rollout
        pass


Available Attributes:

self.model: The RL algorithm instance
self.num_timesteps: Total environment steps
self.training_env: The training environment

Chaining Callbacks:

from stable_baselines3.common.callbacks import CallbackList

callback = CallbackList([eval_callback, checkpoint_callback, custom_callback])
model.learn(total_timesteps=10000, callback=callback)


See references/callbacks.md for comprehensive callback documentation.

5. Model Persistence and Inspection

Saving and Loading:

# Save model
model.save("model_name")

# Save normalization statistics (if using VecNormalize)
vec_env.save("vec_normalize.pkl")

# Load model
model = PPO.load("model_name", env=env)

# Load normalization statistics
vec_env = VecNormalize.load("vec_normalize.pkl", vec_env)


Parameter Access:

# Get parameters
params = model.get_parameters()

# Set parameters
model.set_parameters(params)

# Access PyTorch state dict
state_dict = model.policy.state_dict()

6. Evaluation and Recording

Evaluation:

from stable_baselines3.common.evaluation import evaluate_policy

mean_reward, std_reward = evaluate_policy(
    model,
    env,
    n_eval_episodes=10,
    deterministic=True
)


Video Recording:

from stable_baselines3.common.vec_env import VecVideoRecorder

# Wrap environment with video recorder
env = VecVideoRecorder(
    env,
    "videos/",
    record_video_trigger=lambda x: x % 2000 == 0,
    video_length=200
)


See scripts/evaluate_agent.py for a complete evaluation and recording template.

7. Advanced Features

Learning Rate Schedules:

def linear_schedule(initial_value):
    def func(progress_remaining):
        # progress_remaining goes from 1 to 0
        return progress_remaining * initial_value
    return func

model = PPO("MlpPolicy", env, learning_rate=linear_schedule(0.001))


Multi-Input Policies (Dict Observations):

model = PPO("MultiInputPolicy", env, verbose=1)


Use when observations are dictionaries (e.g., combining images with sensor data).

Hindsight Experience Replay:

from stable_baselines3 import SAC, HerReplayBuffer

model = SAC(
    "MultiInputPolicy",
    env,
    replay_buffer_class=HerReplayBuffer,
    replay_buffer_kwargs=dict(
        n_sampled_goal=4,
        goal_selection_strategy="future",
    ),
)


TensorBoard Integration:

model = PPO("MlpPolicy", env, tensorboard_log="./tensorboard/")
model.learn(total_timesteps=10000)

Workflow Guidance

Starting a New RL Project:

Define the problem: Identify observation space, action space, and reward structure
Choose algorithm: Use references/algorithms.md for selection guidance
Create/adapt environment: Use scripts/custom_env_template.py if needed
Validate environment: Always run check_env() before training
Set up training: Use scripts/train_rl_agent.py as starting template
Add monitoring: Implement callbacks for evaluation and checkpointing
Optimize performance: Consider vectorized environments for speed
Evaluate and iterate: Use scripts/evaluate_agent.py for assessment

Common Issues:

Memory errors: Reduce buffer_size for off-policy algorithms or use fewer parallel environments
Slow training: Consider SubprocVecEnv for parallel environments
Unstable training: Try different algorithms, tune hyperparameters, or check reward scaling
Import errors: Ensure stable_baselines3 is installed: uv pip install stable-baselines3[extra]
Resources
scripts/
train_rl_agent.py: Complete training script template with best practices
evaluate_agent.py: Agent evaluation and video recording template
custom_env_template.py: Custom Gym environment template
references/
algorithms.md: Detailed algorithm comparison and selection guide
custom_environments.md: Comprehensive custom environment creation guide
callbacks.md: Complete callback system reference
vectorized_envs.md: Vectorized environment usage and wrappers
Installation
# Basic installation
uv pip install stable-baselines3

# With extra dependencies (Tensorboard, etc.)
uv pip install stable-baselines3[extra]

Weekly Installs
279
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass