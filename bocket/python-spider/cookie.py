import urllib2;
import cookielib;

### Cookie is for user identity, session tracing.
### usually encrypted
### if websites allow spider with login, then save cookies and send req with saving cookies.

# save cookies to a file
filename = 'cookies.txt';
# a CookieJar instance to store cookie
cookie = cookielib.MozillaCookieJar(filename);          # MozillaCookieJar defers from CookieJar!
# a cookie handler
handler = urllib2.HTTPCookieProcessor(cookie);
# build an opener by handler
opener = urllib2.build_opener(handler);                 # urlopen is a specific opener!
# then send request as usall
response = opener.open('http://www.baidu.com');
# write cookie to file
cookie.save(ignore_discard=True, ignore_expires=True);



### load cookies from a file
#cookie = cookie.MozillaCookieJar();
#cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True);
#req = urllib2.Request('http://www.baidu.com');
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie));
#resopnse = opener.open(req);
#print response.read();
