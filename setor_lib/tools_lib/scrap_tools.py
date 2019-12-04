import urllib.request
import bs4 as bs

def useragent_setting(target_data):
    req = urllib.request.Request(
        target_data,
        data=None,
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }
    )
    return req

def request(page_url):
    req_obj = urllib.request.urlopen(useragent_setting(page_url))
    return req_obj

def build_soup(page_url):
    source_page = request(page_url)
    if(source_page.getcode()!=200):
        print("[error] :request server not responding , please try again later.")
        exit()
    soup_source_page = bs.BeautifulSoup(source_page,'lxml')
    return soup_source_page