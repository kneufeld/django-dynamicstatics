# Django Dynamic Statics

This little app allows you to dynamically change Django's `MEDIA_URL` and
`STATIC_URL` on a per request basis based on the clients `REMOTE_ADDR`.

The use case this was written for was that the local web server has all
the large media assets but the remote server is the public facing web
server. If you were at the local location it sure would be nice to get
the assets directly instead of proxying via the remote web server.

## Prerequisites

`django-dynamicstatics` depends on
[iptools](https://github.com/bd808/python-iptools) and
[django-ipware](https://github.com/un33k/django-ipware) which should get
installed automatically when you install via `pip` or `easy_install`.

## Setup

You'll have to edit your `settings.py` file.

### Original

```python
MEDIA_URL = '/media/'
...
STATIC_URL = '/static/'
```

### Modified

Add two new variables. The format of `MEDIA_URLS` and `STATIC_URLS` is
a `dict` with a string or a list of ip addresses as the key and a url
string as the value. Use `iptools` to effortlessly make a range of ip
addresses.

If the clients remote address doesn't match any key then `MEDIA_URL` or
`STATIC_URL` is used as appropriate.

```python
import iptools

MEDIA_URLS = {
    '127.0.0.1': 'http://localhost/media/',
    #iptools.IpRange(''): '',
    iptools.IpRangeList('192.168.1.0/24','2.3.4.5'): "https://www2.local/media/",
}
...
STATIC_URLS = {
    '127.0.0.1': 'http://localhost/static/',
    #iptools.IpRange(''): '',
    iptools.IpRangeList('192.168.1.0/24','2.3.4.5'): "https://www2.local/static/",
}

# add dynamicstatics to INSTALLED_APPS
INSTALLED_APPS = [
...
  dynamicstatics,
]
```

## Tests

Forthcoming.

