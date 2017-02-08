"""
"""

from pycoin.version import version

try:
    from urllib2 import urlopen, Request
except ImportError:
    from urllib.request import urlopen, Request


PYCOIN_AGENT = 'pycoin-%s' % version


def url_open(url):
    req = Request(url)
    req.add_header('User-agent', PYCOIN_AGENT)
    return urlopen(req)
