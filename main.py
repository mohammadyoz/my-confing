import requests
import re
import base64
from datetime import datetime

def get_configs():
    # لیست بسیار کامل‌تر از کانال‌های فعال
    channels = [
        'V2ray_Alpha', 'v2freeall', 'v2ray_outline_config', 'v2ray_free_confing',
        'VlessConfig', 'V2RayConfigGenerator', 'v2rayng_vpn', 'FreeVlessConfig',
        'V2rayNG_Config_free', 'v2ray_configs_pool', 'vmess_vless_v2rayng',
        'v2rayNG_VPNN', 'ConfigV2rayNG', 'PrivateVPNs', 'V2rayNG_Free_Configs',
        'customv2ray', 'v2ray_swat', 'V2ray_S_A', 'v2ray_premium', 'vpn_factory',
        'v2free_config', 'V2rayNG_Configuration', 'v2rayng_fast', 'free_v2ray_config'
    ]
    
    all_links = []
    current_time = datetime.now().strftime("%H:%M") # فقط ساعت برای کوتاه‌تر شدن اسم
    
    for ch in channels:
        try:
            res = requests.get(f"https://t.me/s/{ch}", timeout=15)
            if res.status_code == 200:
                found = re.findall(r'(?:vless|vmess|trojan|ss|tuic|hysteria2)://[^\s<"\'#]+', res.text)
                if found:
                    # حالا ۵۰ تای آخر هر کانال را برمی‌داریم
                    for link in found[-50:]: 
                        if "#" in link:
                            # حذف امضای قبلی کانال و جایگزینی با ساعت خودمان
                            base_link = link.split('#')[0]
                            clean_link = f"{base_link}#{ch}-{current_time}"
                        else:
                            clean_link = f"{link}#{ch}-{current_time}"
                        all_links.append(clean_link)
        except:
            continue
    
    # حذف تکراری‌ها
    unique_links = list(dict.fromkeys(all_links))
    result_text = "\n".join(unique_links)
    
    b64_output = base64.b64encode(result_text.encode('utf-8')).decode('utf-8')
    
    with open("sub_link.txt", "w") as f:
        f.write(b64_output)

if __name__ == "__main__":
    get_configs()
