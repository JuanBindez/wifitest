# this is part of the wifitest project.
#
# Copyright ©  2024 Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


from wifitest.bruteforce import BruteForce
from wifitest.events import WifiEvents
from wifitest.scan import WifiScan


class WifiTest:
    def scan(self):
        wifi_scan = WifiScan()
        print("Scanning for Wi-Fi networks...")
        print("Wi-Fi networks found:")
        networks = wifi_scan.scan_wifi_networks()
        wifi_scan.print_wifi_details(networks)

    def bruteforce(self, ssid: str, wordlist: str):
        bf = BruteForce()
        bf.brute_force_attack(ssid, wordlist)

    def events(self):
        events = WifiEvents()
        events.monitor_wifi_events()