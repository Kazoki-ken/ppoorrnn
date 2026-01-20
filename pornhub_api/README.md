# PornHub Unofficial API (Fixed) & Video Downloader

Ushbu loyiha ikki qismdan iborat:
1.  **API:** PornHub.com saytidan ma'lumotlarni (videolar va aktyorlar) olish.
2.  **Web Downloader:** Har qanday video linkini (PornHub, YouTube va boshqalar) yuklab olish uchun oddiy web interfeys.

## O'rnatish (Installation)

Ishlatishdan oldin kerakli kutubxonalarni o'rnatishingiz shart. Terminalda quyidagi buyruqni bajaring:

```bash
pip install -r requirements.txt
```

## 1. Web Video Yuklagichni ishlatish (Tavsiya etiladi)

Bu eng oson yo'li. Videolarni to'g'ridan-to'g'ri yuklash uchun:

1.  Terminalda quyidagi buyruqni yozing:
    ```bash
    python app.py
    ```
2.  Brauzeringizni oching va manzil qatoriga yozing: `http://127.0.0.1:5000`
3.  Video linkini kiritib "Yuklash" tugmasini bosing.
4.  Video `downloads` papkasiga tushadi.

## 2. API Kodini ishlatish (Dasturchilar uchun)

Agar sizga faqat ma'lumotlar (json) kerak bo'lsa:

```bash
python final_demo.py
```

### Namuna kod

```python
import pornhub

# Mijozni ishga tushirish
client = pornhub.PornHub([])

# 1. Videolarni olish
print("Videolar olinmoqda...")
videos = client.getVideos(quantity=5, page=1)

for video in videos:
    print(f"Sarlavha: {video.get('title')}")
    print(f"Link: {video.get('url')}")
```

## Troubleshooting (Muammolar va yechimlar)

*   `ModuleNotFoundError`: Kutubxonalar o'rnatilmagan. `pip install -r requirements.txt` buyrug'ini qayta ishlating.
*   Yuklashda xatolik bo'lsa: `yt-dlp` versiyasi eski bo'lishi mumkin. `pip install --upgrade yt-dlp` qiling.

---
Original repository: [sskender/pornhub-api](https://github.com/sskender/pornhub-api)
