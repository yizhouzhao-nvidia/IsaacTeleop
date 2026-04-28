<!--
SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Bimanual UR Example using IsaacLab

This directory contains minimal usage examples for teleoperating two UR arms in IsaacLab.

## Prerequisites



### 1.Isaac Teleop

Follow [Install Isaac Teleop](https://isaac-sim.github.io/IsaacLab/main/source/how-to/cloudxr_teleoperation.html#cloudxr-teleoperation) to install Isaac Teleop.

After installation, start the ClourXR server:

```bash
python -m isaacteleop.cloudxr
```

### 2.Isaac Lab

Follow [Install Isaac Lab](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html) to install Isaac Lab with virtual environment `env_isaaclab`.

After installation, activate the virtual environment:

```bash
source <your_isaaclab_path>/env_isaaclab/bin/activate
```

### 3. Install this package to `env_isaaclab`

```bash
python -m pip install -e .

## If you use uv:
# uv pip install -e .
```

## How to run

1. Source cloudxr env

```bash
source ~/.cloudxr/run/cloudxr.env
```

2. Run the task

To examine the task environment only:

```bash
python scripts/zero_agent.py --task Template-UR10-Play-v0 --num_envs=1
```

Teleoperation with XR controllers:

```bash
python scripts/teleop_se3_agent_bimanual_xr.py \
  --task Template-UR10-Play-v0 \
  --teleop_device motion_controllers \
  --num_envs 1 \
  --xr
```

Key bindings:
- Press any button on the left controller to start teleoperation
- Move the left controller to control the left arm
- Move the right controller to control the right arm
- Press x or y buttons on the left controller to reset


Record data:

```bash
python scripts/record_se3_agent_bimanual_xr.py \
  --task Template-UR10-Play-v0 \
  --teleop_device motion_controllers \
  --num_envs 1 \
  --xr \
  --dataset_file ./datasets/dataset.hdf5
```

Key bindings:
- Press any button on the left controller to start teleoperation
- Move the left controller to control the left arm
- Move the right controller to control the right arm
- Press x or y buttons on the left controller to reset
- Press a or b buttons on the right controller to save the trajectory and reset env

The dataset will be saved to `./datasets/dataset.hdf5`