#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:23:21 2022

@author: hasan
"""

import rospy
import threading
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def robot0_hareket(x, y):
    istemci = actionlib.SimpleActionClient("tb3_0/move_base", MoveBaseAction)
    istemci.wait_for_server()
    hedef = MoveBaseGoal()
    
    x = float(x)
    y = float(y)
        
    hedef.target_pose.header.frame_id = "map"
    hedef.target_pose.pose.position.x = x # hedefin x koordinatı
    hedef.target_pose.pose.position.y = y # hedefin y kordinatı
    hedef.target_pose.pose.orientation.w = 1.0
    
    istemci.send_goal(hedef)
    istemci.wait_for_result()
        
    print(istemci.get_result())
    rospy.loginfo("Goal achieved")
    
def robot1_hareket(x, y):
    istemci = actionlib.SimpleActionClient("tb3_1/move_base", MoveBaseAction)
    istemci.wait_for_server()
    hedef = MoveBaseGoal()
    
    x = float(x)
    y = float(y)
        
    hedef.target_pose.header.frame_id = "map"
    hedef.target_pose.pose.position.x = x # hedefin x koordinatı
    hedef.target_pose.pose.position.y = y # hedefin y kordinatı
    hedef.target_pose.pose.orientation.w = 1.0
    
    istemci.send_goal(hedef)
    istemci.wait_for_result()
        
    print(istemci.get_result())
    rospy.loginfo("Goal achieved")

def robot2_hareket(x, y):
    istemci = actionlib.SimpleActionClient("tb3_2/move_base", MoveBaseAction)
    istemci.wait_for_server()
    hedef = MoveBaseGoal()
    
    x = float(x)
    y = float(y)
        
    hedef.target_pose.header.frame_id = "map"
    hedef.target_pose.pose.position.x = x # hedefin x koordinatı
    hedef.target_pose.pose.position.y = y # hedefin y kordinatı
    hedef.target_pose.pose.orientation.w = 1.0
    
    istemci.send_goal(hedef)
    istemci.wait_for_result()
        
    print(istemci.get_result())
    rospy.loginfo("Goal achieved")
    
