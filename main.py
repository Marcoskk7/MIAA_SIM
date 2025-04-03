from robot.controller import Controller
from robot.motion_planning import MotionPlanning
from config.robot_varant import panda_config,sawyer_config,gen3_config
from config.object_varant import table_config,banana_config,cup_config,bottle_config,drawer_config
from config.camera_varant import camera_config
from create import create_table, create_cylinder,create_box
import sapien

import numpy as np
from mplib import Pose
if __name__ == "__main__":
    controller = Controller()
    robot = controller.add_robot(panda_config)

    table = create_table(
        scene = controller.scene,
        pose = sapien.Pose(p=[1.0, 0.0, 1.0],q=[1, 0, 0, 0]),
        size = 5.0,
        height=1.0,
    )

    box_1 = create_box(
        scene = controller.scene,
        pose = sapien.Pose(p=[0.4, 0.3 ,1],q=[1, 0, 0, 0]),
        half_size = [0.03, 0.03, 0.03],
        color = [0.1, 0.2, 0.5],
        name = "box_1",
    )

    box_2 = create_box(
        scene = controller.scene,
        pose = sapien.Pose(p=[0.2, -0.3 ,1],q=[1, 0, 0, 0]),
        half_size = [0.03, 0.03, 0.03],
        color = [0.6, 0.1, 0.4],
        name = "box_2",
    )

    box_3 = create_box(
        scene = controller.scene,
        pose = sapien.Pose(p=[0.6, 0.1 ,1],q=[1, 0, 0, 0]),
        half_size = [0.03, 0.03, 0.03],
        color = [0.4, 0.7, 0.1],
        name = "box_3",
    )
     # entity = controller.add_entity(bottle_config, False)
    mp = MotionPlanning(panda_config,controller)
    poses = [
        Pose([0.4, 0.3, 0.12], [0, 1, 0, 0]),
        Pose([0.2, -0.3, 0.08], [0, 1, 0, 0]),
        Pose([0.6, 0.1, 0.14], [0, 1, 0, 0]),
    ]

    for i in range(3):
        pose = poses[i]
        new_p = pose.p.copy()  # 创建副本
        new_p[2] += 0.2
        new_pose = Pose(new_p, pose.q)
        mp.move_to_pose(new_pose)
        mp.open_gripper()
        new_p[2] -= 0.18
        new_pose = Pose(new_p, pose.q)
        mp.move_to_pose(new_pose)
        mp.close_gripper()
        new_p[2] += 0.12
        new_pose = Pose(new_p, pose.q)
        mp.move_to_pose(new_pose)
        new_p[0] += 0.1
        new_pose = Pose(new_p, pose.q)
        mp.move_to_pose(new_pose)
        new_p[2] -= 0.12
        new_pose = Pose(new_p, pose.q)
        mp.move_to_pose(new_pose)
        mp.open_gripper()
        new_p[2] += 0.12
        new_pose = Pose(new_p, pose.q)
        mp.move_to_pose(new_pose)
    controller.out.release()
    # controller.visualize(robot)
