# AI Autonomous Drone Project
# Real-Time AI-Based Autonomous UAV System using PX4, ROS2, and Computer Vision

## Overview
This project is a production-oriented AI-powered autonomous drone platform developed using PX4 Autopilot, ROS2, Gazebo Harmonic, MAVSDK, OpenCV, and YOLOv8. The system is capable of autonomous navigation, waypoint-based missions, obstacle detection, object tracking, telemetry monitoring, and AI-assisted decision making in simulation environments and future real-world deployment.

The project demonstrates the integration of robotics middleware, computer vision, autonomous flight control, and AI perception systems into a modular UAV architecture suitable for research, engineering projects, and advanced robotics applications.

Key Features
Autonomous drone takeoff and landing
MAVSDK-based offboard drone control
Waypoint navigation system
Autonomous patrol missions
ROS2 communication framework
Real-time telemetry monitoring
OpenCV-based vision processing
YOLOv8 object detection
Real-time object tracking
Obstacle detection and avoidance logic
AI-assisted navigation decisions
Gazebo Harmonic simulation integration
Dockerized deployment support
GitHub CI/CD workflow
Jetson Nano deployment support
System Architecture

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

Technology Stack
Technology	Purpose
PX4 Autopilot	Flight Control
ROS2 Jazzy	Robotics Middleware
Gazebo Harmonic	Drone Simulation
MAVSDK	Drone Communication
OpenCV	Computer Vision
YOLOv8	AI Object Detection
PyTorch	Deep Learning
Docker	Containerization
GitHub Actions	CI/CD Automation
Folder Structure

AI-Autonomous--Drone/
│
├── ai_models/
├── decision_system/
├── docs/
├── hardware/
├── missions/
├── px4_interface/
├── ros2_ws/
├── simulation/
├── utils/
├── vision/
├── .github/workflows/
├── Dockerfile
├── requirements.txt
└── README.md

Implemented Modules
Flight Control
Autonomous takeoff and landing
Offboard PX4 velocity control
Autonomous waypoint navigation
Patrol mission execution
Mission manager system
AI & Vision
YOLOv8 inference engine
Object detection
Object tracking
Obstacle detection
Camera streaming system
Navigation Intelligence
Path planning
Navigation logic engine
Obstacle avoidance logic
ROS2 Integration
Drone status publisher
Vision publisher node
Navigation subscriber node
Infrastructure
Docker deployment
GitHub Actions CI/CD
Simulation startup scripts
Configuration management
Hardware deployment documentation
Hardware Requirements
Pixhawk Flight Controller
NVIDIA Jetson Nano
GPS Module
Camera Module
ESCs
Brushless Motors
LiPo Battery
Software Requirements
Ubuntu 24.04
ROS2 Jazzy
PX4 Autopilot
Gazebo Harmonic
Python 3.12
MAVSDK
OpenCV
PyTorch
Ultralytics YOLOv8
Installation
Clone Repository
git clone https://github.com/heywilsont-tech/AI-Autonomous--Drone.git
cd AI-Autonomous--Drone
Install Dependencies
pip3 install -r requirements.txt --break-system-packages
Start PX4 SITL
cd ~/PX4-Autopilot
make px4_sitl gz_x500
Run Autonomous Mission
python3 missions/autonomous_patrol.py
Applications
Autonomous surveillance
Smart agriculture
Search and rescue
Disaster response
Infrastructure inspection
Defense and security
AI-based aerial monitoring
Future Enhancements
SLAM integration
Multi-drone coordination
Real-time cloud telemetry dashboard
Reinforcement learning navigation
LiDAR integration
Autonomous landing pad detection
Edge AI optimization
Swarm intelligence
Project Status

Current Status: Active Development

The project currently includes simulation-ready autonomous UAV modules with AI-based perception, ROS2 communication, MAVSDK control, and modular robotics architecture.

Author

Wilson Talakayala

B.Tech Electronics and Instrumentation Engineering
