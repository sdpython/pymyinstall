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
    try:
        import selenium
        sele = True
    except ImportError:
        sele = False

    if sele:
        from selenium import webdriver
        browser = webdriver.Firefox()
        browser.get(page)
        text = browser.page_source
        browser.close()
    else:
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
    text = text.replace("&#46;", ".")
    text = text.replace(" &middot; ", "-")
    text = text.replace("&ndash;", "-")
    return text


def save_page_wheel(filename, content):
    """
    cache a HTML page

    @param      filename        filename
    @param      content         content
    @return                     filename
    """
    with open(filename, "w", encoding="utf8") as f:
        f.write(content)


def read_page_wheel(filename):
    """
    read a cached HTML page

    @param      filename        filename
    @return                     filename
    """
    with open(filename, "r", encoding="utf8") as f:
        text = f.read()
    text = text.replace("&quot;", "'")
    text = text.replace("&#8209;", "-")
    text = text.replace("&#46;", ".")
    text = text.replace(" &middot; ", "-")
    text = text.replace("&ndash;", "-")
    return text


def _cg_dl1(ml, mi):
    ot = ""
    for j in range(0, len(mi)):
        ot += chr(ml[ord(mi[j]) - 48])
    return ot


def _cg_dl(ml, mi, fLOG=None):
    """
    compressed::

        if (top.location!=location) top.location.href=location.href;function dc(ml,mi){var ot="";for(var j=0;j<mi.length;j++)ot+=String.fromCharCode(ml[mi.charCodeAt(j)-48]);document.write(ot);}function dl1(ml,mi){var ot="";for(var j=0;j<mi.length;j++)ot+=String.fromCharCode(ml[mi.charCodeAt(j)-48]);location.href=ot;}function dl(ml,mi){mi=mi.replace('&lt;','<');mi=mi.replace('&#62;','>');mi=mi.replace('&#38;','&');setTimeout(function(){dl1(ml,mi)},1500);}

    source::

        <script type="text/javascript">
        // <![CDATA[
        if (top.location!=location)
            top.location.href=location.href;
        function dc(ml,mi)
        {
            var ot="";
            for(var j=0;j<mi.length;j++)
                ot+=String.fromCharCode(ml[mi.charCodeAt(j)-48]);
            document.write(ot);
        }
        function dl1(ml,mi)
        {
            var ot="";
            for(var j=0;j<mi.length;j++)
                ot+=String.fromCharCode(ml[mi.charCodeAt(j)-48]);
                location.href=ot;
        }
        function dl(ml,mi)
        {
            mi=mi.replace('&lt;','<');
            mi=mi.replace('&#62;','>');
            mi=mi.replace('&#38;','&');
            setTimeout(function(){dl1(ml,mi)},1500);
        }
        // ]]>
        </script>
    """
    if fLOG:
        fLOG("decode", ml)
        fLOG("decode", mi)
    mi = mi.replace('&lt;', '<')
    mi = mi.replace('&#62;', '>')
    mi = mi.replace('&gt;', '>')
    mi = mi.replace('&#38;', '&')
    return _cg_dl1(ml, mi)
