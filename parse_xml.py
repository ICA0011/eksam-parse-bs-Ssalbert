from bs4 import BeautifulSoup
import requests
import lxml


def parse_xml():
    url = "http://upload.itcollege.ee/~aleksei/test.xml"
    xml_content = requests.get(url).content
    soup = BeautifulSoup(xml_content, 'xml')

    data_row = soup.find("data")
    data_row = data_row.get_text()
    result = data_row.strip()

    return result
