.. wifitest documentation master file,

wifitest
============
Release v\ |version|. (:ref:`Installation<install>`)


.. image:: https://img.shields.io/pypi/v/wifitest.svg
  :alt: Pypi
  :target: https://pypi.python.org/pypi/wifitest/

.. image:: https://img.shields.io/pypi/pyversions/wifitest.svg
  :alt: Python Versions
  :target: https://pypi.python.org/pypi/wifitest/


**wifitest** wifitest is an open source tool written in Python designed for wifi testing..
-------------------------------------------------------------------------------------------------------------------------------------------

**Behold, a perfect balance of simplicity versus flexibility**::

    SSID = "wifi"
    WORDLIST = "wordlist.txt"

    wifi = WifiTest()
    wifi.bruteforce(SSID, WORDLIST)

Features
--------

- scan available wifi networks.
- bruteforce on wifi network.
- events of the wifi networks.

The User Guide
---------------
This part of the documentation begins with some background information about
the project, then focuses on step-by-step instructions for getting the most out
of wifitest.

.. toctree::
   :maxdepth: 2

   user/install
   user/cli
   user/quickstart
   user/bruteforce
   user/events
   user/scan


The API Documentation
-----------------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api

