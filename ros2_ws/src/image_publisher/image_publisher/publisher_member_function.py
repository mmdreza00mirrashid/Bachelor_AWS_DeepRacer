import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, 'image_topic', 10)
        self.timer_ = self.create_timer(1.0, self.publish_image)
        self.bridge = CvBridge()

    def publish_image(self):
        # Capture image (you can replace this with your own image capture logic)
        image = cv2.imread('/home/reza/test.jpeg')

        # Convert image to ROS Image message
        img_msg = self.bridge.cv2_to_imgmsg(image, encoding="bgr8")

        # Publish the message
        self.publisher_.publish(img_msg)
        self.get_logger().info('Image published')

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
