#!/bin/bash

echo "Starting PX4 SITL with Gazebo Harmonic"

cd ~/PX4-Autopilot || exit

make px4_sitl gz_x500
