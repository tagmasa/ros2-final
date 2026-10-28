#!/usr/bin/env python3
from pathlib import Path
import joblib
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from ament_index_python.packages import get_package_share_directory

class MoodAINode(Node):
    def __init__(self):
        super().__init__('mood_ai_node')
        self.declare_parameter('prompt', '今日も頑張ったから褒めて！')
        self.publisher = self.create_publisher(String, '/choreography_label', 10)
        package_dir = get_package_share_directory('final_project_choreographer')
        model_path = Path(package_dir) / 'model.joblib'
        self.model = joblib.load(model_path)
        prompt = self.get_parameter('prompt').value
        label = self.model.predict([prompt])[0]
        confidence = float(max(self.model.predict_proba([prompt])[0]))
        self.get_logger().info(f'Input: {prompt}')
        self.get_logger().info(f'Prediction: {label}, confidence={confidence:.3f}')
        self.message = String()
        self.message.data = label
        self.count = 0
        self.timer = self.create_timer(0.5, self.publish_label)

    def publish_label(self):
        self.publisher.publish(self.message)
        self.count += 1
        self.get_logger().info(f'Published: {self.message.data} ({self.count}/3)')
        if self.count >= 3:
            self.timer.cancel()

def main(args=None):
    rclpy.init(args=args)
    node = MoodAINode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
