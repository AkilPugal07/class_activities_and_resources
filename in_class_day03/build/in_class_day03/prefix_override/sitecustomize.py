import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/akprime07/ros2_ws/src/class_activities_and_resources/in_class_day03/install/in_class_day03'
