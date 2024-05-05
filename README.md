# wifitest

![PyPI - Downloads](https://img.shields.io/pypi/dm/wifitest)
![PyPI - License](https://img.shields.io/pypi/l/wifitest)
![Read the Docs](https://img.shields.io/readthedocs/wifitest)
![GitHub Tag](https://img.shields.io/github/v/tag/JuanBindez/wifitest?include_prereleases)
<a href="https://pypi.org/project/wifitest/"><img src="https://img.shields.io/pypi/v/wifitest" /></a>

## Python 3 library for wifi testing.

### Install

    sudo pip install wifitest


### usage:

#### import

```python
from wifitest import WifiTest
```
#### scan available wifi networks

```python
s = WifiTest()
s.scan()
```
#### bruteforce on wifi network

```python
SSID = "wifi"
WORDLIST = "wordlist.txt"

wifi = WifiTest()
wifi.bruteforce(SSID, WORDLIST)

```

### CLI

```bash
usage: wifitest [-h] [--ssid SSID] [--wordlist WORDLIST] {scan,bruteforce,events}

Wifitest CLI

positional arguments:
  {scan,bruteforce,events}
                        Operation to perform: scan, bruteforce, or events

options:
  -h, --help            show this help message and exit
  --ssid SSID           SSID of the target Wi-Fi network (required for bruteforce
                        operation)
  --wordlist WORDLIST   Path to the wordlist file (required for bruteforce operation)
```

### Bruteforce

    sudo wifitest bruteforce  --ssid  WIFINAME --wordlist wordlist.txt


### Scan

    sudo wifitest scan

### Events

    sudo wifitest events
