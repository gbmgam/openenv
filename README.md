# SmartEnergyEnv

## Overview
SmartEnergyEnv simulates a household energy management system. Agents learn to optimize electricity usage by controlling devices, adjusting thermostat settings, and scheduling appliances.

## Action Space
- Turn devices ON/OFF
- Adjust thermostat (set temperature)
- Schedule appliances (washing machine, dishwasher)

## Observation Space
- Time of day
- Electricity price
- Temperature
- Device states
- Energy cost

## Tasks
1. **Task 1 (Easy):** Turn off unused devices at night  
2. **Task 2 (Medium):** Optimize thermostat usage  
3. **Task 3 (Hard):** Schedule appliances during low-tariff hours  

## Reward Function
- Normalized between 0.0–1.0
- Partial progress signals included

## Setup
```bash
pip install -r requirements.txt
python inference.py
