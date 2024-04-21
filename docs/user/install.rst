.. _install:

Installation of wifitest
========================

This guide assumes you already have python and pip installed.

To install wifitest, run the following command in your terminal::

    $ pip install wifitest

Get the Source Code
-------------------

wifitest is actively developed on GitHub, where the source is `available <https://github.com/JuanBindez/wifitest>`_.

You can either clone the public repository::

    $ git clone git://github.com/JuanBindez/wifitest.git

Or, download the `tarball <https://github.com/JuanBindez/wifitest/tarball/master>`_::

    $ curl -OL https://github.com/JuanBindez/wifitest/tarball/master
    # optionally, zipball is also available (for Windows users).

Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages by running::

    $ cd wifitest
    $ python -m pip install .
