import requests
import re
import base64
from datetime import datetime

def get_configs():
    # لیست کانال‌های قوی و جدید
    channels = [
        'V2ray_Alpha', 'v2freeall', 'v2ray_outline_config', 'v2ray_free_confing',
        'VlessConfig', 'V2RayConfigGenerator', 'v2rayng_vpn', 'FreeVlessConfig',
        'V2rayNG_Config_free', 'v2ray_configs_pool', 'vmess_vless_v2rayng',
        'v2rayNG_VPNN', 'ConfigV2rayNG', 'PrivateVPNs', 'V2rayNG_Free_Configs'
    ]
    
    all_links = []
    # دریافت زمان فعلی برای جلوگیری از کش شدن
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    for ch in channels:
        try:
            res = requests.get(f"https://t.me/s/{ch}", timeout=15)
            if res.status_code == 200:
                found = re.findall(r'(?:vless|vmess|trojan|ss|tuic|hysteria2)://[^\s<"\'#]+', res.text)
                if found:
                    for link in found[-10:]: # ۱۰ تای آخر هر کانال
                        # اضافه کردن برچسب زمان به انتهای نام کانفیگ
                        if "#" in link:
                            clean_link = f"{link}-{current_time}"
                        else:
                            clean_link = f"{link}#{ch}-{current_time}"
                        all_links.append(clean_link)
        except:
            continue
    
    unique_links = list(dict.fromkeys(all_links))
    result_text = "\n".join(unique_links)
    
    # تبدیل به Base64
    b64_output = base64.b64encode(result_text.encode('utf-8')).decode('utf-8')
    
    with open("sub_link.txt", "w") as f:
        f.write(b64_output)

if __name__ == "__main__":
    get_configs()
