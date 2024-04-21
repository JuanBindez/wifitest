.. _quickstart:

Quickstart:
===========

**import**::

        from wifitest import WifiTest


**scan available wifi networks**::

        s = WifiTest()
        s.scan()

**bruteforce**::

        SSID = "wifi"
        WORDLIST = "wordlist.txt"

        b = WifiTest()
        b.bruteforce(SSID, WORDLIST)

