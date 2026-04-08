import random
from typing import Dict, Tuple

class EnergyEnv:
    def __init__(self):
        self.devices = {
            "lights": 1,
            "ac": 1,
            "washing_machine": 0,
            "dishwasher": 0
        }
        self.time = 20
        self.price = 0.20
        self.temperature = 22
        self.comfort_range = (20, 24)
        self.energy_cost = 0.0
        self.task_id = None

    def reset(self, task_id: str = "task1") -> Dict:
        self.devices = {"lights": 1, "ac": 1, "washing_machine": 0, "dishwasher": 0}
        self.time = 20
        self.price = 0.20
        self.temperature = 22
        self.energy_cost = 0.0
        self.task_id = task_id
        return self.state()

    def state(self) -> Dict:
        return {
            "time": self.time,
            "price": self.price,
            "temperature": self.temperature,
            "devices": self.devices.copy(),
            "energy_cost": self.energy_cost
        }

    def step(self, action: Dict) -> Tuple[Dict, float, bool, Dict]:
        device = action.get("device")
        op = action.get("operation")

        if device in self.devices:
            if op == "on":
                self.devices[device] = 1
            elif op == "off":
                self.devices[device] = 0

        if device == "ac" and op == "set":
            self.temperature = action.get("value", self.temperature)

        self.time += 1
        if self.time > 24:
            self.time = 0

        self.price = 0.30 if 18 <= self.time <= 22 else 0.10
        active_devices = sum(self.devices.values())
        self.energy_cost += active_devices * self.price * 0.1

        reward = self._compute_reward()
        done = (self.time == 0)

        return self.state(), reward, done, {"task": self.task_id}

    def _compute_reward(self) -> float:
        if self.task_id == "task1":
            if self.time >= 22:
                off_count = sum(1 for d in self.devices.values() if d == 0)
                return off_count / len(self.devices)
            return 0.5

        elif self.task_id == "task2":
            comfort = 1.0 if self.comfort_range[0] <= self.temperature <= self.comfort_range[1] else 0.0
            cost_factor = max(0.0, 1.0 - self.energy_cost / 5.0)
            return (comfort + cost_factor) / 2.0

        elif self.task_id == "task3":
            low_tariff = (self.price <= 0.15)
            scheduled = (self.devices["washing_machine"] == 1 or self.devices["dishwasher"] == 1)
            if scheduled and low_tariff:
                return 1.0
            elif scheduled:
                return 0.5
            else:
                return 0.0

        return 0.0
