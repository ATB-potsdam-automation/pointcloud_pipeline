from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pointcloud_pipeline',
            executable='perception_node',
            name='perception_node',
            output='screen',
            parameters=[
                {"cloud_topic": "/cloud"},
                {"world_frame": "map"},
                {"camera_frame": "cloud"},
                {"voxel_leaf_size": 0.02}, # m
                {"x_filter_min": 0.1},    # m
                {"x_filter_max": 20.0},     # m
                {"y_filter_min": -3.0},    # m
                {"y_filter_max": 3.0},     # m
                {"z_filter_min": -2.5},    # m
                {"z_filter_max": 4.0},     # m
                {"plane_max_iterations": 100},
                {"plane_distance_threshold": 0.03},
                {"cluster_tolerance": 0.02},
                {"cluster_min_size": 1},
                {"cluster_max_size": 10000}
            ]
        )
     ])
