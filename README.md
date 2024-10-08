# 6-Axis Manipulator in ROS 2

This repository contains the code and URDF file for simulating a 6-axis robotic manipulator in ROS 2. The package includes everything you need to visualize the manipulator in RViz and launch it in a simulation environment.

## Features
- **6-axis robotic manipulator**: A URDF model representing a 6-DOF robotic arm.
- **ROS 2 package**: Set up to work seamlessly with ROS 2 Foxy or newer distributions.
- **RViz visualization**: Tools to visualize the robot in RViz.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- ROS 2 Humble 
- Colcon build tool
- RViz 2 for visualization

### Installation

Follow these steps to clone the repository and build the package:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/karansspk462000/urdf_tutorial.git
   cd urdf_tutorial
2. **Build the package: Use colcon to build the package:**
    ```bash
    colcon build
3. **Source your workspace: After building, source your workspace to overlay the newly built packages into your environment:**
   ```bash
   source install/setup.bash
4. **Launch the launch file:**
   ```bash
   ros2 launch urdf_tutorial robot_6_dof.launch.py
   
### Contributing
Contributions are welcome! If you have any improvements or bug fixes, feel free to submit a pull request.

### Contact
If you have any questions, feel free to reach out:

- **Email**: karansspk@gmail.com
- **YouTube Channel**: [Subscribe for more tutorials](https://www.youtube.com/@allaboutrobo/videos)

### Links
- [ROS 2 Documentation](https://docs.ros.org/en/humble/index.html)
- [URDF Documentation](https://wiki.ros.org/urdf)


  


