# ImagePublisher ROS 2 Node Documentation

## Overview

The `ImagePublisher` node is a ROS 2 Python node that captures an image from a file, converts it into a ROS Image message, and publishes it to a specific topic. It is designed to demonstrate a simple image publishing functionality within the ROS 2 framework.

## Node Functionality

The primary functionalities of the `ImagePublisher` node include:

1. **Image Capture:**
   - The node captures an image from a specified file path. Users can replace the file path with the location of their own image file.

2. **ROS Image Message Conversion:**
   - The captured image is converted into a ROS Image message using the `cv_bridge` library. This library facilitates the conversion between OpenCV images and ROS Image messages.

3. **Image Publishing:**
   - The converted ROS Image message is published to the specified ROS topic ('image_topic') using the `rclpy` library.

## Dependencies

- ROS 2 (Robot Operating System 2)
- `sensor_msgs` ROS 2 package (for the `Image` message type)
- `cv_bridge` library for image conversion
- OpenCV library for image processing

## Node Parameters

- **File Path Parameter:**
  - The file path to the image that will be captured and published. Users need to replace the default file path in the code with the path to their own image file to avoid any problems.

## ROS Topics

- **Published Topics:**
  - `/image_topic` (sensor_msgs/Image)
    - The ROS topic to which the converted image messages are published.

## Building and Running the Node

1. **Install Dependencies:**
   ```bash
   sudo apt install ros-foxy-sensor-msgs
  

2. **Build the Package:**
   ```bash
   colcon build --packages-select image_publisher
   


3. **Source the Setup Script:**
   ```bash
   source install/setup.bash


4. **Run the Node:**
   ```bash
   ros2 run image_publisher sender


5. **Recieve the image:**
   in a new terminal:
   ```bash
   ros2 run image_tools showimage image:=/image_topic



