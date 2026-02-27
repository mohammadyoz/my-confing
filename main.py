// نمونه ساده برای جمع‌آوری لینک از بات‌ها یا کانال‌های عمومی
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const telegramChannels = [
    'channel1', // نام کاربری کانال اول بدون @
    'channel2'  // نام کاربری کانال دوم
  ];
  
  let allConfigs = "";

  for (const channel of telegramChannels) {
    const url = `https://t.me/s/${channel}`;
    const response = await fetch(url);
    const text = await response.text();
    
    // استخراج لینک‌های VLESS, VMess, Trojan با Regex
    const vlessRegex = /vless:\/\/[^\s<"']+/g;
    const matches = text.match(vlessRegex);
    
    if (matches) {
      allConfigs += matches.join('\n') + '\n';
    }
  }

  return new Response(btoa(allConfigs), {
    headers: { 'content-type': 'text/plain; charset=utf-8' }
  });
}
