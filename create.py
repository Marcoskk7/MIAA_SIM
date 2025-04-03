import sapien
import cv2
import time
import numpy as np

def create_cylinder(
    scene:sapien.Scene,
    pose:sapien.Pose,
    radius,
    color = None,
    name = "",
) ->sapien.Entity:
    """Create a cylinder"""
    builder:sapien.ActorBuilder = scene.create_actor_builder()
    builder.add_cylinder_collision(radius=radius)
    builder.add_cylinder_visual(radius=radius, material=color)
    cylinder = builder.build(name = name)
    cylinder.set_pose(pose)
    return cylinder

def create_box(
    scene: sapien.Scene,
    pose: sapien.Pose,
    half_size,
    color=None,
    name="",
) -> sapien.Entity:
    """Create a box."""
    half_size:np.ndarray = np.array(half_size)
    builder: sapien.ActorBuilder = scene.create_actor_builder()
    builder.add_box_collision(half_size=half_size)  # Add collision shape
    builder.add_box_visual(half_size=half_size, material=color)  # Add visual shape
    box: sapien.Entity = builder.build(name=name)
    box.set_pose(pose)
    return box

def create_table(
        scene: sapien.Scene,
        pose: sapien.Pose,
        size,
        height,
        thickness=0.1,
        color=(0.8, 0.6, 0.4),
        name="table",
        texture_path=None,  # 添加纹理路径参数
        roughness=0.5,      # 添加粗糙度参数
        metallic=0.0,       # 添加金属度参数
        ) -> sapien.Entity:
            """Create a table (a collection of collision and visual shapes)."""
            builder = scene.create_actor_builder()
        
            # Tabletop
            tabletop_pose = sapien.Pose(
                [0.0, 0.0, -thickness / 2]
            )  # Make the top surface's z equal to 0
            tabletop_half_size = [size / 2, size / 2, thickness / 2]
            builder.add_box_collision(pose=tabletop_pose, half_size=tabletop_half_size)
            builder.add_box_visual(
                pose=tabletop_pose, half_size=tabletop_half_size, material=color
            )

            # Table legs (x4)
            for i in [-1, 1]:
                for j in [-1, 1]:
                    x = i * (size - thickness) / 2
                    y = j * (size - thickness) / 2
                    table_leg_pose = sapien.Pose([x, y, -height / 2])
                    table_leg_half_size = [thickness / 2, thickness / 2, height / 2]
                    builder.add_box_collision(
                        pose=table_leg_pose, half_size=table_leg_half_size
                    )
                    builder.add_box_visual(
                        pose=table_leg_pose, half_size=table_leg_half_size, material=color
                    )

            table = builder.build(name=name)
            table.set_pose(pose)
            return table