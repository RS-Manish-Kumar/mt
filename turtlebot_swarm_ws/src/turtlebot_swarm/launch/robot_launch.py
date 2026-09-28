#!/usr/bin/env python3

import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions.path_join_substitution import PathJoinSubstitution

from ament_index_python.packages import get_package_share_directory

from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController


def create_robot(robot_name, namespace):

    package_dir = get_package_share_directory(
        'webots_ros2_turtlebot'
    )

    robot_description = os.path.join(
        package_dir,
        'resource',
        'turtlebot_webots.urdf'
    )

    swarm_package = get_package_share_directory(
    'turtlebot_swarm'
    )

    ros2_control = os.path.join(
        swarm_package,
        'resource',
        'swarm_ros2control.yml'
    )


    return WebotsController(

        robot_name=robot_name,

        namespace=namespace,

        parameters=[

            {
                'robot_description': robot_description,
                'use_sim_time': True,
                'set_robot_state_publisher': True
            },

            ros2_control,

            {
                'controller_manager.update_rate': 50
            }

        ],

        remappings=[

            (
                '/diffdrive_controller/cmd_vel_unstamped',
                'cmd_vel'
            ),

            (
                '/diffdrive_controller/odom',
                'odom'
            )

        ],

        respawn=True

    )



def generate_launch_description():

    package_dir = get_package_share_directory(
        'turtlebot_swarm'
    )


    world = LaunchConfiguration(
        'world'
    )


    webots = WebotsLauncher(

        world=PathJoinSubstitution(
            [
                package_dir,
                'worlds',
                world
            ]
        ),

        ros2_supervisor=True
    )


    robot1 = create_robot(
        'robot1',
        'robot1'
    )

    robot2 = create_robot(
        'robot2',
        'robot2'
    )

    robot3 = create_robot(
        'robot3',
        'robot3'
    )

    robot1_diffdrive = Node(
        package='controller_manager',
        executable='spawner',
        namespace='robot1',
        arguments=[
            'diffdrive_controller',
            '--controller-manager',
            '/robot1/controller_manager'
        ],
    )


    robot1_joint = Node(
        package='controller_manager',
        executable='spawner',
        namespace='robot1',
        arguments=[
            'joint_state_broadcaster',
            '--controller-manager',
            '/robot1/controller_manager'
        ],
    )


    robot2_diffdrive = Node(
        package='controller_manager',
        executable='spawner',
        namespace='robot2',
        arguments=[
            'diffdrive_controller',
            '--controller-manager',
            '/robot2/controller_manager'
        ],
    )


    robot2_joint = Node(
        package='controller_manager',
        executable='spawner',
        namespace='robot2',
        arguments=[
            'joint_state_broadcaster',
            '--controller-manager',
            '/robot2/controller_manager'
        ],
    )


    robot3_diffdrive = Node(
        package='controller_manager',
        executable='spawner',
        namespace='robot3',
        arguments=[
            'diffdrive_controller',
            '--controller-manager',
            '/robot3/controller_manager'
        ],
    )


    robot3_joint = Node(
        package='controller_manager',
        executable='spawner',
        namespace='robot3',
        arguments=[
            'joint_state_broadcaster',
            '--controller-manager',
            '/robot3/controller_manager'
        ],
    )


    return LaunchDescription([

        DeclareLaunchArgument(
            'world',
            default_value='multi_turtlebot.wbt'
        ),

        webots,

        webots._supervisor,

        robot1,
        robot2,
        robot3,


        robot1_diffdrive,
        robot1_joint,

        robot2_diffdrive,
        robot2_joint,

        robot3_diffdrive,
        robot3_joint

    ])