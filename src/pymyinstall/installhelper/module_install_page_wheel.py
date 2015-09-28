"""
@file
@brief Functions get_page_wheel
"""
from .install_memoize import install_memoize
from .internet_settings import default_user_agent
import sys

if sys.version_info[0] == 2:
    import urllib2 as urllib_request
else:
    import urllib.request as urllib_request


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
            'User-agent': default_user_agent})
    u = urllib_request.urlopen(req)
    text = u.read()
    u.close()
    text = text.decode("utf8")
    text = text.replace("&quot;", "'")
    text = text.replace("&#8209;", "-")
    return text
