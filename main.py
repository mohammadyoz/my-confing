import requests
import re
import base64
from datetime import datetime
import time

def get_configs():
    channels = [
        'Farah_VPN', 'letsproxys', 'shankamil', 'AzadNet', 'MoonsterVpn',
        'ProxGp', 'ConfingV2RaayNG', 'Pruuxi', 'sina_tec', 'v2rayng_fars',
        'v2rayipm', 'SOSkeyNET', 'vpn_proxy_trading', 'FreakConfig', 'V2HUBIR',
        'Confing_m1SHAP', 'NPV_78', 'EmKavpn', 'filtershekanfilm', 'mtmvpn', 
        'hddify', 'filembad', 'prrofile_purple'
    ]
    
    all_links = []
    current_time = datetime.now().strftime("%H:%M")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    for ch in channels:
        try:
            # لود کردن صفحه اصلی کانال با پارامتر زمان برای دور زدن کش
            res = requests.get(f"https://t.me/s/{ch}?t={int(time.time())}", headers=headers, timeout=15)
            if res.status_code == 200:
                # این ریجکس جدید حتی اگه ته لینک کاراکتر فارسی یا فاصله باشه، دقیق عمل می‌کنه
                found = re.findall(r'(?:vless|vmess|trojan|ss|tuic|hysteria2)://[^\s<"\'#]+', res.text)
                if found:
                    # فقط ۱۰ تای آخر (تازه‌ترین‌ها) رو برمی‌داریم که سالم باشن
                    for link in found[-10:]: 
                        base_link = link.split('#')[0]
                        all_links.append(f"{base_link}#{ch}-{current_time}")
            time.sleep(0.5) 
        except:
            continue
    
    unique_links = list(dict.fromkeys(all_links))
    result_text = "\n".join(unique_links)
    b64_output = base64.b64encode(result_text.encode('utf-8')).decode('utf-8')
    
    with open("sub_link.txt", "w") as f:
        f.write(b64_output)

if __name__ == "__main__":
    get_configs()
