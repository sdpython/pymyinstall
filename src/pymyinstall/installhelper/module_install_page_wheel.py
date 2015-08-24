"""
@file
@brief Functions get_page_wheel
"""
import sys

if sys.version_info[0] == 2:
    import urllib2 as urllib_request
else:
    import urllib.request as urllib_request

from .install_memoize import install_memoize


@install_memoize
def get_page_wheel(page):
    """
    get the page

    @param      page        location
    @return                 page content
    """
    req = urllib_request.Request(
        page,
        headers={
            'User-agent': 'Mozilla/5.0'})
    u = urllib_request.urlopen(req)
    text = u.read()
    u.close()
    text = text.decode("utf8")
    text = text.replace("&quot;", "'")
    text = text.replace("&#8209;", "-")
    return text
