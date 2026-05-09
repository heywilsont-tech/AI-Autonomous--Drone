# AI Autonomous Drone Project
# Real-Time AI-Based Autonomous UAV System using PX4, ROS2, and Computer Vision

## Overview
This project is a production-oriented AI-powered autonomous drone platform developed using PX4 Autopilot, ROS2, Gazebo Harmonic, MAVSDK, OpenCV, and YOLOv8. The system is capable of autonomous navigation, waypoint-based missions, obstacle detection, object tracking, telemetry monitoring, and AI-assisted decision making in simulation environments and future real-world deployment.

The project demonstrates the integration of robotics middleware, computer vision, autonomous flight control, and AI perception systems into a modular UAV architecture suitable for research, engineering projects, and advanced robotics applications.

---

# Key Features

- Autonomous drone takeoff and landing
- MAVSDK-based offboard drone control
- Waypoint navigation system
- Autonomous patrol missions
- ROS2 communication framework
- Real-time telemetry monitoring
- OpenCV-based vision processing
- YOLOv8 object detection
- Real-time object tracking
- Obstacle detection and avoidance logic
- AI-assisted navigation decisions
- Gazebo Harmonic simulation integration
- Dockerized deployment support
- GitHub CI/CD workflow
- Jetson Nano deployment support

---

# System Architecture

```text
Camera Input
      ↓
OpenCV Processing
      ↓
YOLOv8 AI Inference
      ↓
Obstacle Detection & Tracking
      ↓
Navigation Decision System
      ↓
MAVSDK Control Layer
      ↓
PX4 Flight Controller
      ↓
Gazebo / Real Drone
