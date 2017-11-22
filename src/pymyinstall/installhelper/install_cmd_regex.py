"""
@file
@brief Regular expressions to extract version numbers
"""


regex_wheel_version = "[-]([0-9]+[.][abc0-9]+([.][0-9]{1,2})?([.][0-9abdevcr]+)?)([+][a-z]+)?" + \
                      "([+]cuda[0-9]{2,5})?([+]cl[0-9]{2,5})?([+]git[0-9]{1})?([+]sdl[0-9])?([+]r33)?" + \
                      "([+]contrib_opencl)?([+]numpy[0-9]{1,2})?([+.]post[0-9]{1,2})?([.][0-9])?[-]"
regex_wheel_version2 = "[-]([0-9]+)[-]cp"
regex_wheel_version3 = "[-](([0-9]+)[.]([0-9]+)[.]([0-9]+)(((rc)|(a)|(b))[0-9]+)?)[.]((zip)|(tar)|(gz)|(whl))"
regex_wheel_version4 = "[-](([0-9]+)[.]([0-9]+)(((rc[0-9]?)|(a)|(b))[0-9]+)?[.])((zip)|(tar)|(gz)|(whl))"
regex_wheel_version5 = "[-]([0-9]+[.][0-9]+([.][0-9][.]?)?([0-9abcrdev]+))[-]"
regex_wheel_version6 = "[-]([0-9]+)[.]([0-9]+)[.+]([0-9]{8})[-]"

regex_wheel_versions = [
    regex_wheel_version,
    regex_wheel_version2,
    regex_wheel_version3,
    regex_wheel_version4,
    regex_wheel_version5,
    regex_wheel_version6
]


if __name__ == "__main__":
    import re
    d = locals().copy()
    for k, v in d.items():
        if "regex" in k and isinstance(v, str):
            try:
                reg = re.compile(v)
            except Exception as e:
                raise Exception("issue with {}:\n{}".format(k, v))
