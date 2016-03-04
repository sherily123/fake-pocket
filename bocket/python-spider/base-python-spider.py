import urllib2;

### use proxy to avoid being forbidden
#   enable_proxy = True;
#   proxyHandler = urllib2.ProxyHandler({'http':'http://some-proxy.com:8080'});
#   nullProxyHandler = urllib2.ProxyHandler({});
#   if enable_proxy:
#       opener = urllib2.build_opener(proxyHandler);
#   else:
#       opener = urllib2.build_opener(nullProxyHandler);

### set @param headers to fake self as a real browser

try:
    req = urllib2.Request('http://blog.csdn.net/cqcre');
    response = urllib2.urlopen(req, timeout=5);
    print response.read();
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code;
    if hasattr(e, 'reason'):
        print e.reason;
else:
    print 'OK';
