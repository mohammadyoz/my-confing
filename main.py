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
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    for ch in channels:
        try:
            url = f"https://t.me/s/{ch}"
            res = requests.get(url, headers=headers, timeout=15)
            # پیدا کردن لینک‌ها
            matches = re.findall(r'(vless|vmess|trojan|ss|tuic|hysteria2)://[^\s<"\'#]+', res.text)
            if matches:
                # فقط پیام‌های خیلی جدید
                all_configs.extend(matches[-5:])
        except:
            continue
    
    # حذف تکراری‌ها و فضاهای خالی
    unique_configs = list(dict.fromkeys([c.strip() for c in all_configs if c.strip()]))
    
    # چسباندن با اینتر (Line Break)
    merged_configs = "\n".join(unique_configs)
    
    # تبدیل به Base64 استاندارد بدون کاراکترهای اضافی
    final_base64 = base64.b64encode(merged_configs.encode('utf-8')).decode('utf-8')
    
    with open("sub_link.txt", "w") as f:
        f.write(final_base64)

if __name__ == "__main__":
    get_configs()
