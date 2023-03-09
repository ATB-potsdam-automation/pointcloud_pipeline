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
                {"camera_frame": "cloud_adjusted"},
                {"voxel_leaf_size": 0.02}, # mm
                {"x_filter_min": 0.1},    # mm
                {"x_filter_max": 20.0},     # mm
                {"y_filter_min": -3.0},    # mm
                {"y_filter_max": 3.0},     # mm
                {"z_filter_min": -2.5},    # mm
                {"z_filter_max": 4.0},     # mm
                {"plane_max_iterations": 100},
                {"plane_distance_threshold": 0.03},
                {"cluster_tolerance": 0.02},
                {"cluster_min_size": 1},
                {"cluster_max_size": 10000}
            ]
        )
     ])
