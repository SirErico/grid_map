from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    folder_path_arg = DeclareLaunchArgument(
        'folder_path',
        default_value='/ws/src/grid_map/grid_map_pcl/worlds/lunaryard',
        description='Path to the folder containing the PCD file'
    )

    pcd_filename_arg = DeclareLaunchArgument(
        'pcd_filename',
        default_value='lunaryard_middle.pcd',
        description='Name of the PCD file'
    )

    node_params = {
        'folder_path': LaunchConfiguration('folder_path'),
        'pcd_filename': LaunchConfiguration('pcd_filename'),
        'map_rosbag_topic': 'grid_map',
        'output_grid_map': 'elevation_map.bag',
        'map_frame': 'map',
        'map_layer_name': 'elevation',
        'prefix': '',
        'set_verbosity_to_debug': True
    }

    pcl_loader_node = Node(
        package='grid_map_pcl',
        executable='grid_map_pcl_loader_node',
        name='grid_map_pcl_loader_node',
        output='screen',
        parameters=[node_params],
        remappings=[
            ('grid_map_from_raw_pointcloud', 'grid_map')
        ]
    )

    ld = LaunchDescription()

    ld.add_action(folder_path_arg)
    ld.add_action(pcd_filename_arg)
    ld.add_action(pcl_loader_node)
    # ld.add_action(grid_map_republisher)  # Uncomment if you want continuous publishing

    return ld
