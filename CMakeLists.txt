cmake_minimum_required(VERSION 3.0.2)
project(rviz_tools_py)

find_package(catkin REQUIRED
  rospy
  geometry_msgs
  visualization_msgs
  tf
)

catkin_package()
catkin_python_setup()
