import requests
import re
import base64

channels = [
    'prrofile_purple', 'filembad', 'Pruuxi', 'V2HUBIR', 'letsproxys', 
    'proxy_kafee', 'Farah_VPN', 'shankamil', 'AzadNet', 'MoonsterVpn', 
    'ProxGp', 'ConfingV2RaayNG', 'sina_tec', 'v2rayng_fars', 'v2rayipm', 
    'SOSkeyNET', 'vpn_proxy_trading', 'FreakConfig', 'Confing_m1SHAP', 
    'NPV_78', 'EmKavpn', 'filtershekanfilm', 'mtmvpn', 'hddify', 'proxiteIegram'
]

def get_configs():
    all_configs = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    for ch in channels:
        try:
            url = f"https://t.me/s/{ch}"
            res = requests.get(url, headers=headers, timeout=15)
            matches = re.findall(r'(vless|vmess|trojan|ss|tuic|hysteria2)://[^\s<"\']+', res.text)
            if matches: all_configs.extend(matches[-5:])
        except: continue
    
    unique_configs = list(dict.fromkeys(all_configs))
    content = "\n".join(unique_configs)
    b64_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    with open("sub_link.txt", "w") as f: f.write(b64_content)

if __name__ == "__main__":
    get_configs()
