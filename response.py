import urllib.request
import urllib.parse
import urllib.error


def site_alive(site):
    
    if "http://" not in site:
        site = "http://"+site
    if "127.0.0.1" not in site:
        if "www." not in site:
            site = site.replace("http://", "http://www.")
        
        try:
            urllib.request.urlopen(site).getcode()
        except:
            print("No response from server")
            print("Program will exit")
            exit()
    return site
