import pywifi
import time
from pywifi import const


class WifiEvents():
    """
    Class to handle Wi-Fi events such as connection and disconnection.
    """

    def __init__(self):
        self.last_status = None

    def monitor_wifi_events(self):
        """
        Method to start monitoring Wi-Fi events.
        """
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]

        print("Starting Wi-Fi events monitoring...")

        while True:
            current_status = iface.status()
            if current_status != self.last_status:
                if current_status == const.IFACE_CONNECTED:
                    print("Connected to network")
                elif current_status == const.IFACE_DISCONNECTED:
                    print("Disconnected from network")
                self.last_status = current_status

            time.sleep(1)
