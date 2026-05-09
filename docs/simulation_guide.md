# Gazebo Simulation Guide

## Start PX4 SITL

```bash
cd ~/PX4-Autopilot
make px4_sitl gz_x500
```

## Run MAVSDK Mission

```bash
python3 missions/takeoff_and_land.py
```

## Run Autonomous Patrol

```bash
python3 missions/autonomous_patrol.py
```

## Run Object Detection

```bash
python3 vision/object_detection.py
```

## Run ROS2 Nodes

### Drone Node

```bash
python3 ros2_ws/src/drone_control/drone_node.py
```

### Vision Node

```bash
python3 ros2_ws/src/vision_system/vision_node.py
```

### Navigation Node

```bash
python3 ros2_ws/src/navigation_system/navigation_node.py
```
