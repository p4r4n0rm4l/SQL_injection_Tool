from urllib.request import urlopen


def get_the_page(site, opt):
    with urlopen(site) as f:
        the_page = f.read().decode('utf-8')
        return the_page
