# JableTV Downloader (Uzbek Manual)

Bu dastur JableTV saytidan videolarni yuklab olishga yordam beradi.

## O'rnatish (Installation)

1.  **Python va FFmpeg o'rnatilgan bo'lishi kerak.**
2.  **ChromeDriver yuklab olish:**
    *   Google Chrome brauzeringiz versiyasiga mos [ChromeDriver](https://chromedriver.chromium.org/downloads) ni yuklab oling.
    *   `chromedriver.exe` faylini ushbu papkaga (kod turgan joyga) tashlang.
3.  **Kutubxonalarni o'rnatish:**
    Terminalda quyidagi buyruqni bering:
    ```bash
    pip install -r requirements.txt
    pip install Flask
    ```

## Ishlatish (Usage)

### 1. Web orqali (Eng oson)

1.  Dasturni ishga tushiring:
    ```bash
    python web_app.py
    ```
2.  Brauzerda `http://127.0.0.1:5000` manziliga kiring.
3.  Video linkini qo'yib "Yuklash" tugmasini bosing.

### 2. Terminal orqali

To'g'ridan-to'g'ri terminalda ham ishlatish mumkin:

```bash
python main.py --url "VIDEO_LINKI"
```
Masalan:
```bash
python main.py --url https://jable.tv/videos/ipx-486/
```

## Muammolar yechimi

*   **ChromeDriver xatosi:** Agar "chromedriver executable needs to be in PATH" desa, `chromedriver.exe` fayli `main.py` bilan bir papkada ekanligiga ishonch hosil qiling.
*   **FFmpeg xatosi:** Videoni mp4 ga aylantirish uchun FFmpeg kerak. Agar o'rnatilmagan bo'lsa, uni o'rnatib `PATH` ga qo'shish kerak.

---
Original Repository: [hcjohn463/JableTVDownload](https://github.com/hcjohn463/JableTVDownload)
