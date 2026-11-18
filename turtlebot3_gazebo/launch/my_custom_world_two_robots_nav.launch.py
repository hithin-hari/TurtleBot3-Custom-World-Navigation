import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    nav2_launch_file = os.path.join(
        get_package_share_directory('nav2_bringup'),
        'launch',
        'bringup_launch.py'
    )

    navigation_dir = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'navigation'
    )

    map_file = os.path.join(
        navigation_dir, 'maps', 'my_custom_world_final.yaml'
    )

    robot1_params = os.path.join(
        navigation_dir, 'config', 'burger_tb3_1.yaml'
    )

    robot2_params = os.path.join(
        navigation_dir, 'config', 'burger_tb3_2.yaml'
    )


    robot1_nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_launch_file),
        launch_arguments={
            'namespace': 'TB3_1',
            'use_namespace': 'True',
            'slam': 'False',
            'map': map_file,
            'use_sim_time': 'True',
            'params_file': robot1_params,
            'autostart': 'True',
            'use_composition': 'False',
        }.items()
    )

    robot2_nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_launch_file),
        launch_arguments={
            'namespace': 'TB3_2',
            'use_namespace': 'True',
            'slam': 'False',
            'map': map_file,
            'use_sim_time': 'True',
            'params_file': robot2_params,
            'autostart': 'True',
            'use_composition': 'False',
        }.items()
    )

    return LaunchDescription([
        robot1_nav2,
        robot2_nav2
    ])
