import requests

def jd_signin(cookie: str):
    headers = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'https://home.m.jd.com/myJd/newhome.action',
        'Accept': 'application/json, text/plain, */*',
    }
    url = 'https://api.m.jd.com/client.action?functionId=signBeanIndex'
    params = {
        'client': 'wh5',
        'clientVersion': '1.0.0',
        'body': '{}',
    }
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        data = resp.json()
        if data.get('code') == '0':
            print("签到成功，获得京豆:", data.get('data', {}).get('beanNum', 0))
        else:
            print("签到失败，信息：", data.get('msg', '未知错误'))
    except Exception as e:
        print("签到请求异常：", e)

if __name__ == '__main__':
    import os
    ck = os.getenv('JD_COOKIE')
    if not ck:
        print("请在环境变量 JD_COOKIE 中设置京东 Cookie")
    else:
        jd_signin(ck)
