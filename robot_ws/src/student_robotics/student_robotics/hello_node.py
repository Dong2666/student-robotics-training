import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class HelloNode(Node):
    """Minimal node: announces itself, then idles until interrupted."""

    def __init__(self):
        super().__init__('hello_node')
        self.get_logger().info('student_robotics hello node started')


def main(args=None):
    rclpy.init(args=args)
    node = HelloNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
