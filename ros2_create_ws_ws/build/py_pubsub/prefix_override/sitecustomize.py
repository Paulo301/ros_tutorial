import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/paulo/ros2_create_ws_ws/install/py_pubsub'
