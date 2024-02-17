import rclpy
from rclpy.node import Node
from my_interfaces.srv import Navigation

def main(args=None):
    rclpy.init(args=args)
    navigation_client = Node('navigation_client')

    # Create a client for the navigation service
    navigation_client_service = navigation_client.create_client(Navigation, 'navigation')
    while not navigation_client_service.wait_for_service(timeout_sec=1.0):
        navigation_client.get_logger().info('Navigation service not available, waiting...')

    # Send a navigation request
    request = Navigation.Request()
    request.x = 10.0  # Replace with the desired destination x-coordinate
    request.y = 5.0   # Replace with the desired destination y-coordinate

    future = navigation_client_service.call_async(request)

    # Wait for the service to complete and print the result
    rclpy.spin_until_future_complete(navigation_client, future)
    if future.result() is not None:
        navigation_client.get_logger().info(f"Navigation result: {future.result().success}")
    else:
        navigation_client.get_logger().error('Service call failed!')

    rclpy.shutdown()

if __name__ == '__main__':
    main()
