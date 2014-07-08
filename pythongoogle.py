import urllib2, re

#proof of concept

#set up search user agent
baseurl = "http://www.google.com/search?q=";
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(opener)
result = urllib2.urlopen(baseurl)
html = result.read()
#parse result html

linklist = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)#RE credit to stackexchange user JohnJohnGa
