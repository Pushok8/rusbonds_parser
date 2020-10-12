import json
from typing import NewType

from bs4 import BeautifulSoup
from requests import Session
import requests

# ANNOTATIONS
url_str = NewType('url_str', str)
# CONSTANTS
USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)'
HOST: url_str = 'https://www.rusbonds.ru/'
with open('login_data.json') as login_data_json:
    DATA_FOR_LOGGING: dict[str: str] = json.load(open('login_data.json'))

registered_user: Session = requests.Session()
registered_user.headers['User-Agent'] = USER_AGENT

r = registered_user.post(HOST, data=DATA_FOR_LOGGING)