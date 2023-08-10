from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from math import pi
import os

def generate_launch_description():

    return LaunchDescription([
        SetEnvironmentVariable('RCUTILS_LOGGING_BUFFERED_STREAM', '1'),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory("roverrobotics_driver"), 'launch', 'miti.launch.py')])),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory("roverrobotics_driver"), 'launch', 'ps4_controller.launch.py')])),
    ])
