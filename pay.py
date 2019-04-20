import requests
from settings import settings
import json
def get_xcsrf():
    r = requests.post('https://www.roblox.com/favorite/toggle').headers
    if not r['X-CSRF-TOKEN']:
        print('Failed to get xcsrf token.')
        exit()
    else:
        return r['X-CSRF-TOKEN']

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:66.0) Gecko/20100101 Firefox/66.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Referer': 'https://www.roblox.com/my/money.aspx',
'Content-Type': 'application/json; charset=utf-8',
'X-CSRF-TOKEN': get_xcsrf(),
'DNT': '1',
'Cache-Control': 'max-age=0',
}

cookies = {
    '.ROBLOSECURITY': settings['ROBLOSECURITY']
}

url = f'https://www.roblox.com/groups/settings' + str(settings['GroupId']) + '/one-time-payout/false'

for payouts in settings['users']:
    robux = str(settings['users'][payouts])
    print(f'Paying {payouts} {robux} Robux')
    data = {
        'percentages': {payouts: robux}
    }
    json_data = json.dumps(data)
    r = requests.post(url, headers=headers, data=data, cookies=cookies)

    if r.status_code is 200:
        print('OK 200')
    elif r.status_code is 403:
        print('xcsrf token error: Is roblox down?')
    else:
        print('Error: Not enough robux')