from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

URL="https://www.bolsasymercados.es/esp/Home"

def get_html_code(url):
    try:
        html=urlopen(url)
    except HTTPError:
        print("Ha ocurrido un error HTTP")
    except URLError:
        print("Ha ocurrido un error URL")
    else:
        html_code = html.read()
        html_code = BeautifulSoup(html_code, 'html.parser')
    return html_code

def scrape(_url):
    html_code = get_html_code(_url)
    items = html_code.find_all("div",{"class":"precio"})
    for item in items:
        print("El índice actual del IBEX35 es:", item.text)

if __name__=="__main__":
    scrape(URL)