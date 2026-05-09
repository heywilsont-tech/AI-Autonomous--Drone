# NVIDIA Jetson Nano Setup

## Update System

```bash
sudo apt update && sudo apt upgrade -y
```

## Install Python Dependencies

```bash
sudo apt install python3-pip -y
```

## Install PyTorch

Use NVIDIA optimized PyTorch builds for Jetson.

## Install OpenCV

```bash
sudo apt install python3-opencv -y
```

## Clone Repository

```bash
git clone https://github.com/heywilsont-tech/AI-Autonomous--Drone.git
```

## Run AI Detection

```bash
python3 vision/object_detection.py
```
