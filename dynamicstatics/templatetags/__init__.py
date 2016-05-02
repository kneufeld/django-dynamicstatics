from ipware.ip import get_ip

def __lookup(request, url_map, default_url ):
    """
    based on the current request, pick the appropriate static url
    """
    remote_ip = get_ip(request)

    for ips, url in url_map.iteritems():
        if hasattr(ips, '__iter__'):
            if any( map( lambda ip: remote_ip in ip, ips ) ):
                return url
        else:
            if remote_ip == ips:
                return url

    try:
        return url_map['default']
    except KeyError:
        pass

    return default_url
