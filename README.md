# TurtleBot3 Custom World and Autonomous Navigation

A ROS 2 Humble project based on the ROBOTIS TurtleBot3 simulation package, featuring a custom Gazebo world, TurtleBot3 simulation, environment mapping, and autonomous navigation using ROS 2 Nav2.

## Features

- Custom Gazebo world.
- TurtleBot3 Burger simulation.
- Custom environment map.
- Single-robot autonomous navigation using ROS 2 Nav2.
- Two-robot autonomous navigation using ROS 2 Nav2.
- AMCL-based robot localization.
- RViz visualization and goal-based navigation.
- Multi-robot simulation in a shared Gazebo world.

## Project Demonstrations

### Single-Robot Autonomous Navigation using ROS 2 Nav2

![Single Robot Screenshot](media/screenshot_2.png)

[Watch Single-Robot Navigation Demonstration](media/single_robot_navigation.webm)

### Two-Robot Autonomous Navigation using ROS 2 Nav2

![Two Robot Screenshot](media/screenshot_1.png)

[Watch Two-Robot Navigation Demonstration](media/two_robot_navigation.webm)

## Technologies

- Ubuntu 22.04
- ROS 2 Humble
- Gazebo Classic
- TurtleBot3 Burger
- SLAM Toolbox
- Nav2
- AMCL
- RViz
- Python

## Project Structure

```text
turtlebot3_simulations/
├── media/
│   ├── screenshot_1.png
│   ├── screenshot_2.png
│   ├── single_robot_navigation.webm
│   └── two_robot_navigation.webm
└── turtlebot3_gazebo/
    ├── launch/
    │   ├── my_custom_world.launch.py
    │   ├── my_custom_world_two_robots.launch.py
    │   └── my_custom_world_two_robots_nav.launch.py
    ├── worlds/
    │   └── my_custom_world.world
    ├── models/
    ├── navigation/
    │   ├── maps/
    │   ├── config/
    │   ├── rviz/
    │   └── scripts/
    ├── CMakeLists.txt
    └── package.xml
```

## Installation and Build

Clone the repository into a ROS 2 workspace's `src` directory.

Install the required ROS 2 dependencies, then build:

```bash
cd ~/Desktop/turtlebot

source /opt/ros/humble/setup.bash

colcon build --symlink-install
```

Source the workspace:

```bash
source install/setup.bash
export TURTLEBOT3_MODEL=burger
```

## Running the Custom World

```bash
ros2 launch turtlebot3_gazebo my_custom_world.launch.py
```

## Running Autonomous Navigation

In a separate terminal:

```bash
source /opt/ros/humble/setup.bash
source ~/Desktop/turtlebot/install/setup.bash

export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_navigation2 navigation2.launch.py \
map:=$(ros2 pkg prefix turtlebot3_gazebo)/share/turtlebot3_gazebo/navigation/maps/my_custom_world_final.yaml \
use_sim_time:=True
```

After RViz opens, use **2D Pose Estimate** to initialize the robot's position on the map. Then use **Nav2 Goal** to send navigation goals.

## Original Project

This project extends the open-source simulation package developed by ROBOTIS.

Original repository: https://github.com/ROBOTIS-GIT/turtlebot3_simulations

The original package and its licensing terms remain acknowledged.