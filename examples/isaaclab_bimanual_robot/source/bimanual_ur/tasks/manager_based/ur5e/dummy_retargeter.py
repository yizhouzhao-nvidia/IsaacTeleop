# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import torch

import isaaclab.sim as sim_utils
import isaaclab.utils.math as PoseUtils
from isaaclab.devices.device_base import DeviceBase
from isaaclab.devices.retargeter_base import RetargeterBase, RetargeterCfg
from isaaclab.markers import VisualizationMarkers, VisualizationMarkersCfg


class DummyRetargeter(RetargeterBase):
    """Simple retargeter that maps motion controller inputs to G1 hand joints.

    Mapping:
    - A button (digital 0/1) → Thumb joints
    - Trigger (analog 0-1) → Index finger joints
    - Squeeze (analog 0-1) → Middle finger joints
    """

    def __init__(self, cfg: DummyRetargeterCfg):
        """Initialize the retargeter."""
        super().__init__(cfg)
        self._sim_device = cfg.sim_device
        self._hand_joint_names = cfg.hand_joint_names
        self._enable_visualization = cfg.enable_visualization

        if cfg.hand_joint_names is None:
            raise ValueError("hand_joint_names must be provided")

        # Initialize visualization if enabled
        if self._enable_visualization:
            marker_cfg = VisualizationMarkersCfg(
                prim_path="/Visuals/g1_controller_markers",
                markers={
                    "joint": sim_utils.SphereCfg(
                        radius=0.01,
                        visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(0.0, 1.0, 0.0)),
                    ),
                },
            )
            self._markers = VisualizationMarkers(marker_cfg)

    def retarget(self, data: dict) -> torch.Tensor:
        """Convert controller inputs to robot commands.

        Args:
            data: Dictionary with MotionControllerTrackingTarget.LEFT/RIGHT keys
                 Each value is a 2D array: [pose(7), inputs(7)]

        Returns:
            Tensor: [left_wrist(7), right_wrist(7), hand_joints(14)]
            hand_joints order:
                [
                    left_proximal(3), right_proximal(3), left_distal(2), left_thumb_middle(1),
                    right_distal(2), right_thumb_middle(1), left_thumb_tip(1), right_thumb_tip(1)
                ]
        """
        pass

    def get_requirements(self) -> list[RetargeterBase.Requirement]:
        return [RetargeterBase.Requirement.MOTION_CONTROLLER]


@dataclass
class DummyRetargeterCfg(RetargeterCfg):
    """Configuration for the Dummy retargeter."""

    enable_visualization: bool = False
    hand_joint_names: list[str] | None = None  # List of robot hand joint names
    retargeter_type: type[RetargeterBase] = DummyRetargeter
