#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of IoT related modules (Internet of Things)
"""

from ..installhelper.module_install import ModuleInstall


def iot_set():
    """
    list of sphinx themes
    """
    mod = [
        ModuleInstall('homeassistant', 'pip',
                      purpose="Home Assistant is a home automation platform running on Python 3. The goal of Home Assistant is to be able to track and control all devices at home and offer a platform for automating control.",
                      web="https://github.com/balloob/home-assistant/",
                      usage="IoT"),
        ModuleInstall(
            'phue', 'pip', purpose="A Philips Hue Python library", usage="IoT"),
        ModuleInstall('ledcontroller', 'pip',
                      purpose="Controller library for limitlessled/easybulb/milight Wi-Fi LEDs", usage="IoT"),

        ModuleInstall('enum-compat', 'pip'),
        ModuleInstall('netifaces', 'pip'),
        ModuleInstall('protobuf-py3', 'pip', mname="google.protobuf"),
        ModuleInstall('zeroconf', 'pip'),
        ModuleInstall('pychromecast', 'pip'),
        ModuleInstall('pyuserinput', 'pip'),
        ModuleInstall('tellcore-py', 'pip', usage="IoT"),
        ModuleInstall('python-nmap', 'pip'),
        ModuleInstall('python-magic', 'pip'),
        ModuleInstall('websocket-client', 'pip'),
        ModuleInstall('pushbullet.py', 'pip', usage="IoT"),
        ModuleInstall('python-nest', 'pip', usage="IoT"),
        ModuleInstall('pydispatcher', 'pip'),
        ModuleInstall('VarEvents', 'pip', usage="IoT"),
        ModuleInstall('PyISY', 'pip', usage="IoT"),
        ModuleInstall('python-pushover', 'pip', usage="IoT"),
        ModuleInstall('transmissionrpc', 'pip', usage="IoT"),
        ModuleInstall('pyowm', 'pip', usage="DATA"),
        ModuleInstall('sleekxmpp', 'pip', usage="IoT"),
        ModuleInstall('dnspython3', 'pip', usage="IoT"),
        ModuleInstall('blockchain', 'pip', usage="IoT"),
        ModuleInstall('python-mpd2', 'pip', usage="IoT"),
        ModuleInstall('hikvision', 'pip', usage="IoT"),
        ModuleInstall('colorlog', 'pip', usage="IoT"),
        ModuleInstall('jsonrpc-requests', 'pip', usage="IoT"),
        ModuleInstall('cookies', 'pip', usage="IoT"),
        ModuleInstall('mock', 'pip'),
        ModuleInstall('pbr', 'pip'),
        ModuleInstall('responses', 'pip'),
        ModuleInstall('python-forecastio', 'pip', usage="IoT"),
        ModuleInstall('pyserial', 'pip', mname="serial", usage="IoT"),
        ModuleInstall('PyMata', 'pip', usage="IoT"),
        ModuleInstall('pyRFXtrx', 'github', 'Danielhiversen'),
        ModuleInstall('pymysensors', 'github', 'theolind'),
        ModuleInstall('pynetgear', 'pip', usage="IoT"),
        ModuleInstall('netdisco', 'pip', usage="IoT"),
        ModuleInstall('pywemo', 'pip', usage="IoT"),
        ModuleInstall('python-wink', 'github', 'balloob'),
        ModuleInstall('slacker', 'pip'),
        ModuleInstall('temper-python', 'github', 'rkabadi'),
        ModuleInstall('pyedimax', 'github', 'rkabadi'),

        # Uncomment for Raspberry Pi
        # ModuleInstall('RPi.GPIO', 'pip'),
        # uncomment on a Raspberry Pi / Beaglebone
        # ModuleInstall('Adafruit_Python_DHT', 'github', 'mala-zaba', purpose="Adafruit temperature/humidity sensor", usage="IoT"),

        ModuleInstall('paho-mqtt', 'pip', usage="IoT"),
        ModuleInstall('pymodbus', 'github', 'bashwork', usage='IoT'),
        ModuleInstall('python-verisure', 'github',
                      'persandstrom', usage='IoT'),

    ]
    return [_ for _ in mod if _ is not None]
