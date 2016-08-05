#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of IoT related modules (Internet of Things)
"""

from ..installhelper.module_install import ModuleInstall


def iot_set():
    """
    list of sphinx themes and others helpers for sphinx, it requires the modules in set *small*
    """
    mod = [
        ModuleInstall(
            'phue', 'pip', purpose="A Philips Hue Python library", usage="IoT"),
        ModuleInstall('ledcontroller', 'pip',
                      purpose="Controller library for limitlessled/easybulb/milight Wi-Fi LEDs", usage="IoT"),

        ModuleInstall('enum-compat', 'pip',
                      purpose="enum/enum34 compatibility package"),
        ModuleInstall('netifaces', 'pip',
                      purpose="Portable network interface information."),
        ModuleInstall('zeroconf', 'pip',
                      purpose="Multicast DNS Service Discovery for Python, originally by Paul Scott-Murphy."),
        ModuleInstall(
            'protobuf', 'pip', purpose="Protocol Buffers are Google’s data interchange format"),
        ModuleInstall('pychromecast', 'pip',
                      purpose="Library for Python 2 and 3 to communicate with the Google Chromecast."),
        ModuleInstall('pyuserinput', 'pip',
                      purpose="A simple, cross-platform module for mouse and keyboard control"),
        ModuleInstall('tellcore-py', 'pip', usage="IoT",
                      purpose="Python wrapper for Telldus' home automation library"),
        ModuleInstall('python-nmap', 'pip',
                      purpose="This is a python class to use nmap and access scan results from python3"),
        ModuleInstall('python-magic', 'pip',
                      purpose="File type identification using libmagic"),
        ModuleInstall('websocket-client', 'pip',
                      purpose="WebSocket client for python. hybi13 is supported."),
        ModuleInstall('pushbullet.py', 'pip', usage="IoT",
                      purpose="A simple python client for pushbullet.com"),
        ModuleInstall('python-nest', 'pip', usage="IoT",
                      purpose="Python API and command line tool for talking to the Nest™ Thermostat"),
        ModuleInstall('VarEvents', 'pip', usage="IoT",
                      purpose="Python module to create variables that can raise custom events."),
        ModuleInstall('PyISY', 'pip', usage="IoT",
                      purpose="Python module to talk to ISY994 from UDI."),
        ModuleInstall('python-pushover', 'pip', usage="IoT",
                      purpose="Comprehensive bindings and command line utility for the Pushover notification service"),
        ModuleInstall('transmissionrpc', 'pip', usage="IoT",
                      purpose="Python module that implements the Transmission bittorent client RPC protocol."),
        ModuleInstall('pyowm', 'pip', usage="DATA",
                      purpose="A Python wrapper around the OpenWeatherMap web API"),
        ModuleInstall('sleekxmpp', 'pip', usage="IoT",
                      purpose="SleekXMPP is an elegant Python library for XMPP (aka Jabber, Google Talk, etc)."),
        ModuleInstall('dnspython3', 'pip', usage="IoT",
                      purpose="A DNS toolkit for Python 3.x"),
        ModuleInstall('blockchain', 'pip', usage="IoT",
                      purpose="Blockchain API library (v1)"),
        ModuleInstall('python-mpd2', 'pip', usage="IoT",
                      purpose="A Python MPD client library"),
        ModuleInstall('hikvision', 'pip', usage="IoT",
                      purpose="Provides a python interface to interact with a hikvision camera"),
        ModuleInstall('colorlog', 'pip',
                      purpose="Log formatting with colors!"),
        ModuleInstall('jsonrpc-requests', 'pip',
                      purpose="A JSON-RPC client library, backed by requests"),
        ModuleInstall(
            'cookies', 'pip', purpose="Friendlier RFC 6265-compliant cookie parser/renderer"),
        ModuleInstall(
            'mock', 'pip', purpose="Rolling backport of unittest.mock for all Pythons"),
        ModuleInstall('pbr', 'pip', purpose="Python Build Reasonableness"),
        ModuleInstall('responses', 'pip',
                      purpose="A utility library for mocking out the `requests` Python library."),
        ModuleInstall('python-forecastio', 'pip', usage="IoT",
                      purpose="A thin Python Wrapper for the Forecast.io weather API"),
        ModuleInstall('pyserial', 'pip', mname="serial",
                      usage="IoT", purpose="Python Serial Port Extension"),
        ModuleInstall('PyMata', 'pip', usage="IoT",
                      purpose="A Python Protocol Abstraction Library For Arduino Firmata"),
        ModuleInstall('pyRFXtrx', 'pip', mname="RFXtrx",
                      purpose="A Python library to communicate with the RFXtrx family of devices"),
        # ModuleInstall('pymysensors', 'github', 'theolind', mname="mysensors",
        # purpose="Python API for talking to a MySensors gateway"),
        ModuleInstall('pynetgear', 'pip', usage="IoT",
                      purpose="Access Netgear routers using their SOAP API"),
        ModuleInstall('netdisco', 'pip', usage="IoT",
                      purpose="Discover devices on your local network"),
        ModuleInstall('pywemo', 'pip', usage="IoT",
                      purpose="Access WeMo switches using their SOAP API"),
        ModuleInstall('python-wink', 'pip', mname="pywink",
                      purpose="Python implementation of the Wink API"),
        ModuleInstall('slacker', 'pip', purpose="Slack API client"),
        ModuleInstall(
            'vincenty', 'pip', purpose="Calculate the geographical distance between 2 points with extreme accuracy."),
        ModuleInstall('pyusb', 'pip', usage="IoT",
                      purpose="Python USB access module"),
        ModuleInstall('temperusb', 'pip', usage="IoT",
                      purpose="Reads temperature from TEMPerV1 devices (USB 0c45:7401)"),
        ModuleInstall('pyedimax', 'github', 'rkabadi', usage="IoT",
                      purpose="Pyedimax is a python library for interfacing with the Edimax Smart Plug switches SP-1101W and SP-2101W"),

        # Uncomment for Raspberry Pi
        # ModuleInstall('RPi.GPIO', 'pip'),
        # uncomment on a Raspberry Pi / Beaglebone
        # ModuleInstall('Adafruit_Python_DHT', 'github', 'mala-zaba', purpose="Adafruit temperature/humidity sensor", usage="IoT"),

        ModuleInstall('paho-mqtt', 'pip', usage="IoT",
                      purpose="MQTT version 3.1/3.1.1 client class"),
        # ModuleInstall('pymodbus', 'github', 'bashwork', usage='IoT'),
        ModuleInstall('python-verisure', 'github',
                      'persandstrom', usage='IoT', purpose="A python module for reading and changing status of verisure devices through mypages."),

        ModuleInstall('homeassistant', 'pip',
                      purpose="Home Assistant is a home automation platform running on Python 3. " +
                      "The goal of Home Assistant is to be able to track and control all devices at home and offer a platform for automating control.",
                      web="https://github.com/balloob/home-assistant/",
                      usage="IoT"),
    ]
    return [_ for _ in mod if _ is not None]
