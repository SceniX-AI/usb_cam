from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution


def launch_setup(context, *args, **kwargs):
    camera_name = LaunchConfiguration("camera_name")
    camera_namespace = LaunchConfiguration("camera_namespace")
    param_file = LaunchConfiguration("param_file")

    ld = []  # launch description list

    webcam = Node(
        package="usb_cam",
        executable="usb_cam_node_exe",
        namespace=camera_namespace,
        name=camera_name,
        parameters=[param_file],
    )
    ld.append(webcam)

    return ld


def generate_launch_description():
    declared_arguments = [
        DeclareLaunchArgument(
            name="camera_name",
            default_value="my_camera",
            description="camera_name",
        ),
        DeclareLaunchArgument(
            name="camera_namespace",
            default_value="usb",
            description="camera_namespace",
        ),
        DeclareLaunchArgument(
            name="param_file",
            default_value=PathJoinSubstitution([FindPackageShare("usb_cam"), "config", "params.yaml"]),
            description="camera_namespace",
        ),
    ]
    return LaunchDescription(declared_arguments + [OpaqueFunction(function=launch_setup)])
