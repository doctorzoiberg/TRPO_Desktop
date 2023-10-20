import requests
from bs4 import BeautifulSoup


def parse_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.find('div', 'm_l fl')
    headers = []
    for i in table.find_all('ul'):
        headers.append(i.text)
    return headers


def get_phones_data(headers):
    table = dict()
    for i in range(2, len(headers)):
        headers_split = headers[i].split('\n')
        name = headers_split[2]
        if i >= 2 and i <= 10:
            id = name[0]
            name = name[1:]
        else:
            id = name[:2]
            name = name[2:]
        cpu = headers_split[3]
        gpu = headers_split[4]
        mem = headers_split[5]
        ux = headers_split[6]
        t_score = headers_split[7]
        table[id] = [name, cpu, gpu, mem, ux, t_score]
    return table


def get_ai_data(headers):
    table = dict()
    for i in range(2, len(headers)):
        headers_split = headers[i].split('\n')
        name = headers_split[2]
        if i >= 2 and i <= 10:
            id = name[0]
            name = name[1:]
        else:
            id = name[:2]
            name = name[2:]
        image_classification = headers_split[3]
        object_direction = headers_split[4]
        t_score = headers_split[5]
        table[id] = [name, image_classification, object_direction, t_score]
    return table
