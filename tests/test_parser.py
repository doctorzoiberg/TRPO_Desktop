import pytest
import requests
from app.Parser import parser


@pytest.mark.parametrize('url', [('https://www.antutu.com/en/ranking/rank1.htm'),
                                 ('https://www.antutu.com/en/ranking/ios1.htm'),
                                 ('https://www.antutu.com/en/ranking/ai1.htm')])
def test_access_url(url):
    page = requests.get(url)
    assert page.status_code == 200


@pytest.mark.parametrize('url', [('https://www.antutu.com/en/ranking/rank1.htm'),
                                 ('https://www.antutu.com/en/ranking/ios1.htm'),
                                 ('https://www.antutu.com/en/ranking/ai1.htm')])
def test_parse_text_data(url):
    headers = parser.parse_text(url)
    assert type(headers) == list
    assert len(headers) != 0
