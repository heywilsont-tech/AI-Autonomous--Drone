# System Architecture

## Flow

Camera Input -> OpenCV Processing -> YOLO Inference -> Decision System -> MAVSDK -> PX4 -> Drone Control

## Major Components

- PX4 Flight Controller
- MAVSDK Communication Layer
- ROS2 Middleware
- OpenCV Vision Pipeline
- YOLOv8 AI Detection
- Obstacle Avoidance Engine
- Autonomous Navigation System
- Gazebo Simulation Environment

## Communication Protocols

- MAVLink
- DDS (ROS2)
- UART

## Deployment Platforms

- Ubuntu 24.04
- Jetson Nano
- Pixhawk Flight Controller
