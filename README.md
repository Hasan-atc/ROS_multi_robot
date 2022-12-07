# ROS Multi Robot Filo Management
In this work title, I will show you how to set up a ROS-based multi-robot system and make it ready for use.

![rviz_set_pose](https://user-images.githubusercontent.com/74008306/206080690-dccaba94-670b-4819-bfed-643c6b38a016.png)


# Requiremets :large_blue_diamond:
``` UBUNTU 18.04 ```

``` ROS Melodic ```

``` Turtlebot3 or Turtlebot2 (Made using Turtlebot3) ```

# Installations :arrow_down:
:small_red_triangle_down: Before starting make a work space:

```` 
mkdir -p filo_ws
cd filo_ws/
mkdir -p src
cd src/
````
:small_red_triangle_down: Start downloading necessary files to the workspace:

````
git clone https://github.com/Hasan-atc/ROS_multi_robot.git
git clone https://github.com/ros-planning/navigation.git
git clone https://github.com/ros/geometry2.git
````

:small_red_triangle_down: Let's compile the workspace:
````
cd .. # Directory is filo_ws
catkin_make
````

:small_red_triangle_down: Edit '.bashrc' file
````
Type this code in terminal screen:
gedit ~/.bashrc

Paste the following into the opened txt file. Save and exit later :
source /opt/ros/melodic/setup.bash
export TURTLEBOT3_MODEL=waffle_pi
source ~/filo_ws/devel/setup.bash

export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=localhost

Type this code in terminal screen:
bash
````

# Operating the Multi-Robot System 
:heavy_check_mark: First Terminal -- Initializing the Gazebo simulation environment:
````
roslaunch turtlebot3_gazebo multi_turtlebot3.launch
````
![image](https://user-images.githubusercontent.com/74008306/206093959-7d5f80fd-b833-43ee-9165-2c4dcc62d108.png)


:heavy_check_mark: Secondary Terminal -- Initializing the RVİZ simulation environment:
````
roslaunch turtlebot3_navigation multi_nav_bringup.launch
````
![rviz_set_pose](https://user-images.githubusercontent.com/74008306/206094379-46c64d37-bc73-42a3-8e17-a6b951e0be7c.png)

:exclamation: In order for the robot positions to come in this way, you must determine the positions of the robots with the help of 2D Pose Estimate.

:exclamation: As described in the previous repo, mapping is required.

# Enabling movement of robots :robot:
:arrow_right: Movement through Rviz:
```
With the 2D Nav Goal button, the robot can be moved to the desired location.
```

:arrow_right: Movement with Topics:
````
move = actionlib.SimpleActionClient("tb3_0/move_base", MoveBaseAction) # Different move_base topic is published for each robot
goal = MoveBaseGoal()
````

````
goal.target_pose.header.frame_id = "map"  # Frame required to determine Target Points
goal.target_pose.pose.position.x = x  # Target Points X coordinate
goal.target_pose.pose.position.y = y  # Target Points Y coordinate
goal.target_pose.pose.position.w = 1.0  # Position angle of the robot
````

````
istemci.send_goal(hedef)  # Sending target points to the robot
````

# Ease of use with the interface :checkered_flag:
:bulb: With the buttons and information sections on the interface, you can decide which positions all the robots will go to:
````
cd filo_ws/src/code
chmod +x multi_robot.py & chmod +x robots.py
python multi_robot.py
````
:exclamation: Make sure the multi_robot.py and robots.py files are in the same directory

![image](https://user-images.githubusercontent.com/74008306/206100456-8f451f6c-73dc-4f7d-a057-2d1fb53ac193.png)

# Result
:tada:Congratulations, at the end of this study, you learned to move 3 different robots with interface connection autonomously on the map. 

For more detailed information, I recommend you to review the links that I will reach in the resources section. Stay with the robots.:tada:

# Resources :handshake:
:small_orange_diamond: https://osrf.github.io/ros2multirobotbook/

:small_orange_diamond: http://wiki.ros.org/navigation

:small_orange_diamond: https://pypi.org/project/PyQt5/

:small_orange_diamond: https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/

# Coming Soon :1st_place_medal:
:white_check_mark: I will open source [Teknofest Autonomous Vehicle Competition](https://teknofest.org/en/competitions/competition/29) codes

[![Instagram Badge](https://img.shields.io/badge/-Instagram-C13584?style=flat-quare&labelColor=red&logo=instagram&logoColor=white&link=link)](https://www.instagram.com/hsnatc_02/?next=%2F)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hasan-atici-6180481b9)
