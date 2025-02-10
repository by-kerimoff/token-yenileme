import time
import requests

# Yeni token alan funksiya
def get_new_token():
    # Burada yeni token alınır. Məsələn, bir API istifadə edə bilərsiniz.
    # API ünvanını və parametrləri əlavə edin.
    api_url = "https://www.canlitv.me//getToken"  # Token alınan API ünvanı
    response = requests.get(api_url)
    new_token = response.json()["token"]  # API cavabından tokeni çıxarın
    return new_token

# Linki yeniləyən funksiya
def update_m3u8_link(token):
    base_url = "https://cdn7.canlitv.me/kanald.m3u8"
    tms = int(time.time())  # Hazırki zamanı alırıq
    new_link = f"{base_url}?tkn={token}&tms={tms}"
    return new_link

# Əsas proqram
def main():
    while True:
        # Yeni token alınır
        token = get_new_token()
        
        # Link yenilənir
        m3u8_link = update_m3u8_link(token)
        print(f"Yeni m3u8 linki: {m3u8_link}")
        
        # 1 saat gözləyirik (tokenin müddəti bitənə qədər)
        time.sleep(3600)

# Proqramı başlat
if name == "main":
    main()
