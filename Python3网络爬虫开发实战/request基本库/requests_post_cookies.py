#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests

headers = {
    'Cookie':'_uab_collina=155488580599644713292334; UM_distinctid=16a066a8ad221b-05fdb9d9997f9c-39395704-1fa400-16a066a8ad37; __auc=d1f60f4b16a066a8b6ce1e17112; __gads=ID=e40d1d92cb2f61c8:T=1554885807:S=ALNI_MZEV49Jj0PsahSk2LRIGfT34M5HBw; sid=BU9dKsPBgaBQN6qpt4jfroV1irO.unhxHpXOgGlZfNMq8GvwjzznhhxWqXfpq6Mb%2F2yzI4o; uid=14519546; _f=iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAABSklEQVRYR%2B1XOxLCQAiFC9lZ2Xgjr5LcyMbKzoPkCjis2RVx2W%2FiOJqMhSQQeLx9MEEgIpgvQgR8muBs4F%2FbRQDUEy%2BzDtMQ6oxVg38FhDvLXfDdtWzpw%2F%2B9n%2B%2BgZEc%2Bi71X56hmRNMmk%2BhC2NbHR9rWs1yMbhrnqQZiaSSVXHc%2FBz5ocmY6Vrj0%2BRgQi4Vc52OArZjVGSkt1rPWehyLgfCoDaIkcqNXi1SL1x%2BJ0vuW2OPj9DH2%2FbvHaUjugJfxG%2FVEgahtnSwSVcyImc0AQudrWFB43KO2U9XX%2BAbRi3zj7vL2%2Bi5GuCAGIZNJOwamNUYWf7odQIPZgGgWdKeto%2FWVjLipMh%2BvDYjSmaWrVTXyU4xIMCULI6URP5b15OP7FiM8wR6LWXxYtS7EUn3EdoIe364oMdJze2RRICVM9Pqsttl7C6uNzwG5A0REryCcRnCcAAAAAElFTkSuQmCC%2CWin32.1920.1080.24; Hm_lvt_d4a0e7c3cd16eb58a65472f40e7ee543=1556436109,1556529175,1556529286,1557238109; __asc=2ab41c1b16a929fd52e91566e73; CNZZDATA1256903590=105224302-1554885356-%7C1557233160; _cnzz_CV1256903590=is-logon%7Clogged-in%7C1557238120809%26urlname%7Cwkwrpbspbv%7C1557238120809; Hm_lpvt_d4a0e7c3cd16eb58a65472f40e7ee543=1557238120',
    'Host':'huaban.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

r = requests.get('https://huaban.com',headers=headers)
print(r.text)