import requests
import random
from hashlib import md5

# Set your own appid/appkey.
appid = 'xxxxxx'
appkey = 'xxxxxx'


def get_trans(query, from_lang='en', to_lang='zh'):
    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # print(result)
    return result['trans_result'][0]['dst']


def all_trans(query):
    res_end = []
    res_begin = []
    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    lang_list = ['en', 'jp', 'fra', 'kor', 'ru']
    for temp in lang_list:
        res_begin.append(get_trans(query, 'zh', temp))

    for temp in zip(res_begin, lang_list):
        res_end.append(get_trans(temp[0], temp[1], 'zh'))
    res_end.append(query)
    return res_end


if __name__ == "__main__":
    res = all_trans('童话说雨后终会出现彩虹，却不曾说过它也会转瞬成空')
