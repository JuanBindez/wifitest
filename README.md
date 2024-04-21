# wifitest

## Python 3 library for wifi testing.

### Install

    sudo pip install wifitest


### usage

```python

from wifitest import WifiTest

SSID = "wifi"
WORDLIST = "wordlist.txt"

wifi = WifiTest()
wifi.bruteforce(SSID, WORDLIST)

```
