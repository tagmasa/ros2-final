#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class MotionExecutor(Node):
    def __init__(self):
        super().__init__('motion_executor')
        self.publisher = self.create_publisher(
            JointTrajectory,
            '/crane_plus_arm_controller/joint_trajectory',
            10,
        )
        self.subscription = self.create_subscription(
            String,
            '/choreography_label',
            self.callback,
            10,
        )
        self.executed = False
        self.get_logger().info('Waiting for /choreography_label')

    def callback(self, msg):
        if self.executed:
            return
        self.executed = True
        label = msg.data.strip().lower()
        self.get_logger().info(f'Received label: {label}')
        if label == 'celebrate':
            self.celebrate()
        elif label == 'calm':
            self.calm()
        elif label == 'sympathy':
            self.sympathy()
        else:
            self.home()

    def move_to(self, positions, duration=2.0):
        msg = JointTrajectory()
        msg.joint_names = [
            'crane_plus_joint1',
            'crane_plus_joint2',
            'crane_plus_joint3',
            'crane_plus_joint4',
        ]
        point = JointTrajectoryPoint()
        point.positions = positions
        point.velocities = [0.0, 0.0, 0.0, 0.0]
        point.accelerations = [0.0, 0.0, 0.0, 0.0]
        point.time_from_start = Duration(
            sec=int(duration),
            nanosec=int((duration % 1.0) * 1000000000),
        )
        msg.points.append(point)
        self.publisher.publish(msg)
        time.sleep(duration + 0.3)

    def home(self):
        self.move_to([0.0, 0.0, 0.0, 0.0], 2.0)

    def celebrate(self):
        self.home()
        self.move_to([0.55, 0.25, -0.25, 0.15], 1.4)
        self.move_to([-0.55, 0.25, -0.25, 0.15], 1.4)
        self.move_to([0.55, 0.25, -0.25, 0.15], 1.4)
        self.move_to([-0.55, 0.25, -0.25, 0.15], 1.4)
        self.home()

    def calm(self):
        self.home()
        self.move_to([0.20, 0.15, -0.15, 0.10], 2.2)
        self.move_to([-0.20, 0.15, -0.15, 0.10], 2.2)
        self.move_to([0.15, 0.05, -0.05, 0.05], 2.2)
        self.move_to([-0.15, 0.05, -0.05, 0.05], 2.2)
        self.home()

    def sympathy(self):
        self.home()
        self.move_to([0.0, 0.50, -0.40, 0.25], 2.5)
        self.move_to([0.0, 0.35, -0.30, 0.18], 1.8)
        self.move_to([0.22, 0.25, -0.25, 0.15], 1.6)
        self.move_to([-0.22, 0.25, -0.25, 0.15], 1.6)
        self.home()

def main(args=None):
    rclpy.init(args=args)
    node = MotionExecutor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
