import paho.mqtt.publish as publish

class Car:


    def __init__(self, license_plate, mqtt_broker, mqtt_port):

        self.license_plate = license_plate
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port

    def _send_mqtt_message(self, event_type):

        topic = f"sensor/car/{event_type}"
        message = f"{event_type}, {self.license_plate}"
        publish.single(topic, message, hostname=self.mqtt_broker, port=self.mqtt_port)

    def enter_carpark(self):

        self._send_mqtt_message("entered")

    def exit_carpark(self):

        self._send_mqtt_message("exited")

# Example usage
my_car = Car("ABC123", "localhost", 1883)  # Replace with actual broker address and port
my_car.enter_carpark()
my_car.exit_carpark()
