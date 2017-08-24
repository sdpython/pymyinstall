#-*- coding: utf-8 -*-
"""
@file
@brief Functions get_page_wheel
"""

import sys
from .install_memoize import install_memoize
from .internet_settings import default_user_agent

if sys.version_info[0] == 2:
    import urllib2 as urllib_request
    from codecs import open
    from HTMLParser import HTMLParser
else:
    import urllib.request as urllib_request
    from html.parser import HTMLParser


class InternalJsException(Exception):
    """
    Raises when a javascript url cannot be decrypted.
    """
    pass


@install_memoize
def get_page_wheel(page, sele=False):
    """
    get the page

    @param      page        location
    @param      sele        use selenium or not or False to try
    @return                 page content
    """
    if sele is None or sele:
        try:
            import selenium
            sele = True
        except ImportError:
            sele = False
    else:
        sele = False

    if sele:
        import selenium.webdriver
        browser = selenium.webdriver.Firefox()
        browser.get(page)
        text = browser.page_source
        browser.close()
        regular = len(text) < 100000
    else:
        regular = True

    if regular:
        req = urllib_request.Request(
            page,
            headers={
                'User-agent': default_user_agent})
        try:
            u = urllib_request.urlopen(req)
        except Exception as e:
            raise Exception("unable to get '{0}'".format(page)) from e
        text = u.read()
        u.close()
        text = text.decode("utf8")

    return _clean_page_wheel(text)


def _clean_page_wheel(text):
    """
    remove unexpected characters

    @param      text        string
    @return                 string
    """
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
    return _clean_page_wheel(text)


def _cg_dl1(ml, mi):
    ot = ""
    for j in range(0, len(mi)):
        ot += chr(ml[ord(mi[j]) - 48])
    return ot


def _cg_dl(ml, mi, fLOG=None):
    """
    compressed::

        if (top.location!=location) top.location.href=location.href;
        function dc(ml,mi){var ot="";for(var j=0;j<mi.length;j++)ot+=String.fromCharCode(ml[mi.charCodeAt(j)-48]);
        document.write(ot);}function dl1(ml,mi){var ot="";for(var j=0;j<mi.length;j++)ot+=String.fromCharCode(ml[mi.charCodeAt(j)-48]);
        location.href=ot;}function dl(ml,mi){mi=mi.replace('&lt;','<');mi=mi.replace('&#62;','>');mi=mi.replace('&#38;','&');
        setTimeout(function(){dl1(ml,mi)},1500);}

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


class HTMLParser4Links(HTMLParser):
    """
    extreact all links ni HTML page
    """

    def __init__(self):
        """
        constructor
        """
        if sys.version_info[0] == 2:
            HTMLParser.__init__(self)
        else:
            HTMLParser.__init__(self, convert_charrefs=True)
        self.links = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        """
        enters a tag
        """
        if tag == "a":
            self.current = ""
            self.attrs = attrs

    def handle_endtag(self, tag):
        """
        ends of a tag
        """
        if tag == "a":
            if self.current is not None and len(self.current) > 0:
                app = (self.current, self.attrs)
                self.links.append(app)
            self.current = None

    def handle_data(self, data):
        """
        stores data if a link
        """
        if self.current is not None:
            self.current += data


def extract_all_links(text):
    """
    parses HTML to extract all links

    @param      text        HTML page
    @return                 list of links
    """
    parser = HTMLParser4Links()
    parser.feed(text)
    return parser.links


def enumerate_links_module(name, alls, version, plat):
    """
    selects the links for a specific module

    @param      name        module name
    @param      alls        all links from @see fn extract_all_links
    @param      version     python version
    @param      plat        platform
    """
    version = "%d%d" % version[:2]
    lname = name.lower()
    lname_ = lname.replace("-", "_") + "-"
    lname += "-"
    for a in alls:
        n = a[0]
        ln = n.lower()
        if (ln.startswith(lname) or ln.startswith(lname_)) and plat in ln:
            vers = ("cp" + version, "py" + version)
            good = False
            for v in vers:
                if v in ln:
                    good = True
            if not good:
                continue
        else:
            continue

        js = None
        for at, val in a[1]:
            if at == "onclick":
                js = val.lstrip()

        if js:
            js0 = js
            suf = '"javascript:dl("'
            bs = ["javascript:", "javascript :"]
            res = None
            for b in bs:
                if js.startswith(b):
                    js = js[len(b):]
                    if js.endswith(suf):
                        js = js[:-len(suf) - 2]
                    if "javascript:" in js:
                        # Addition: 207-08-24
                        js = js[:js.index('"javascript:')]
                    js = js.strip('" \t ;')
                    dl = _cg_dl
                    if dl is not None:
                        try:
                            res = eval(js)
                        except SyntaxError as e:
                            raise SyntaxError(
                                "Unable to evaluate '{0}'\njs0='{1}'.".format(js, js0))
                        break
            if res is None:
                raise InternalJsException(
                    "Unable to decode js '{0}'".format(js))
            yield n, js, res
