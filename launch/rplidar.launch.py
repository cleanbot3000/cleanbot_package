import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.2:1.0-port0', #this is the bottom right USB port when looking at the USB port openings
                'frame_id': 'lidar_frame',
                'angle_compensate': True,
                'scan_mode': 'Standard'
            }]
        )
    ])