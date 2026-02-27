import requests
import re
import base64
from datetime import datetime
import time

def get_configs():
    # لیست کامل و آپدیت شده شامل کانال‌های جدید
    channels = [
        'Farah_VPN', 'letsproxys', 'shankamil', 'AzadNet', 'MoonsterVpn',
        'ProxGp', 'ConfingV2RaayNG', 'Pruuxi', 'sina_tec', 'v2rayng_fars',
        'v2rayipm', 'SOSkeyNET', 'vpn_proxy_trading', 'FreakConfig', 'V2HUBIR',
        'Confing_m1SHAP', 'NPV_78', 'EmKavpn', 'filtershekanfilm', 'mtmvpn', 
        'hddify', 'filembad', 'prrofile_purple'
    ]
    
    all_links = []
    current_time = datetime.now().strftime("%H:%M")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    # کلمات کلیدی برای فیلتر کردن و بیرون کشیدن لینک‌های بیشتر
    keywords = ['vless', 'vmess', 'ss', 'trojan']

    for ch in channels:
        try:
            # ۱. بررسی صفحه اصلی کانال
            search_urls = [f"https://t.me/s/{ch}"]
            
            # ۲. اضافه کردن جستجوی اختصاصی برای کانال‌های پرپست
            for kw in keywords:
                search_urls.append(f"https://t.me/s/{ch}?q={kw}")

            for url in search_urls:
                res = requests.get(url, headers=headers, timeout=15)
                if res.status_code == 200:
                    # استخراج با ریجکس تقویت شده
                    found = re.findall(r'(?:vless|vmess|trojan|ss|tuic|hysteria2)://[^\s<"\'#]+', res.text)
                    if found:
                        # برداشتن ۵۰ مورد آخر از هر نتیجه جستجو
                        for link in found[-50:]: 
                            base_link = link.split('#')[0]
                            all_links.append(f"{base_link}#{ch}-{current_time}")
                time.sleep(0.2) # جلوگیری از بلاک شدن توسط تلگرام
        except:
            continue
    
    # حذف تکراری‌ها و مرتب‌سازی
    unique_links = list(dict.fromkeys(all_links))
    result_text = "\n".join(unique_links)
    
    # تبدیل به فرمت Base64 برای سابسکریپشن
    b64_output = base64.b64encode(result_text.encode('utf-8')).decode('utf-8')
    
    with open("sub_link.txt", "w") as f:
        f.write(b64_output)

if __name__ == "__main__":
    get_configs()
