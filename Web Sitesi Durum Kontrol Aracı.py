import requests

print("--- Web Sitesi Durum Kontrol Aracı ---")
print("Not: Lütfen adresi yazarken başına 'https://' veya 'http://' eklemeyi unutmayın.")

adres = input("Kontrol edilecek sitenin adresini girin: ")

try:
    cevap = requests.get(adres)
    
    durum_kodu = cevap.status_code
    
    print("\nSonuçlar:")
    print("-------------------------")
    print("HTTP Status Kodu:", durum_kodu)
    
    if durum_kodu == 200:
        print("Durum: Site sorunsuz bir şekilde çalışıyor! (200 OK)")
    elif durum_kodu == 403:
        print("Durum: Bu sayfaya erişim izniniz yok. (403 Forbidden)")
    elif durum_kodu == 404:
        print("Durum: Aradığınız sayfa bulunamadı. (404 Not Found)")
    elif durum_kodu == 500:
        print("Durum: Sitenin sunucusunda bir hata var. (500 Internal Server Error)")
    else:
        print("Durum: Siteye ulaşıldı ama farklı bir durum kodu döndü.")

except requests.exceptions.RequestException:
    print("\nBağlantı Hatası: Siteye ulaşılamadı!")
    print("Lütfen internet bağlantınızı ve girdiğiniz adresi (https:// kısmını) kontrol edin.")