import os
import openai
from env.energy_env import EnergyEnv

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

openai.api_base = API_BASE_URL
openai.api_key = HF_TOKEN

env = EnergyEnv()
obs = env.reset(task_id="task1")

print("[START]")

for step in range(10):
    # Simple heuristic baseline
    if obs["time"] >= 22:
        action = {"device": "lights", "operation": "off"}
    else:
        action = {"device": "ac", "operation": "set", "value": 22}

    obs, reward, done, info = env.step(action)
    print(f"[STEP] {step} obs={obs} reward={reward:.2f}")

    if done:
        break

print("[END]")
