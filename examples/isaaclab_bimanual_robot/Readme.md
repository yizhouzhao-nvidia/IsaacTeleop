<!--
SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Bimanual UR Example using IsaacLab

This directory contains minimal usage examples for teleoperating two UR arms in IsaacLab.

## Prerequisite

```
pip install lerobot
```

## Examples

- **record.py**
  Record a dataset in the LeRobot format from live human data. Currently it only
  captures head and hands position for demonstrations purpose.

  Note: the record.py script always create a new dataset. You must remove
  existing one before running it again:

  ```bash
  rm -rf local_datasets
  ```

- **visualize.py**
  A basic rerun visualizer to plot out the dataset.

- **analyze.py**
  A quick sample to parse and analyze the LeRobot dataset.
