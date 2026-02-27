import requests
import re
import base64

def get_configs():
    channels = [
        'prrofile_purple', 'filembad', 'Pruuxi', 'V2HUBIR', 'letsproxys', 
        'proxy_kafee', 'Farah_VPN', 'shankamil', 'AzadNet', 'MoonsterVpn', 
        'ProxGp', 'ConfingV2RaayNG', 'sina_tec', 'v2rayng_fars', 'v2rayipm', 
        'SOSkeyNET', 'vpn_proxy_trading', 'FreakConfig', 'Confing_m1SHAP', 
        'NPV_78', 'EmKavpn', 'filtershekanfilm', 'mtmvpn', 'hddify', 'proxiteIegram'
    ]
    
    all_links = []
    for ch in channels:
        try:
            res = requests.get(f"https://t.me/s/{ch}", timeout=10)
            if res.status_code == 200:
                # پیدا کردن تمام پروتکل‌ها
                found = re.findall(r'(?:vless|vmess|trojan|ss|tuic|hysteria2)://[^\s<"\'#]+', res.text)
                if found:
                    all_links.extend(found[-5:]) # ۵ تای آخر هر کانال
        except:
            continue
    
    # حذف تکراری‌ها
    unique_links = list(dict.fromkeys(all_links))
    result_text = "\n".join(unique_links)
    
    # تبدیل به Base64
    b64_output = base64.b64encode(result_text.encode('utf-8')).decode('utf-8')
    
    with open("sub_link.txt", "w") as f:
        f.write(b64_output)

if __name__ == "__main__":
    get_configs()
