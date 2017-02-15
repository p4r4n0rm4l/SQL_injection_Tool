import urllib2
import re
import httplib
def get_the_page(site,opt):
    req = urllib2.Request(site)
    try:
        response = urllib2.urlopen(req)
    except:
        print "Invalid url"
        print "Program will exit"
        exit()
    else:
        the_page=response.read()
##        if opt=='2':
##            the_page=re.sub("<.*?>","",the_page)
        return (the_page)
