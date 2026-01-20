# JableTV Downloader (Web Interface + Video Player)

Ushbu dastur JableTV saytidan videolarni yuklab olish, formatlash va to'g'ridan-to'g'ri ko'rish uchun mo'ljallangan qulay web interfeysdir.

## Xususiyatlari
*   **Video Yuklash:** Link orqali videolarni oson yuklash.
*   **Formatlash (Convert):** Videolarni MP4 formatiga o'tkazish (CPU yoki GPU yordamida).
*   **Video Player:** Yuklangan videolarni shu yerni o'zida ko'rish imkoniyati.
*   **Orqa fon rejimi:** Yuklash jarayoni veb-sahifani qotirib qo'ymaydi.

## O'rnatish (Installation)

1.  **Talablar:**
    *   Python 3.x
    *   Google Chrome Brauzeri
    *   [ChromeDriver](https://chromedriver.chromium.org/downloads) (Chrome versiyangizga mosini yuklab, shu papkaga tashlang)
    *   [FFmpeg](https://ffmpeg.org/download.html) (Videolarni formatlash uchun kerak. `PATH` ga qo'shilgan bo'lishi shart)

2.  **Kutubxonalarni o'rnatish:**
    Terminalda quyidagi buyruqni bering:
    ```bash
    pip install -r requirements.txt
    pip install Flask
    ```

## Ishlatish (Usage)

1.  Dasturni ishga tushiring:
    ```bash
    python web_app.py
    ```
2.  Brauzeringizda **`http://127.0.0.1:5000`** manziliga kiring.
3.  **Video yuklash:**
    *   Video linkini kiriting.
    *   Formatlash turini tanlang (masalan, "mp4 ga aylantirish").
    *   "Yuklashni Boshlash" tugmasini bosing.
4.  **Videolarni ko'rish:**
    *   Yuqoridagi menyudan "Yuklanganlar" bo'limiga o'ting.
    *   Ro'yxatdan videoni tanlab, "Ko'rish" tugmasini bosing.

## Formatlash turlari haqida
*   **0: Formatlashsiz (Tezkor):** Video `ts` bo'laklaridan iborat bo'ladi, lekin birlashtiriladi. Eng tez usul.
*   **1: mp4 ga aylantirish (Tavsiya):** Standart usul. Sifat o'zgarmaydi, lekin hamma qurilmalarda ochiladi.
*   **2: GPU orqali:** Agar sizda NVIDIA videokartasi bo'lsa, bu juda tez ishlaydi.
*   **3: CPU orqali:** Protsessor kuchidan foydalanadi (sekinroq bo'lishi mumkin).

---
Original Repository: [hcjohn463/JableTVDownload](https://github.com/hcjohn463/JableTVDownload)
