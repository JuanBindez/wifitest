.. _bruteforce:

Bruteforce:
===========

**bruteforce on wifi network:**::

        SSID = "wifi"
        WORDLIST = "wordlist.txt"

        wifi = WifiTest()
        wifi.bruteforce(SSID, WORDLIST)
