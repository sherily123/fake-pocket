import urllib;
import urllib2;
import cookielib;

### login school system and save the cookie
filename = 'school-grade-cookie.txt';
cookie = cookielib.MozillaCookieJar(filename);
handler = urllib2.HTTPCookieProcessor(cookie);
opener = urllib2.build_opener(handler);
postData = urllib.urlencode({
    'username': '12330395',
    'password': 'sherry1234',
    'captcha': '1184'               ### how to deal with captcha code???
});
try:
    res = opener.open('https://wjw.sysu.edu.cn', postData);
    cookie.save(ignore_discard=True, ignore_expires=True);
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print 'Exception code: ';
        print e.code;
    if hasattr(e, 'reason'):
        print 'Exception reason: ';
        print e.reason;
else:
    print 'ok';
