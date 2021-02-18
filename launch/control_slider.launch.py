import os

import launch
import launch_ros.actions
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    urdf_file_name = 'mycobot_urdf.urdf'
    urdf = os.path.join(get_package_share_directory('myCobotROS'), urdf_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()
    params = {'robot_description': robot_desc}
    robot_state_publisher = launch_ros.actions.Node(package='robot_state_publisher',
                                  executable='robot_state_publisher',
                                  output='both',
                                  parameters=[params])

    joint_state_publisher_gui = launch_ros.actions.Node(package='joint_state_publisher_gui',
                                  executable='joint_state_publisher_gui',
                                  output='both')

    control_slider = launch_ros.actions.Node(package='myCobotROS',
                                  executable='control_slider',
                                  output='both')

    rviz_config_file = get_package_share_directory('myCobotROS') + "/mycobot.rviz"
    rviz = launch_ros.actions.Node(package='rviz2',
                     executable='rviz2',
                     name='rviz2',
                     output='log',
                     arguments=['-d', rviz_config_file])

    return launch.LaunchDescription([robot_state_publisher, joint_state_publisher_gui, control_slider, rviz])