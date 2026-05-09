# Setup Guide

## Ubuntu 24.04

Install dependencies:

```bash
sudo apt update
sudo apt install git python3-pip python3-colcon-common-extensions
```

## PX4 Setup

```bash
git clone https://github.com/PX4/PX4-Autopilot.git
cd PX4-Autopilot
bash ./Tools/setup/ubuntu.sh
```

## Run Simulation

```bash
make px4_sitl gz_x500
```

## Install MAVSDK

```bash
pip3 install mavsdk --break-system-packages
```

## Install OpenCV and YOLO

```bash
pip3 install opencv-python ultralytics --break-system-packages
```
