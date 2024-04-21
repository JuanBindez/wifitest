from wifitest import WifiTest

SSID = "wifi"
WORDLIST = "wordlist.txt"

wifi = WifiTest()
wifi.bruteforce(SSID, WORDLIST)