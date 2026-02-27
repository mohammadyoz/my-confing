import requests
import re
import base64
from datetime import datetime

def get_configs():
    # لیست اختصاصی شما که درخواست دادید
    channels = [
        'Farah_VPN', 'letsproxys', 'shankamil', 'AzadNet', 'MoonsterVpn',
        'ProxGp', 'ConfingV2RaayNG', 'Pruuxi', 'sina_tec', 'v2rayng_fars',
        'v2rayipm', 'SOSkeyNET', 'vpn_proxy_trading', 'FreakConfig', 'V2HUBIR',
        'Confing_m1SHAP', 'NPV_78', 'EmKavpn', 'filtershekanfilm', 'mtmvpn', 'hddify'
    ]
    
    all_links = []
    # دریافت ساعت برای جلوگیری از کش و نمایش زمان آپدیت
    current_time = datetime.now().strftime("%H:%M")
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    for ch in channels:
        try:
            # استفاده از نسخه s/ برای استخراج مستقیم از وب
            res = requests.get(f"https://t.me/s/{ch}", headers=headers, timeout=15)
            if res.status_code == 200:
                # استخراج تمام پروتکل‌های معروف
                found = re.findall(r'(?:vless|vmess|trojan|ss|tuic|hysteria2)://[^\s<"\'#]+', res.text)
                if found:
                    # برداشتن ۲۰ کانفیگ آخر از هر کانال برای لیست پربارتر
                    for link in found[-20:]: 
                        # تمیز کردن لینک و اضافه کردن نام کانال و زمان
                        base_link = link.split('#')[0]
                        clean_link = f"{base_link}#{ch}-{current_time}"
                        all_links.append(clean_link)
        except:
            continue
    
    # حذف لینک‌های تکراری
    unique_links = list(dict.fromkeys(all_links))
    result_text = "\n".join(unique_links)
    
    # تبدیل کل لیست به فرمت Base64 برای اشتراک (Subscription)
    b64_output = base64.b64encode(result_text.encode('utf-8')).decode('utf-8')
    
    with open("sub_link.txt", "w") as f:
        f.write(b64_output)

if __name__ == "__main__":
    get_configs()
