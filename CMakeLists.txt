cmake_minimum_required(VERSION 3.0.2)
project(hand_snn)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS rostest roslib roscpp rospy std_msgs std_srvs sensor_msgs sr_robot_msgs control_msgs controller_manager_msgs
        sr_utilities diagnostic_msgs dynamic_reconfigure self_test urdf gazebo_msgs)
# find_package(gazebo REQUIRED)
include_directories(include ${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS} ${SDFormat_INCLUDE_DIRS})

# catkin_python_setup()
catkin_package(
        CATKIN_DEPENDS roslib roscpp rospy std_msgs std_srvs sensor_msgs sr_robot_msgs control_msgs controller_manager_msgs sr_utilities
        diagnostic_msgs dynamic_reconfigure self_test urdf gazebo_msgs ros_ethercat_model position_controllers
        # LIBRARIES HandCommander SrVirtual
)

###########
## Build ##
###########