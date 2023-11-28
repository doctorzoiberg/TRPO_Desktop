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


def get_column_name_list(string):
    column_name_list = list()

    column_name_list.append('№')
    for column_name in string.split('\n')[1:(-1)]:
        column_name_list.append(str(column_name.strip().removesuffix('\ue603')))

    return column_name_list


def get_table_row_list(number, string):
    table_row_list = list()
    string_split = string.split('\n')

    table_row_list.append(str(number))

    if number < 10:
        name = string_split[2][1:]
    else:
        name = string_split[2][2:]
    table_row_list.append(str(name.strip()))

    for column_value in string_split[3:(-2)]:
        table_row_list.append(str(column_value.strip()))

    return table_row_list


def get_data(headers, platform):
    data = list()

    data.append([platform])
    data.append(get_column_name_list(headers[1]))
    for i in range(2, len(headers)):
        data.append(get_table_row_list((i - 1), headers[i]))

    return data
