"""
@file
@brief Constants used in many places
"""
import sys

default_user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' if sys.platform.startswith(
    "win") else 'Mozilla/5.0'
