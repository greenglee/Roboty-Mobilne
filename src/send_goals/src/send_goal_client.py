#! /usr/bin/env python
import rospy
import time
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback

# informacja zwrotna z serwera o tym, że nowa wiadomość została odebrana
def feedback_callback(feedback):
    
    print('[Feedback] Going to Goal Pose...')

# inicjalizacja węzła move_base
rospy.init_node('move_base_action_client')

# połączenie z move_base
client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
# czekanie na uruchomienie
client.wait_for_server()

# tworzenie celu do wysłania na serwer
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'map'
goal.target_pose.pose.position.x = 9
goal.target_pose.pose.position.y = 9
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.z = 0.75
goal.target_pose.pose.orientation.w = 0.66

# wysłanie celu do serwera i określenie, która funkcja ma wysłać informację zwrotną
client.send_goal(goal, feedback_cb=feedback_callback)

# oczekiwanie na osiągnięcie celu
client.wait_for_result()

print('[Result] State: %d'%(client.get_state()))