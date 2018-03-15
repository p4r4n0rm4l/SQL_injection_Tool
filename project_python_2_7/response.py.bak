## import urllib2
import urllib
def site_alive(site):
    
    if "http://" not in site:
        site="http://"+site
    if "127.0.0.1" not in site:
        if "www." not in site:
            site = site.replace("http://","http://www.")
        ## req = urllib2.Request(site)
        
        try:
            ## response = urllib2.urlopen(req)
            urllib.urlopen(site).getcode()
        except:
            print "No response from server"
            print "Program will exit"
            exit()
    return (site)
