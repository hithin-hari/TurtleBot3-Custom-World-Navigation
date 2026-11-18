import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from tf2_msgs.msg import TFMessage


class TFCombiner(Node):

    def __init__(self):
        super().__init__('tf_combiner')

        self.tf_pub = self.create_publisher(
            TFMessage, '/tf', 100
        )

        static_qos = QoSProfile(
            depth=100,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL
        )

        self.static_pub = self.create_publisher(
            TFMessage, '/tf_static', static_qos
        )

        for robot in ['TB3_1', 'TB3_2']:
            self.create_subscription(
                TFMessage, f'/{robot}/tf',
                self.tf_callback, 100
            )

            self.create_subscription(
                TFMessage, f'/{robot}/tf_static',
                self.static_callback, static_qos
            )

        self.get_logger().info('Combining both robot TF topics')

    def tf_callback(self, msg):
        self.tf_pub.publish(msg)

    def static_callback(self, msg):
        self.static_pub.publish(msg)


def main():
    rclpy.init()
    node = TFCombiner()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
