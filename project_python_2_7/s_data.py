from bs4 import BeautifulSoup


def search_for(the_page):
    soup = BeautifulSoup(the_page, "html.parser")
    a = soup.find_all('table', style="width:29%")
    n = len(a)
    total_data = [''] * n
    for i in range(0, n):
        total_data[i] = a[i].string

    return(total_data)
