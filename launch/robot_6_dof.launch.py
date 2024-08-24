from launch import LaunchDescription
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, TimerAction
import os
import launch_ros.descriptions
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Paths to the files
    urdf_file = os.path.join('/home/karan/ros2_ws/src/urdf_tutorial/urdf/robot_model_6_dof.urdf.xacro')

    # Create the LaunchDescription
    ld = LaunchDescription()

    # Declare arguments for configuration files
    ld.add_action(
        DeclareLaunchArgument(
            'robot_description',
            default_value=Command(['xacro ', urdf_file]),
            description='URDF file for the robot'
        )
    )

    # Create nodes
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': launch_ros.descriptions.ParameterValue(
                Command(['xacro ', urdf_file]),
                value_type=str
            )
        }]
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
    )

    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        parameters=[{'use_sim_time': True}],
        arguments=['-d', '/home/karan/ros2_ws/src/urdf_tutorial/config/robot_6_dof.rviz']
    )

    joint_state_publisher_gui_node = Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            parameters=[{'robot_description': Command(['xacro ', urdf_file])}],
    )

    # Add nodes and actions to the LaunchDescription
    ld.add_action(robot_state_publisher)
    # ld.add_action(joint_state_publisher)
    ld.add_action(joint_state_publisher_gui_node)
    
    ld.add_action(rviz2)  


    return ld
















