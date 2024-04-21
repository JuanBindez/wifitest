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
