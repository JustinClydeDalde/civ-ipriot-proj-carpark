import threading
import carpark_sensor
import mqtt_communication
import display_manager


def run_carpark_sensor():
    carpark_sensor.main()

def run_mqtt_communication():
    mqtt_communication.main()

def run_display_manager():
    display_manager.main()

if __name__ == "__main__":

    sensor_thread = threading.Thread(target=run_carpark_sensor)
    mqtt_thread = threading.Thread(target=run_mqtt_communication)
    display_thread = threading.Thread(target=run_display_manager)



    sensor_thread.start()
    mqtt_thread.start()
    display_thread.start()



    sensor_thread.join()
    mqtt_thread.join()
    display_thread.join()

