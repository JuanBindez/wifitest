import pywifi
from pywifi import const

class WifiScan():
    """
    Class to perform Wi-Fi network scanning and print details of the scanned networks.
    """    
    
    def scan_wifi_networks(self):
        """
        Scan for Wi-Fi networks and return the scan results.

        Returns:
            list: A list of network scan results.
        """
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]  # obtém a primeira interface Wi-Fi disponível
        iface.scan()
        return iface.scan_results()

    def print_wifi_details(self, networks):
        """
        Print details of the scanned Wi-Fi networks.

        Args:
            networks (list): A list of network scan results.
        """
        for network in networks:
            print("SSID:", network.ssid)
            print("BSSID:", network.bssid)
            print("Signal Strength (dBm):", network.signal)
            print("Frequency (MHz):", network.freq)
            print("Security:", self.translate_encryption_type(network.akm))
            print("----------------------------------")

    def translate_encryption_type(self, encryption_type):
        """
        Translate encryption type code to human-readable format.

        Args:
            encryption_type (int): Encryption type code.

        Returns:
            str: Human-readable encryption type.
        """
        if encryption_type == const.AKM_TYPE_NONE:
            return "Open"
        elif encryption_type == const.AKM_TYPE_WPA:
            return "WPA"
        elif encryption_type == const.AKM_TYPE_WPAPSK:
            return "WPA-PSK"
        elif encryption_type == const.AKM_TYPE_WPA2:
            return "WPA2"
        elif encryption_type == const.AKM_TYPE_WPA2PSK:
            return "WPA2-PSK"
        else:
            return "Unknown"