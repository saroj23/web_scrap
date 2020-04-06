# pip install requests
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup


def get_HTML_text(url):
    response = requests.get(url)
    response_page = response.text
    response_status = response.status_code

    if response_status == 200:
        return response_page
    elif response_status == 403:
        raise Exception("try after minute again")
    else:
        raise Exception("oops something went wrong")


# get html txt of website
response_page = get_HTML_text(
    "https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht")
# parse html
response_page_soup = BeautifulSoup(response_page, "html.parser")
# select table
container = response_page_soup.find(
    "table", {"class": "chart full-width"})
# select table kok tbody ko tr
trs = container.find("tbody").findAll("tr")

# file open
try:
    f = open("movies.csv", "w")
    f.write("name, image \n")  # headers

    for tr in trs:
        title = tr.find("td", {"class", "titleColumn"}).a.text
        image = tr.find("td", {"class", "posterColumn"}).a.img["src"]
        f.write(title+",\""+image+"\"\n")
except Exception as e:
    print("oops", e)
else:
    f.close()

