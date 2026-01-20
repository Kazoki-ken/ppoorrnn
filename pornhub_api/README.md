# PornHub Unofficial API (Fixed)

Ushbu kutubxona PornHub.com saytidan ma'lumotlarni (videolar va aktyorlar) olish uchun mo'ljallangan. Ushbu versiya yangi sayt dizayniga moslashtirilgan.

## O'rnatish (Installation)

Ishlatishdan oldin kerakli kutubxonalarni o'rnatishingiz shart. Terminalda quyidagi buyruqni bajaring:

```bash
pip install -r requirements.txt
```

Yoki alohida-alohida o'rnatish:

```bash
pip install beautifulsoup4 requests lxml
```

## Ishlatish (Usage)

Kutubxonani ishga tushirish uchun tayyor `final_demo.py` faylidan foydalanishingiz mumkin.

Terminalda ushbu papkaga kirib, quyidagi buyruqni yozing:

```bash
python final_demo.py
```
(Yoki `python3 final_demo.py`)

### Namuna kod

O'zingizning skriptingizda quyidagicha ishlatishingiz mumkin:

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

# 2. Aktyorlarni olish
print("\nAktyorlar olinmoqda...")
stars = client.getStars(quantity=5, page=1)

for star in stars:
    print(f"Ism: {star.get('name')}")
    print(f"Link: {star.get('url')}")
```

## Troubleshooting (Muammolar va yechimlar)

Agar `ModuleNotFoundError: No module named 'bs4'` xatosini olsangiz, demak `beautifulsoup4` o'rnatilmagan. Yuqoridagi **O'rnatish** bo'limiga qarang.

---
Original repository: [sskender/pornhub-api](https://github.com/sskender/pornhub-api)
