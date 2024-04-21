from wifitest import WifiTest

SSID = "wifi"
WORDLIST = "wordlist.txt"

wifi = WifiTest()
wifi.scan()
wifi.bruteforce(SSID, WORDLIST)
wifi.events()