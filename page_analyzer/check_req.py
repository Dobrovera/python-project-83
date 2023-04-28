import page_analyzer.db
import requests
from bs4 import BeautifulSoup


def check_request(curs, id):
    name_url = page_analyzer.db.get_info_by_id(curs, id)['name']
    url_info = {}
    try:
        r = requests.get(name_url)
        url_info['status_code'] = r.status_code
        soup = BeautifulSoup(r.text, 'html.parser')
        url_info['title'] = str(soup.find_all('title'))[8:-9]
        url_info['h1'] = str(soup.find_all('h1'))[5:-6]
        url_info['description'] = str(soup.find_all
                                      ('meta',
                                       attrs={'name': 'description'}))[16:-23]
        return url_info
    except requests.ConnectionError or requests.exceptions.RequestException:
        return False