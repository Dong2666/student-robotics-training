from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    rate = LaunchConfiguration('rate')

    return LaunchDescription([
        DeclareLaunchArgument(
            'rate',
            default_value='1.0',
            description='Status publish rate in Hz',
        ),
        Node(
            package='student_robotics',
            executable='status_publisher',
            output='screen',
            parameters=[{'rate': rate}],
        ),
        Node(
            package='student_robotics',
            executable='status_subscriber',
            output='screen',
        ),
    ])
