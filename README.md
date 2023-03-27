#  pointcloud_pipeline

Repository with pointcloud pipeline package for project LANARVi in ROS2.

# How to run the test

1. Build the package - ```colcon build```.

2. Source workspace - ```source install/setup.bash```.

3. Run the launch_file, specify the path with argument data_path where pcl data can be stored - ```ros2 launch pointcloud_pipeline processing_node.launch.py data_path:='/path/to/directory/'```.