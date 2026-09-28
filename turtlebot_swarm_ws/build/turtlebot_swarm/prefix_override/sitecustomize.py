import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/manish/turtlebot_swarm_ws/install/turtlebot_swarm'
