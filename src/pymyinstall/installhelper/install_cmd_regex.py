"""
@file
@brief Regular expressions to extract version numbers
"""


regex_wheel_version = "[-]([0-9]+[.][abc0-9]+([.][0-9])?([.][0-9abdevcr]+)?)([+][a-z]+)?" + \
                      "([+]cuda[0-9]{2,5})?([+]sdl[0-9])?([+]r33)?([+]contrib_opencl)?([+]numpy[0-9]{1,2})?([+.]post[0-9]{1,2})?([.][0-9])?[-]"
regex_wheel_version2 = "[-]([0-9]+)[-]cp"
