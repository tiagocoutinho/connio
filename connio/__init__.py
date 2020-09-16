__version__ = "0.0.0"


import urllib.parse


SERIAL_SCHEMES = {'serial', 'tcp-serial', 'rfc2217'}
SOCKET_SCHEMES = {'tcp'}


def connection_for_url(url, *args, **kwargs):
    url_result = urllib.parse.urlparse(url)
    scheme = url_result.scheme
    if scheme in SERIAL_SCHEMES:
        from serialio import serial_for_url
        return serial_for_url(url, *args, **kwargs)
    elif scheme in SOCKET_SCHEMES:
        from sockio import socket_for_url
        return socket_for_url(url, *args, **kwargs)
