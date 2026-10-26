import numpy as np
import rclpy
from rclpy.node import Node
from neato2_interfaces.msg import Bump 
from geometry_msgs.msg import Twist

class e_stop(Node):
    def __init__(self):
        super().__init__("emergency_stop_node")
        self.create_timer(0.1, self.run_loop)
        self.bump_state = False
        self.sub = self.create_subscription(Bump, "bump", self.process_collision, 10)
        self.pub = self.create_publisher(Twist, "cmd_vel", 10)

    def process_collision(self, msg):
        if (msg.left_front == 1 or msg.right_front == 1 or msg.left_side == 1 or msg.right_side == 1):
            self.bump_state = True


    def run_loop(self):
        vel = Twist()

        if self.bump_state:
            vel.linear.x = 0.0
        else:
            vel.linear.x = 0.1

        self.pub.publish(vel)


def main(args=None):
    rclpy.init(args=args)  # Initialize ROS2 network
    node = e_stop()  # Create our node
    rclpy.spin(node)  # Run our node
    rclpy.shutdown()  # If interrupted, gracefully shutdown the ROS2 netwo


if __name__ == '__main__':
    main()
