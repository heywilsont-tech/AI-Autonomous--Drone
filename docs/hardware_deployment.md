# Hardware Deployment Guide

## Recommended Hardware

- Pixhawk 6C Flight Controller
- NVIDIA Jetson Nano
- CSI Camera
- GPS Module
- 2212 Brushless Motors
- 30A ESCs
- 4S LiPo Battery

## Pixhawk Connections

| Component | Port |
|----------|------|
| GPS | GPS Port |
| Telemetry | TELEM2 |
| Jetson Nano | UART |
| ESCs | MAIN OUT |

## Jetson Nano Communication

Use MAVLink UART communication between Jetson Nano and Pixhawk.

## Deployment Workflow

1. Flash PX4 firmware
2. Connect Jetson Nano
3. Configure MAVLink communication
4. Start ROS2 nodes
5. Launch AI perception stack
6. Arm drone and start autonomous mission
