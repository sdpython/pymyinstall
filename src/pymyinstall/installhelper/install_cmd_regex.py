"""
@file
@brief Regular expressions to extract version numbers
"""


regex_wheel_version = "[-]([0-9]+[.][abc0-9]+([.][0-9])?([.][0-9abdevcr]+)?)([+][a-z]+)?" + \
                      "([+]cuda[0-9]{2,5})?([+]git[0-9]{1})?([+]sdl[0-9])?([+]r33)?([+]contrib_opencl)?([+]numpy[0-9]{1,2})?([+.]post[0-9]{1,2})?([.][0-9])?[-]"
regex_wheel_version2 = "[-]([0-9]+)[-]cp"
regex_wheel_version3 = "[-](([0-9]+)[.]([0-9]+)[.]([0-9]+)(((rc)|(a)|(b))[0-9]+)?)[.]((zip)|(tar)|(gz)|(whl))"
regex_wheel_version4 = "[-](([0-9]+)[.]([0-9]+)(((rc[0-9]?)|(a)|(b))[0-9]+)?[.])((zip)|(tar)|(gz)|(whl))"
regex_wheel_version5 = "[-]([0-9]+[.][0-9]+([.][0-9])?([0-9abcr]+))[-]"


if __name__ == "__main__":
    import re
    d = locals().copy()
    for k, v in d.items():
        if "regex" in k:
            try:
                reg = re.compile(v)
            except Exception as e:
                raise Exception("issue with {}:\n{}".format(k, v))
